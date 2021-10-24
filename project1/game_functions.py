import sys
import pygame
from pygame.constants import KEYDOWN, KEYUP
from bullet import Bullet


def check_events(ai_settings, screen, ship, bullets):
    """Responde a eventos de pressionamentos de teclas e de mouse"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == KEYUP:
            check_keyup_events(event, ship)
        

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Responde a pressionamento de teclas"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Cria um novo projetil e o adiciona ao grupo de projeteis
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """Responde a solturas de tecla"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False    
            

def update_screen(ai_settings, screen, ship, bullets):
    """Atualiza as imagens na tela e alterna para a nova tela.
    
    Args:
        ai_settings: Configurações do jogo
        screen: Janela do jogo
        ship: Nave principal
    """
    # Redesenha a tela a cada passagem pelo laço
    screen.fill(ai_settings.bg_color)
    # Redesenha todos os projeteis atras da espaconave e dos alieniginas
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    
    # Deixa a tela mais recente visível
    pygame.display.flip()

