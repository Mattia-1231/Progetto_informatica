#primo commit
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

#mappa secondo commit

WHITE = (255, 255, 255)
GRAY = (100, 100, 100)

walls = [
    pygame.Rect(400, 100, 400, 30),
    pygame.Rect(250, 250, 30, 300),
    pygame.Rect(1000, 200, 30, 350),
    pygame.Rect(450, 550, 500, 30),
]


pygame.draw.rect(
    screen,
    WHITE,
    (40, 40, WIDTH - 80, HEIGHT - 80),
    4
)

for wall in walls: 
	pygame.draw.rect(screen, GRAY, wall)

#COLORI TERZO COMMIT

CYAN = (0, 255, 255)

# PLAYER

player = {
   "x": WIDTH // 2,
   "y": HEIGHT // 2,
   "radius": 18,
   "speed": 5,
   "hp": 100,
   "angle": 0
}
# AGGIUNGI NEL DRAW

pygame.draw.circle(
   screen,
   CYAN,
   (int(player["x"]), int(player["y"])),
   player["radius"]
)
# AGGIUNGI IMPORT

import math
# AGGIUNGI NEL LOOP

keys = pygame.key.get_pressed()

if keys[pygame.K_a]:
   player["angle"] += 4

if keys[pygame.K_d]:
   player["angle"] -= 4

rad = math.radians(player["angle"])

if keys[pygame.K_w]:

   player["x"] += math.cos(rad) * player["speed"]
   player["y"] += math.sin(rad) * player["speed"]

if keys[pygame.K_s]:

   player["x"] -= math.cos(rad) * player["speed"]
   player["y"] -= math.sin(rad) * player["speed"]
# AGGIUNGI NEL DRAW

end_x = player["x"] + math.cos(rad) * 35
end_y = player["y"] + math.sin(rad) * 35

pygame.draw.line(
   screen,
   WHITE,
   (player["x"], player["y"]),
   (end_x, end_y),
   4
)



