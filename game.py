import pygame
import random
import numpy as np

green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

DISPLAY_W, DISPLAY_H = 700, 500

GRID_SIZE = 20


snake_w, snake_h = 10, 10
food_w, food_h = 8, 8


pygame.init()
clock = pygame.time.Clock()

display = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
pygame.display.update()
pygame.display.set_caption('Snake')

size_x = DISPLAY_W//snake_w

snake_head = [200, 100]

snake = [snake_head]

food = [random.randrange(1, (DISPLAY_W//10)) * 10, random.randrange(1, (DISPLAY_H//10)) * 10]

UP = [0, -10]
DOWN = [0, 10]
RIGHT = [10, 0]
LEFT = [-10, 0]

next_loc = RIGHT

score = 0

running = True
while running:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == ord('w'):
                if not next_loc == DOWN:
                    next_loc = UP
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                if not next_loc == UP:
                    next_loc = DOWN
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                if not next_loc == RIGHT:
                    next_loc = LEFT
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                if not next_loc == LEFT:
                    next_loc = RIGHT
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    if snake_head[0] == food[0] and snake_head[1] == food[1]:
        score += 1
        food = [random.randrange(1, (DISPLAY_W // 10)) * 10, random.randrange(1, (DISPLAY_H // 10)) * 10]
    else:
        snake.pop()
    display.fill(black)
    snake_head[0] += next_loc[0]
    snake_head[1] += next_loc[1]
    for part in snake:
        if snake_head[0] == part[0] and snake_head[1] == part[1]:
            running = False
    snake.insert(0, list(snake_head))
    for part in snake:
        pygame.draw.rect(display, green, pygame.Rect(part[0], part[1], snake_w, snake_h))

    if not 0 <= snake_head[0] < DISPLAY_W:
        running = False
    if not 0 <= snake_head[1] < DISPLAY_H:
        running = False

    pygame.draw.rect(display, red, pygame.Rect(food[0], food[1], 10, 10))
    pygame.display.update()

pygame.quit()
quit()
