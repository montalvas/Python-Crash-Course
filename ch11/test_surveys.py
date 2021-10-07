import unittest
from surveys import AnonymousSurvey

# O nome da classe teste é: Test + nome da própria classe


class TestAnonymousSurvey(unittest.TestCase):
    """Testes para a classe AnonymousSurvey"""

    def test_store_single_response(self):
        """Testa se uma única resposta é armazenada de forma apropriada."""
        my_survey = AnonymousSurvey(
            "What language did you first learn to speak?")
        my_survey.store_response('English')

        #Verifica se a resposta está na lista
        self.assertIn('English', my_survey.responses)
    
    def test_store_multiple_responses(self):
        """Teste se várias respostas são armazenadas de forma apropriada."""
        my_survey = AnonymousSurvey(
            "What language did you first learn to speak?")
        responses = ['English', 'Spanish', 'Portuguese', 'Japanese']
        
        for response in responses:
            my_survey.store_response(response)
        
        # Testa se cada resposta foi armazenada na instancia
        for response in responses:
            self.assertIn(response, my_survey.responses)


unittest.main()
