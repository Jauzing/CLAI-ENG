import os
import openai
import sqlite3
from termsDataBase import trafficInsuranceTerms, commonTerms, fireTerms, glassTerms, theftTerms, motorAndElectronicsTerms, drulleTerms
from termsDataBase import liabilityTrollyHousecarTerms, travelBreakTerms, crisisHelpTerms, towingTerms, legalProtectionTerms, vehicleDamageTerms, rentalCarTerms, deductibleDiscountTerms, privateCareTerms, extraProtectionElectricAndHybridTerms, carInsuranceLargeTerms, propertyInCarTerms


debug = False # Set to True to enable debugging
megaDebug = False # Set to True to enable extended debugging

if debug:
    print("Setting OpenAI API key...")
else:
    pass

openai.api_key = os.environ['OPENAI_API_KEY'] # Set the OpenAI API key as a environment variable in the OS

def findCorrectChapter(): # Function to find the correct chapter
    global chosenChapter # Make the variable global so it can be used outside the function
    global userQuestion
    if debug:
        print("Ber användaren om frågan... \n ")
    else:
        pass
    userQuestion = input("Vad är din fråga? \n ") # Ask the user for their question

    messages = [ # Create a list of messages to send to the OpenAI API
        {"role": "system",
         "content": "Du är en hjälpsam assistent som arbetar på ett försäkringsbolag. "
                    " Här är kapitel från företagets villkor för företagsfordon:"
            """" Trafikförsäkring 
                Gemensamma bestämmelser
                Brand
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
         "content": f"Baserat på användarens fråga, hitta rätt kapitel i villkoren där svaret finns."
         f"Svara endast med namnet på kapitlet. Om det kan finnas flera kapitel som innehåller svaret, svara med samtliga. Användarens fråga: {userQuestion}."},
    ]
    if debug:
        print(" Anropar OpenAI API för att hitta rätt kapitel... \n")
    else:
        pass
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )
    chosenChapter = response['choices'][0]['message']['content'] # Store the chapter in a variable
    storeTermsAsVariable() # Call the function to store the terms as a variable
    return chosenChapter.strip(), userQuestion  # Return the chapter and userQuestion stripped of whitespace


def storeTermsAsVariable():
    if debug:
        print(" Laddar in alla kapitel i villkoret som variabler... \n")
    else:
        pass

    chapter_terms = { # Create a dictionary with the chapters and their variable names that store the terms
        "Trafikförsäkring": trafficInsuranceTerms,
        "Gemensamma bestämmelser": commonTerms,
        "Brand": fireTerms,
        "Glasrutor": glassTerms,
        "Stöld och inbrott": theftTerms,
        "Motor och elektronik för personbil, lätt lastbil och husbil": motorAndElectronicsTerms,
        "Motor och elektronik för husvagn": motorAndElectronicsTerms,
        "Drulle": drulleTerms,
        "Ansvar för husbil och husvagn": liabilityTrollyHousecarTerms,
        "Reseavbrott för husbil och husvagn": travelBreakTerms,
        "Krishjälp": crisisHelpTerms,
        "Bärgning": towingTerms,
        "Rättsskydd för fordonet": legalProtectionTerms,
        "Vagnskada": vehicleDamageTerms,
        "Hyrbil": rentalCarTerms,
        "Självriskrabatt 3 000 kr": deductibleDiscountTerms,
        "Privat vård och ersättning för medicinsk invaliditet efter trafikolycka": privateCareTerms,
        "Extra skydd för elbil och laddhybrid": extraProtectionElectricAndHybridTerms,
        "Bilförsäkring stor": carInsuranceLargeTerms,
        "Egendom i bil": propertyInCarTerms,
    }

    # Check if the chosen chapter exists in the dictionary
    global selected_chapter_terms # Make the variable global so it can be used outside the function
    selected_chapter_terms = [] # Create an empty list to store the terms to enable multiple chapter answers

    for chapter in chosenChapter.split('\n'): # Split the chosen chapter into a list of chapters
        if chapter in chapter_terms: # Check if the chapter exists in the dictionary
            selected_chapter_terms.append(chapter_terms[chapter]) # If it does, append the terms to the list
            if megaDebug:
                print(f"Valda kapitel {chosenChapter}")
            else:
                pass
        else: # If the chapter doesn't exist in the dictionary
            print(f"Kapitlet {chapter} finns inte") # Print that the chapter doesn't exist
    print(f"Samtliga utvalda kapitel: {chosenChapter}  \n")

    if megaDebug: # If extended debugging is wanted
        print(f"Stored terms (first 50 characters): {selected_chapter_terms[:100]}...") # Print the first 50 characters of the terms
    else:
        pass # If extended debugging is not wanted, do nothing

    return selected_chapter_terms # Return the list of terms
def findCorrectAnswer(): # Function to find the correct answer
    global insuranceAnswer
    if debug:
        print(" Hittar rätt svar...")
    else:
        pass
    messages = [ # Create a list of messages to send to the OpenAI API
        {"role": "system",
         "content": f"Du är en hjälpsam assistent som svarar på frågor om försäkring för företag. Om du inte hittar exakt rätt svar i villkoret kan du använda generellt resonemang och din träningsdata för att svara. "
                    " Du är en expert på försäkring, underwriting och skadereglering. Ditt svar ska vara kortfattat och lätt att förstå. "
                    "Här är villkoren för kapitlet där svaret finns på användarens fråga:"
            f""""{selected_chapter_terms}"""},
        {"role": "user", # Create a user message with the user's question
         "content": f"Användarens fråga som du ska besvara: {userQuestion}. Citera först den delen i villkoret där du hittat svaret. Två rader under det skriver du svaret på frågan. Exempel: Fråga: Vart blir jag bärgad om jag krockar? Du svarar följande: \n  Villkorstext: Vid bärgning bärgas bilen till närmaste verkstad. Om kundens bostad är närmare än verkstaden kan kunden välja att bli bärgad dit. \n Svar:Bilen bärgas till närmaste verkstad."},
    ]

    response = openai.ChatCompletion.create( # Call the OpenAI API
        model="gpt-4",
        messages=messages
    )
    if megaDebug:
        print(" Hittat svar!")  # Debugging: Indicate that the OpenAI API is about to be called
    else:
        pass
    insuranceAnswer = response['choices'][0]['message']['content'] # Store the answer in a variable
    if debug:
        print(f"Generated answer is: {insuranceAnswer}")
    else:
        pass
    print(f"Det genererade svaret är: {insuranceAnswer}")
    return insuranceAnswer.strip() # Return the answer stripped of whitespace


# Function to check if the user wants to ask another question
def goAgane():
    while True:
        asking = input("Vill du ställa en till fråga? (Ja/Nej) \n")
        if asking.lower() == "ja":
            return True
        elif asking.lower() == "nej":
            print("Tack för att du använde vår tjänst!")
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
    print("Sparar fråga och svar till databasen...")

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