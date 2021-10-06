from surveys import AnonymousSurvey

# Define uma pergunta e cria uma pesquisa
my_survey = AnonymousSurvey("What language did you first learn to speak?")

# Mostra a pergunte e armazena as respostas
my_survey.show_question()

print("Print 'q' anytime to quit.")
while True:
    response = input("\nLanguage: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Exibe os resultados da pesquisa:
print("Thank you to everyone who participated in the survey!")
my_survey.show_results()
