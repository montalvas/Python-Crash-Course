class AnonymousSurvey():
    """Coleta respostas anônimas para uma pergunta de pesquisa.
    
    Methods:
    __init__, show_question, store_response, show_results
    """
    
    def __init__(self, question) -> None:
        """Armazena uma pergunte e se preparar para armazenar as respostas

        Args:
            question (str): Pergunta da pesquisa
        Self:
            responses (list): Lista das respostas
        """
        self.question = question
        self.responses = []
        
    def show_question(self):
        """Mostra a pergunta da pesquisa."""
        print(self.question)
    
    def store_response(self, new_response):
        """Armazena uma única resposta da pesquisa.
        
        Args:
            new_response (str): Nova resposta
        """
        self.responses.append(new_response)
    
    def show_results(self):
        """Mostra todas as respostas dadas."""
        print("\nSurvey results:")
        for response in self.responses:
            print(f'\t{response}')