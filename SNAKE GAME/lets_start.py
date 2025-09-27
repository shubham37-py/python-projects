import pygame
import random

pygame.init()

height = 600
width = 800

screen = pygame.display.set_mode((width,height))

pygame.display.set_caption(("Snake Game 🐍"))

black = (0, 0, 0)
GREEN = (222, 144, 17)
RED = (255, 0, 0)

snake_block = 10
snake=[(100, 100), (90, 100), (80, 100)]
direction = "RIGHT"
food_x = random.randint(0, (width - snake_block) // snake_block) * snake_block
food_y = random.randint(0, (height - snake_block) // snake_block) * snake_block
food_position = (food_x, food_y)

clock = pygame.time.Clock()

running = True
while running :
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction !="LEFT":
                direction = "RIGHT"
            elif event.key == pygame.K_UP and direction !="DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction !="UP":
                direction = "DOWN" 

    head_x,head_y = snake[0]
    if direction == "RIGHT":
        head_x += snake_block 
    elif direction == "LEFT":
        head_x -= snake_block 
    elif direction == "UP":
        head_y -= snake_block
    elif direction == "DOWN":
        head_y += snake_block

    

    snake.insert(0,(head_x, head_y))

    if head_x < 0 or head_x >= width or head_y < 0 or head_y >= height:
        running = False


    if snake[0] == food_position:
        food_x = random.randint(0, (width - snake_block) // snake_block) * snake_block
        food_y = random.randint(0, (height - snake_block) // snake_block) * snake_block
        food_position = (food_x, food_y)
    else:
        snake.pop()


    for block in snake:
        pygame.draw.rect(screen, GREEN, (block[0], block[1], snake_block, snake_block))
        pygame.draw.rect(screen, RED, (food_position[0], food_position[1], snake_block, snake_block))

    pygame.display.update()        
    clock.tick(len(snake)*2)
    # clock.tick(50)

font = pygame.font.SysFont(None, 55)
fo= pygame.font.SysFont(None, 40)
game_over_surface = font.render('GAME OVER ', True, RED)
game_over_surf = fo.render(f'YOUR SCORE : {len(snake)*10-30} ', True, RED)

screen.blit(game_over_surface, (width // 2 - 100, height // 2 - 30))
screen.blit(game_over_surf, (width // 2 - 100, height // 2 + 30))
pygame.display.update()
pygame.time.wait(3000)  

pygame.quit()