from survey import AnonymousSurvey

# define a question and make a survey
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# show the question, and store responses to the question
my_survey.show_question()
print("Enter 'q' to exit")

while True:
    response = input("Language: ")

    if response == 'q':
        print("bye bye")

        break

    my_survey.store_response(response)

# show the survey result
print("\nThanks for participate!")
my_survey.show_results()