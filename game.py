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

snake_head = np.array([200, 100])

snake = [snake_head]

food = np.array([random.randrange(1, (DISPLAY_W//10)) * 10, random.randrange(1, (DISPLAY_H//10)) * 10])

UP = [0, -10]
DOWN = [0, 10]
RIGHT = [10, 0]
LEFT = [-10, 0]

next_loc = RIGHT

score = 0

running = True
while running:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == ord('w'):
                next_loc = UP
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                next_loc = DOWN
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                next_loc = LEFT
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                next_loc = RIGHT
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    snake_head += next_loc
    print(snake_head)
    snake.insert(0, list(snake_head))

    if snake_head == food:
        score += 1
        food = [random.randrange(1, (DISPLAY_W // 10)) * 10, random.randrange(1, (DISPLAY_H // 10)) * 10]
    else:
        snake.pop()

    display.fill(black)
    for part in snake:
        pygame.draw.rect(display, green, pygame.Rect(part[0], part[1], snake_w, snake_h))

    pygame.draw.rect(display, red, pygame.Rect(food[0], food[1], 10, 10))
    print('reating')
    pygame.display.update()

pygame.quit()
quit()
