from functions import *
asking = True
# Create table first (Do this once)

if __name__ == '__main__':
    create_table()  # Create table if it doesn't exist
    if megaDebug:
        viewDatabaseQ = input("Vill du se databasen? (Ja/Nej) \n")
        if viewDatabaseQ.lower() == "ja":
            checkDataBase()
        else:
            pass
    while True:  # Loop to allow multiple questions
        chosenChapter, userQuestion = findCorrectChapter()
        insuranceAnswer = findCorrectAnswer()

        # Translate the answer to Swedish
        insuranceAnswer = translate_text(insuranceAnswer, target_lang='sv')

        print(insuranceAnswer)
        saveQA(userQuestion, insuranceAnswer)
        ask_again = goAgane()
        if not ask_again:
            break  # Break the loop if user does not want to ask another question
