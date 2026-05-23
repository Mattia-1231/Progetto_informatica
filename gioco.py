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
