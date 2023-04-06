import pygame
pygame.init()

x = 1280
y = 720
#tela
screen = pygame.display.set_mode((x,y))
pygame.display.set_caption("Meu Primeiro Jogo")

#background
bg = pygame.image.load('IMAGENS/deserto.jpg').convert_alpha()
bg = pygame.transform.scale(bg, (x,y))
#personagens
guereirro = pygame.image.load('IMAGENS/persona.png').convert_alpha()
guereirro = pygame.transform.scale(guereirro, (140,100))

p1 = pygame.image.load('IMAGENS/ninja.png').convert_alpha()
p1 = pygame.transform.scale(p1, (110,100))
#localização personagens
pos_guerreiro_x = 500
pos_guerreiro_y = 360

pos_p1_x = 200
pos_p1_y = 300


#iniciar jogo
rodando = True

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    screen.blit(bg, (0,0))

    rel_x = x % bg.get_rect().width
    screen.blit(bg, (rel_x - bg.get_rect().width,0))
    if rel_x < 1280:
        screen.blit(bg, (rel_x, 0))



        #teclas

    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP] and pos_p1_y > 500:
        pos_p1_y  -=1
    if tecla[pygame.K_DOWN] and pos_p1_y < 600:
            pos_p1_y += 1




        #movimento tela
    x-=1
#criar imagens
    screen.blit(guereirro, (pos_guerreiro_x, pos_guerreiro_y))
    screen.blit(p1, (pos_p1_x, pos_p1_y))
    pygame.display.update()