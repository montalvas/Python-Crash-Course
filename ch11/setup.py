import unittest
from surveys import AnonymousSurvey

# Permite testar os métodos instanciando a classe apenas uma vez

class TestAnonymousSurvey(unittest.TestCase):
    """Teste para a classe AnonymousSurvey"""

    def setUp(self):
        """Cria uma pesquisa e um conjunto de respostas que poderão ser usadas
        em todos os métodos de teste"""
        
        self.my_survey = AnonymousSurvey(
            "What language did you first learn to speak?")
        self.responses = ['English', 'Spanish', 'Mandarin']
        
    def test_store_single_response(self):
        """Testa se uma única respostas é armazenada de forma apropriada."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    
    def test_store_multiple_response(self):
        """Teste se várias respostas são armazenadas de forma apropriada."""
        for response in self.responses:
            self.my_survey.store_response(response)
            
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


unittest.main()
        