import sys
import pygame


def check_events(ship):
    """Responde a eventos de pressionamentos de teclas e de mouse"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # Move a espaçonave para a direita
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            # Move a espaçonave para a esquerda
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
            
            

def update_screen(ai_settings, screen, ship):
    """Atualiza as imagens na tela e alterna para a nova tela.
    
    Args:
        ai_settings: Configurações do jogo
        screen: Janela do jogo
        ship: Nave principal
    """
    # Redesenha a tela a cada passagem pelo laço
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    
    # Deixa a tela mais recente visível
    pygame.display.flip()

