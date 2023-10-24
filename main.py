from functions import *
asking = True
# Create table first (Do this once)

if __name__ == '__main__':
    create_table()  # Create table if it doesn't exist
    while True:  # Loop to allow multiple questions
        chosenChapter, userQuestion = findCorrectChapter()
        print(f"Valt kapitel: {chosenChapter}")
        insuranceAnswer = findCorrectAnswer()
        saveQA(userQuestion, insuranceAnswer)
        ask_again = goAgane()
        if not ask_again:
            break  # Break the loop if user does not want to ask another question
