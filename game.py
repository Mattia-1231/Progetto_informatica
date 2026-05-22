
import pygame

pygame.init()

WIDTH, HEIGHT = 1280, 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arena Survival Ultimate")

clock = pygame.time.Clock()

running = True

while running:

    clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    screen.fill((15, 15, 20))

    pygame.display.flip()

pygame.quit()

#mappa

WHITE = (255, 255, 255)
GRAY = (100, 100, 100)

walls = [
   pygame.Rect(400, 100, 400, 30),
   pygame.Rect(250, 250, 30, 300),
   pygame.Rect(1000, 200, 30, 350),
   pygame.Rect(450, 550, 500, 30),
]
# AGGIUNGI NEL GAME LOOP

pygame.draw.rect(
   screen,
   WHITE,
   (40, 40, WIDTH - 80, HEIGHT - 80),
   4
)

for wall in walls: 
	pygame.draw.rect(screen, GRAY, wall)

