import random
import pygame
pygame.init()

x = 1280
y = 720

#tela
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption("Meu Primeiro Jogo")

#background
bg = pygame.image.load('IMAGENS/deserto.jpg').convert_alpha()
bg = pygame.transform.scale(bg, (x, y))

#personagens
guereirro = pygame.image.load('IMAGENS/persona.png').convert_alpha()
guereirro = pygame.transform.scale(guereirro, (80, 60))

p1 = pygame.image.load('IMAGENS/ninja.png').convert_alpha()
p1 = pygame.transform.scale(p1, (110, 100))

#Itens
shuriken = pygame.image.load('IMAGENS/shuriken.png').convert_alpha()
shuriken = pygame.transform.scale(shuriken, (30,30))

#localização personagens e acessorios
pos_guerreiro_x = 1000
pos_guerreiro_y = 550

pos_p1_x = 50
pos_p1_y = 590

vel_shuriken_x = 0
pos_shuriken_x = 50
pos_shuriken_y = 590

pontos = 10


#iniciar jogo

lanca = False

rodando = True

font = pygame.font.SysFont('Fontes/fonte.ttf', 50)

p1_rect = p1.get_rect()
guereirro_rect = guereirro.get_rect()
shuriken_rect = shuriken.get_rect()


#funções
def respawn():
    x = 1350
    y = random.randint(500, 640)
    return [x, y]

def respawn_shuriken():
    lanca = False
    respawn_shuriken_x = pos_p1_x
    respawn_shuriken_y = pos_p1_y
    vel_shuriken_x = 0
    return [respawn_shuriken_x, respawn_shuriken_y, lanca, vel_shuriken_x]

def colisions():
    global pontos
    if p1_rect.colliderect(guereirro_rect) or guereirro_rect.x == 60:
        pontos -= 1
        return True
    elif shuriken_rect.colliderect(guereirro_rect):
        pontos +=1
        return True
    else:
        return  False


while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    screen.blit(bg, (0, 0))

    rel_x = x % bg.get_rect().width
    screen.blit(bg, (rel_x - bg.get_rect().width, 0))
    if rel_x < 1280:
        screen.blit(bg, (rel_x, 0))

#teclas

    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP] and pos_p1_y > 500:
        pos_p1_y -= 1
        if not lanca:
            pos_shuriken_y -=1


    if tecla[pygame.K_DOWN] and pos_p1_y < 600:
        pos_p1_y += 1
        if not lanca:
            pos_shuriken_y += 1


    if tecla[pygame.K_x]:
        lanca = True
        vel_shuriken_x = 2


    if pontos == -1:
        rodando = False
#Respawn
    if pos_guerreiro_x == 50:
       pos_guerreiro_x = respawn()[0]
       pos_guerreiro_y = respawn()[1]

    if pos_shuriken_x == 1300:
        pos_shuriken_x, pos_shuriken_y, lanca, vel_shuriken_x = respawn_shuriken()

    if pos_guerreiro_x == 50 or colisions():
        pos_guerreiro_x = respawn()[0]
        pos_guerreiro_y = respawn()[1]


#Posição rect

    p1_rect.y = pos_p1_y
    p1_rect.x = pos_p1_x

    shuriken_rect.y = pos_shuriken_y
    shuriken_rect.x = pos_shuriken_x

    guereirro_rect.y = pos_guerreiro_y
    guereirro_rect.x = pos_guerreiro_x


#movimento tela
    x -= 1
    pos_guerreiro_x -= 4
    pos_shuriken_x += vel_shuriken_x

    score = font.render(f'Pontos: {int(pontos)} ', True, (0,0,0))
    screen.blit(score, (50, 50))

#criar imagens
    screen.blit(guereirro, (pos_guerreiro_x, pos_guerreiro_y))
    screen.blit(p1, (pos_p1_x, pos_p1_y))
    screen.blit(shuriken, (pos_shuriken_x, pos_shuriken_y))

#marcações
    pygame.draw.rect(screen, (255, 0, 0), p1_rect, 4)
    pygame.draw.rect(screen, (255, 0, 0), shuriken_rect, 4)
    pygame.draw.rect(screen, (255, 0, 0), guereirro_rect, 4)

    print(pontos)

    pygame.display.update()

