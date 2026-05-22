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
