import pygame


class Ship():
    """Modelo de nave
    
    Methods:
        __init__: Inicializa a espaçonave e define sua posição inicial.
        blitme: Desenha a espaçonave em sua posição inicial
    """
    
    def __init__(self, screen, ai_settings) -> None:
        """Inicializa a espaçonave e define sua posição inicial.
        
        Args:
            screen: Tela em que será desenhada a espaçonave
            ai_settings: Configurações do jogo
        """
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # Carrega a imagem da espaçonave e obtém seu rect (retângulo)
        self.image = pygame.image.load(("images/ship.bmp"))
        self.rect = self.image.get_rect()
        
        # Inicia cada nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # Armazena um valor decimal para o centro da espaçonave
        self.center = float(self.rect.centerx)
        
        # Flag de movimento
        self.moving_right = False
        self.moving_left = False
    
    def update_position(self):
        """Atualiza a posição da espaçonave de acordo com a flag de 
        movimento"""
        # Atualiza o valor do centra da espaçonave, e não o retângulo
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            
        # Atualiza o objeto react de acordo com self.center
        self.rect.centerx = self.center
    
        
    def blitme(self):
        """Desenha a espaçonave em sua posição inicial"""
        self.screen.blit(self.image, self.rect)
        
    