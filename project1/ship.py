import pygame


class Ship():
    """Modelo de nave
    
    Methods:
        __init__: Inicializa a espaçonave e define sua posição inicial.
        blitme: Desenha a espaçonave em sua posição inicial
    """
    
    def __init__(self, screen) -> None:
        """Inicializa a espaçonave e define sua posição inicial.
        
        Args:
            screen: Tela em que será desenhada a espaçonave
        """
        self.screen = screen   
        
        # Carrega a imagem da espaçonave e obtém seu rect (retângulo)
        self.image = pygame.image.load(("images/ship.bmp"))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Inicia cada nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    
    def blitme(self):
        """Desenha a espaçonave em sua posição inicial"""
        self.screen.blit(self.image, self.rect)
        
    