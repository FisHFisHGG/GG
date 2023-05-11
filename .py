import pygame
import random

# Inițializăm Pygame
pygame.init()

# Definim culorile
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Setăm dimensiunile ecranului jocului
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Setăm titlul jocului
pygame.display.set_caption("Farsky-like game")

# Cream ecranul jocului
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Definim variabilele de stare ale jucătorului
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2
player_speed = 5
player_size = 25

# Definim variabilele pentru resurse
resource_size = 20
resource_count = 25
resources = []
for i in range(resource_count):
    resource_x = random.randint(0, SCREEN_WIDTH - resource_size)
    resource_y = random.randint(0, SCREEN_HEIGHT - resource_size)
    resources.append(pygame.Rect(resource_x, resource_y, resource_size, resource_size))

# Definim variabilele pentru construcții
buildings = []

# Bucla principala a jocului
running = True
while running:
    # Citim toate evenimentele generate de jucător
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Citim tastele apăsate de jucător
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Verificăm dacă jucătorul a ieșit din ecran
    if player_x < 0:
        player_x = 0
    elif player_x > SCREEN_WIDTH - player_size:
        player_x = SCREEN_WIDTH - player_size
    if player_y < 0:
        player_y = 0
    elif player_y > SCREEN_HEIGHT - player_size:
        player_y = SCREEN_HEIGHT - player_size

    # Verificăm dacă jucătorul a colectat o resursă
    for resource in resources:
        if pygame.Rect(player_x, player_y, player_size, player_size).colliderect(resource):
            resources.remove(resource)
            # Adăugăm o construcție
            building_x = random.randint(0, SCREEN_WIDTH - player_size)
            building_y = random.randint(0, SCREEN_HEIGHT - player_size)
            buildings.append(pygame.Rect(building_x, building_y, player_size, player_size))

    # Ștergem ecranul și redesenăm jucătorul și resursele
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, [player_x, player_y, player_size, player_size])
    for resource in resources:
        pygame.draw.rect(screen, BLUE, resource)

    # Redesenăm construcțiile
    for building in buildings:
        pygame.draw.rect(screen, WHITE, building)

    # Actualizăm ecranul
    pygame.display.update()

# Oprim
