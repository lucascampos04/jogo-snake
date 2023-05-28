import pygame
from pygame.locals import *
import random

window = (600, 600)
pixel_size = 10

# maça sendo spawnada aleatoriamente
def random_apple():
    x = random.randint(0, window[0])
    y = random.randint(0, window[1])
    return x // pixel_size * pixel_size, y // pixel_size * pixel_size
 
# funções de colisão 
def coli(pos1, pos2):
    return pos1 == pos2

def off_coli(pos):
    if 0 <= pos[0] < window[0] and 0 <= pos[1] < window[1]:
        return False
    else:
        return True

def restart_game():
    global snake_pos
    global apple_pos
    global snake_direction
    snake_direction = K_LEFT
    apple_pos = random_apple()
    snake_pos = [(250, 50), (260, 50), (270, 50)]


pygame.init()
screen = pygame.display.set_mode(window)
pygame.display.set_caption('Snake')


# cobrinha
snake_pos = [(250, 50), (260, 50), (270, 50)]
snake_surface = pygame.Surface((pixel_size, pixel_size))
snake_surface.fill((255, 255, 255))
snake_direction = K_LEFT

# maça que vai aparecer na tela
apple_surface = pygame.Surface((pixel_size, pixel_size))
apple_surface.fill((255, 0, 0))
apple_pos = random_apple()

while True:
    # Movimento da cobrinha na tela
    pygame.time.Clock().tick(15)
    screen.fill((0,0,0))
    # FECHANDO A JANELA
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            quit()

        elif event.type == KEYDOWN:
            if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                snake_direction = event.key



    # desenhando a maça na tela 
    screen.blit(apple_surface, apple_pos)

    if coli(apple_pos, snake_pos[0]):
        snake_pos.append((-10, -10))
        apple_pos = random_apple()

    # desenhando a cobrinha na tela
    for pos in snake_pos:
        screen.blit(snake_surface, pos)

    # fazendo o corpo acompanhar a cabeça da cobrinha
    for i in range(len(snake_pos) -1, 0, -1):
        if coli(snake_pos[0], snake_pos[i]):
            restart_game()
        snake_pos[i] = snake_pos[i-1]

    if off_coli(snake_pos[0]):
        restart_game()

    if snake_direction == K_UP:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] - pixel_size)

    if snake_direction == K_DOWN:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] + pixel_size)

    if snake_direction == K_LEFT:
        snake_pos[0] = (snake_pos[0][0] - pixel_size,  snake_pos[0][1] )

    if snake_direction == K_RIGHT:
        snake_pos[0] = (snake_pos[0][0] + pixel_size, snake_pos[0][1])


    pygame.display.update()