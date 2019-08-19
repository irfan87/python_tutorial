class AnonymousSurvey:
    # store a question, and prepare to store responses
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        # show the survey question
        print(self.question)

    def store_response(self, new_response):
        # store a single response to the survey
        self.responses.append(new_response)

    def show_results(self):
        # show all the responses that have been given
        print("Survey results")

        for response in self.responses:
            print(f"- {response.title()}")