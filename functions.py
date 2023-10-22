from flask import Flask, request, render_template, jsonify
import os
import openai
import sqlite3
from termsDataBase import trafficInsuranceTerms, commonTerms, fireTerms, glassTerms, theftTerms, motorAndElectronicsTerms, drulleTerms
from termsDataBase import liabilityTrollyHousecarTerms, travelBreakTerms, crisisHelpTerms, towingTerms, legalProtectionTerms, vehicleDamageTerms, rentalCarTerms, deductibleDiscountTerms, privateCareTerms, extraProtectionElectricAndHybridTerms, carInsuranceLargeTerms, propertyInCarTerms


debug = True

if debug:
    print("Setting OpenAI API key...")
else:
    pass

openai.api_key = os.environ['OPENAI_API_KEY']



def findCorrectChapter():
    global chosenChapter
    global userQuestion
    if debug:
        print("About to ask for the user's question...")
    else:
        pass
    userQuestion = input("Vad är din fråga? \n ")

    messages = [
        {"role": "system",
         "content": "You are a helpful assistant working at an insurance company. "
                    "Here are chapters from our terms & conditions:"
            """" 1. Trafikförsäkring 
2. Gemensamma bestämmelser
3. Brand
4. Glasrutor
5. Stöld och inbrott
6. Motor och elektronik för personbil, lätt lastbil och husbil
7. Motor och elektronik för husvagn
8. Drulle
9. Ansvar för husbil och husvagn
10. Reseavbrott för husbil och husvagn
11. Krishjälp
12. Bärgning
13. Rättsskydd för fordonet
14. Vagnskada
15. Hyrbil 
16. Självriskrabatt 3 000 kr 
17. Privat vård och ersättning för medicinsk invaliditet efter trafikolycka
18. Extra skydd för elbil och laddhybrid
19. Bilförsäkring stor
20. Egendom i bil 
"""},
        {"role": "user",
         "content": f"Based on the users question, find the right chapter in the terms&conditions where the answer lies. Reply only with the chapter name. Users question: {userQuestion}."},
    ]
    if debug:
        print("Calling OpenAI API to find the correct chapter...")
    else:
        pass
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )
    chosenChapter = response['choices'][0]['message']['content']
    print(f"Chosen chapter is: {chosenChapter}")
    return chosenChapter.strip()
def storeTermsAsVariable():
    if debug:
        print("Storing terms as variable...")
    else:
        pass

    chapter_terms = {
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
    if chosenChapter in chapter_terms:
        selected_chapter_terms = chapter_terms[chosenChapter]
    else:
        print("Kapitlet finns inte")
        selected_chapter_terms = None
    if debug:
        print(f"Stored terms (first 50 characters): {selected_chapter_terms[:100]}...")
    else:
        pass

    return selected_chapter_terms
def findCorrectAnswer():
    if debug:
        print("Finding the correct answer...")
    else:
        pass
    messages = [
        {"role": "system",
         "content": "Du är en hjälpsam assistent som svarar på frågor om försäkring för företag. Om du inte är säker på ditt svar kan du använda generellt resonemang och datan du är tränad på för att svara. "
                    " Du är en expert på försäkring, underwriting och skadereglering. Ditt svar ska vara kortfattat och lätt att förstå. "
                    "Här är villkoren för kapitlet där svaret finns på användarens fråga:"
            """"{chapterText1}"""},
        {"role": "user",
         "content": f"Användarens fråga som du ska besvara: {userQuestion}. Svara med den del av villkoret där du hittat svaret, samt svaret på frågan."},
    ]

    if debug:
        print("Calling OpenAI API to find the correct answer...") # Debugging: Indicate that the OpenAI API is about to be called
    else:
        pass
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )
    insuranceAnswer = response['choices'][0]['message']['content']
    if debug:
        print(f"Generated answer is: {insuranceAnswer}")
    else:
        pass
    return insuranceAnswer.strip()
