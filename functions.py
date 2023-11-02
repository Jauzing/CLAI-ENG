import os
import openai
import sqlite3
from termsDataBase import *
from googletrans import Translator
import time

debug = True  # Set to True to enable debugging
megaDebug = False  # Set to True to enable extended debugging

### VARIABLES ###

temprating = 0.7  # Set the temperature rating for the OpenAI API
model = "gpt-4"  # Set the model for the OpenAI API



def translate_text(text, target_lang='sv'):
    try:
        translator = Translator()
        translated = translator.translate(text, dest=target_lang)
        return translated.text
    except Exception as e:
        print(f"Translation failed: {e}")
        return text

# Function to print debug messages
def debug_print(message):
    if debug:
        print(message)


# Function to print extended debug messages
def mega_debug_print(message):
    if megaDebug:
        print(message)
    else:
        pass


### API KEY SETUP ###
debug_print("Setting OpenAI API key...")
openai.api_key = os.environ['OPENAI_API_KEY']  # Set the OpenAI API key as a environment variable in the OS


def findCorrectChapter(): # Function to find the correct chapter
    global chosenChapter # Make the variable global so that it can be used outside the function
    global userQuestion

    debug_print("Setting OpenAI API key...")

    userQuestion = input("\n Vad är din fråga? \n -> ") # Ask the user for their question

    messages = [ # Create a list of messages to send to the OpenAI API
        {"role": "system",
         "content": "Du är en hjälpsam assistent som arbetar på ett försäkringsbolag. "
                    " Här är kapitel från företagets villkor för företagsfordon:"
            """" Trafikförsäkring 
                Gemensamma bestämmelser
                Fire Damage Insurance for Vehicles
                Glasrutor
                Stöld och inbrott 
                Motor och elektronik för personbil, lätt lastbil och husbil 
                Motor och elektronik för husvagn
                Drulle
                Ansvar för husbil och husvagn
                Reseavbrott för husbil och husvagn
                Krishjälp
                Bärgning
                Rättsskydd för fordonet
                Vagnskada
                Hyrbil 
                Självriskrabatt 3 000 kr 
                Privat vård och ersättning för medicinsk invaliditet efter trafikolycka
                Extra skydd för elbil och laddhybrid
                Bilförsäkring stor
                Egendom i bil 
                """},

        {"role": "user", # Create a user message with the user's question
         "content": f"Baserat på användarens fråga, hitta rätt kapitel i villkoren där svaret finns. Användaren kan ibland stava fel, använda slang eller skriva på ett annat sätt än exakt vad som står i villkoret. Fundera på om det finns några synonymer eller andra sätt att uttrycka sig på som användaren kan ha använt."
         f"Svara endast med namnet på kapitlet. Om det kan finnas flera kapitel som innehåller svaret, svara med samtliga. Användarens fråga: {userQuestion}."},
    ]

    debug_print("Anropar OpenAI API för att hitta rätt kapitel... \n") # Debugging: Indicate that the OpenAI API is about to be called


    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )
    chosenChapter = response['choices'][0]['message']['content'] # Store the chapter in a variable
    storeTermsAsVariable() # Call the function to store the terms as a variable
    return chosenChapter.strip(), userQuestion  # Return the chapter and userQuestion stripped of whitespace

def storeTermsAsVariable():

    debug_print("Laddar in alla kapitel i villkoret som variabler... \n")

    chapter_terms = { # Create a dictionary with the chapters and their variable names that store the terms
        "Traffic Insurance Conditions and Deductible Provisions": trafficInsuranceTerms,
        "General Provisions for Vehicle Insurance Coverage": commonTerms,
        "Fire Damage Insurance for Vehicles": fireTerms,
        "Glass Breakage Coverage for Vehicle Windows": glassTerms,
        "Theft and Burglary Protection for Vehicles": theftTerms,
        "Motor and Electronics Insurance for Personal Vehicles, Light Trucks, and Motorhomes": motorAndElectronicsTerms,
        "Coverage for Internal Equipment and Systems in Privately and Commercially Owned Caravans": motorAndElectronicsTerms,
        "All-Risk 'Clumsy' Coverage for Personal and Light Commercial Vehicles": drulleTerms,
        "Liability for mobile home and caravan": liabilityTrollyHousecarTerms,
        "Interrupted Journey Coverage for Motorhomes and Caravans": travelBreakTerms,
        "Crisis Assistance Coverage Provisions": crisisHelpTerms,
        "Towing and Transportation Coverage Details": towingTerms,
        "Legal Protection Coverage for Motor Vehicles": legalProtectionTerms,
        "Vehicle Damage Coverage and Exclusions, Collisions": vehicleDamageTerms,
        "Rental Car Coverage and Compensation Guidelines": rentalCarTerms,
        "Deductible Provisions for Collisions, Vandalism, Parking, and Towing. Deductible reduction 3000 SEK": deductibleDiscountTerms,
        "Private care and compensation for medical disability after a traffic accident": privateCareTerms,
        "Enhanced Protection for Electric and Plug-in Hybrid Vehicles": extraProtectionElectricAndHybridTerms,
        "Comprehensive Vehicle Insurance 'Big': Coverage, Exclusions, and Additional Benefits": carInsuranceLargeTerms,
        "Property in Vehicle: Coverage, Exclusions, and Deductibles": propertyInCarTerms,
    }

    # Check if the chosen chapter exists in the dictionary
    global selected_chapter_terms # Make the variable global so that it can be used outside the function
    selected_chapter_terms = [] # Create an empty list to store the terms to enable multiple chapter answers

    for chapter in chosenChapter.split('\n'): # Split the chosen chapter into a list of chapters
        if chapter in chapter_terms: # Check if the chapter exists in the dictionary
            selected_chapter_terms.append(chapter_terms[chapter]) # If it does, append the terms to the list
            mega_debug_print(f"Valda kapitel {chapter}") # Debugging: Print the chosen chapter
        else: # If the chapter doesn't exist in the dictionary
            print(f"Kapitlet {chapter} finns inte") # Print that the chapter doesn't exist

    mega_debug_print(f"Inladdat villkor (första 50 bokstäverna): {selected_chapter_terms[:100]}...") # Debugging: Print the first 50 characters of the terms
    return selected_chapter_terms # Return the list of terms


def findCorrectAnswer():  # Function to find the correct answer
    global insuranceAnswer
    debug_print(" \n Finding correct answer... \n ")  # Debugging: Indicate that the model will analyze and look for correct answer.
    messages = [  # Create a list of messages to send to the OpenAI API
        {"role": "system",  # Create
         # a system message with instructions how the model should reply.
         "content": f"""You are a helpful assistant that answers questions about business insurance.
          If you don't find the exact right answer in the text, answer 'I dont know' """
                    "Here are the terms of the chapter/s where the answer to the user's question is likely found:"
                    f""""{selected_chapter_terms}"""},

        {"role": "user",  # Create a user message with the user's question
         "content": f"""The user's question: {userQuestion}.
          First, quote the part of the condition where you found the answer. Two lines below that, you write a friendly but concise answer to the question in Swedish. Use an 🧾 emoji before quoting the terms. Use a 📌 emoji before the answer.
          Example: 🧾 Villkor: Extra skydd för elbil och laddhybrid Förlängt skydd för motor och elektronik Försäkringen gäller om bilen • är högst 12 år räknat från första registreringsdatumet. \n \n 📌 Svar: 12 år från första reg.datum.
         """},
    ]

    response = openai.ChatCompletion.create(  # Call the OpenAI API
        model=model,
        messages=messages,
        temperature=temprating,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0

    )

    mega_debug_print("\n Hittat svar!")  # Debugging: Indicate that the answer has been found
    insuranceAnswer = response['choices'][0]['message']['content']  # Store the answer in a variable

    insuranceAnswer = insuranceAnswer.replace(". ",
                                              ".\n")  # Replace each period and space with a period and a newline character

    # print(f"Det genererade svaret är: {insuranceAnswer}")

    mega_debug_print(f" \n Det genererade svaret är: {insuranceAnswer} \n ")  # Debugging: Print the generated answer
    time.sleep(5)

    # Translate
    insuranceAnswer = translate_text(insuranceAnswer, target_lang='sv')

    return insuranceAnswer


# Function to check if the user wants to ask another question
def goAgane():
    while True:
        asking = input("Finns det något mer jag kan stå till tjänst med? (Ja/Nej) \n")
        if "ja" in asking.lower() :
            return True
        elif "nej" in asking.lower() :
            print("Tack för att du använde min robot! 🤟")
            return False
        else:
            print("Vänligen följ instruktionerna! Svara med 'Ja' eller 'Nej'.")


def create_table():
    conn = sqlite3.connect('insuranceQA.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS insuranceQA (
            userQuestion TEXT,
            insuranceAnswer TEXT
        )
    ''')
    conn.commit()
    conn.close()


# Function that takes the question + answer and saves it to excel file
def saveQA(userQuestion, insuranceAnswer):
    # TODO: Behöver fråga användaren om svaret anses korrekt, innan det sparas till databasen
    print("\n Sparar fråga och svar till databasen... \n ")

    # Connect to database
    conn = sqlite3.connect('insuranceQA.db')
    c = conn.cursor()

    # Insert values into table
    c.execute("INSERT INTO insuranceQA VALUES (?, ?)", (userQuestion, insuranceAnswer))

    # Commit changes and close connection
    conn.commit()
    conn.close()

    print("Sparat!")
    return


def checkDataBase():
    # Connect to the database
    conn = sqlite3.connect('insuranceQA.db')

    # Create a cursor
    c = conn.cursor()

    # Execute a query
    for row in c.execute('SELECT * FROM insuranceQA'):
        print(row)

    # Close the connection
    conn.close()