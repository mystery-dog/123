import pygame
import random
import sys

pygame.init()

grid_size = 10
cell_size = 40
num_mines=10
screen_size = grid_size*cell_size
screen = pygame.display.set_mode((screen_size,screen_size))
pygame.display.set_caption("踩地雷")

whith=(255,255,255)
black=(0,0,0)
geay=(200,200,200)

grid = [[0 for _ in range(10)] for _ in range(10)]
revealed = [[False for _ in range(10)] for _ in range(10)]

for _ in range(num_mines):
    

print("iop")