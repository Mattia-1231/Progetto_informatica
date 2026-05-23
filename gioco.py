#commit1
import pygame
import random
import math

# =========================================================
# INIT
# =========================================================

pygame.init()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arena Survival Ultimate")

clock = pygame.time.Clock()

# =========================================================
# FONT
# =========================================================

font = pygame.font.SysFont("consolas", 24)
big_font = pygame.font.SysFont("consolas", 60)

# =========================================================
# COLORI
# =========================================================

BLACK = (15, 15, 20)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
RED = (255, 60, 60)
GREEN = (0, 255, 100)
YELLOW = (255, 255, 0)
ORANGE = (255, 150, 0)
GRAY = (100, 100, 100)
DARK = (40, 40, 40)
# =========================================================
# MAPPA
# =========================================================

walls = [
    pygame.Rect(400, 100, 400, 30),
    pygame.Rect(250, 250, 30, 300),
    pygame.Rect(1000, 200, 30, 350),
    pygame.Rect(450, 550, 500, 30),
]

# =========================================================
# PLAYER
# =========================================================

player = {
    "x": WIDTH // 2,
    "y": HEIGHT // 2,
    "radius": 18,
    "speed": 5,
    "hp": 100,
    "max_hp": 100,
    "angle": 0,
    "freeze": 0,
    "healing": 0,
    "dash": 0,
    "score": 0
}
# =========================================================
# ENTITA'
# =========================================================

enemies = []
bullets = []
particles = []

# =========================================================
# FUNZIONI
# =========================================================

def dist(x1, y1, x2, y2):
    return math.hypot(x2 - x1, y2 - y1)

def wall_collision(x, y, radius=15):

    rect = pygame.Rect(
        x - radius,
        y - radius,
        radius * 2,
        radius * 2
    )

    for wall in walls:
        if rect.colliderect(wall):
            return True

    return False
# =========================================================
# PARTICELLE
# =========================================================

def create_particles(x, y, color):

    for _ in range(10):

        particles.append({
            "x": x,
            "y": y,
            "dx": random.uniform(-3, 3),
            "dy": random.uniform(-3, 3),
            "life": 25,
            "color": color
        })

# =========================================================
# ENEMY SPAWN
# =========================================================

def spawn_enemy():

    while True:

        x = random.randint(50, WIDTH - 50)
        y = random.randint(50, HEIGHT - 50)

        if dist(x, y, player["x"], player["y"]) > 250:
            if not wall_collision(x, y):
                break

    enemy_type = random.choice(["normal", "fast", "tank"])

    if enemy_type == "normal":

        hp = 40
        speed = 2
        radius = 14
        color = RED

    elif enemy_type == "fast":

        hp = 20
        speed = 4
        radius = 10
        color = YELLOW

    else:

        hp = 100
        speed = 1
        radius = 22
        color = ORANGE

    enemies.append({
        "x": x,
        "y": y,
        "hp": hp,
        "speed": speed,
        "radius": radius,
        "color": color
    })
# =========================================================
# SHOOT
# =========================================================

def shoot():

    rad = math.radians(player["angle"])

    bullets.append({
        "x": player["x"],
        "y": player["y"],
        "dx": math.cos(rad) * 15,
        "dy": math.sin(rad) * 15,
        "damage": 20,
        "life": 60
    })

# =========================================================
# ABILITA'
# =========================================================

def melee_attack():

    for e in enemies:

        if dist(player["x"], player["y"], e["x"], e["y"]) < 80:

            e["hp"] -= 25
            create_particles(e["x"], e["y"], WHITE)

def strong_attack():

    for e in enemies:

        if dist(player["x"], player["y"], e["x"], e["y"]) < 140:

            e["hp"] -= 50
            create_particles(e["x"], e["y"], ORANGE)

def freeze():

    player["freeze"] = 240

def heal():

    player["healing"] = 300

def dash():

    player["dash"] = 10
# =========================================================
# LOOP
# =========================================================

running = True
spawn_timer = 0

while running:

    dt = clock.tick(60)

    # =====================================================
    # EVENTI
    # =====================================================

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_z:
                shoot()

            if event.key == pygame.K_SPACE:
                melee_attack()

            if event.key == pygame.K_q:
                strong_attack()

            if event.key == pygame.K_f:
                freeze()

            if event.key == pygame.K_e:
                heal()

            if event.key == pygame.K_LSHIFT:
                dash()
  # =====================================================
    # INPUT
    # =====================================================

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        player["angle"] += 4

    if keys[pygame.K_d]:
        player["angle"] -= 4

    speed = player["speed"]

    if player["dash"] > 0:
        speed = 12
        player["dash"] -= 1

    rad = math.radians(player["angle"])

    move_x = 0
    move_y = 0

    if keys[pygame.K_w]:

        move_x += math.cos(rad) * speed
        move_y += math.sin(rad) * speed

    if keys[pygame.K_s]:

        move_x -= math.cos(rad) * speed
        move_y -= math.sin(rad) * speed

    nx = player["x"] + move_x
    ny = player["y"] + move_y

    if not wall_collision(nx, player["y"], player["radius"]):
        player["x"] = nx

    if not wall_collision(player["x"], ny, player["radius"]):
        player["y"] = ny

    # =====================================================
    # SPAWN
    # =====================================================

    spawn_timer += 1

    if spawn_timer > 30:

        spawn_enemy()
        spawn_timer = 0
