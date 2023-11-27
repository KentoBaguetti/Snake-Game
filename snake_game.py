import pygame
import random
pygame.init()

font_style = pygame.font.SysFont(None, 26)

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
# Initializing the Screen
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# Message function to display messages in the game window
def message(msg, colour, x_loc, y_loc):
    screen_msg = font_style.render(msg, True, colour)
    screen.blit(screen_msg, (x_loc, y_loc))
    
def score_counter(score):
    value = font_style.render("Your score: " + str(score), True, (255,0,0))
    screen.blit(value, [0,0])
    
# create the game clock
clock = pygame.time.Clock()

# snake size
snake_block = 10

# the snake
def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, (0,0,0), [x[0], x[1], snake_block, snake_block])


def game_loop(): # game loop
    
    
    # coordinates for the snake, will be updated throughout the gameloop to display the snakes location
    snake_x = SCREEN_WIDTH//2
    snake_y = SCREEN_HEIGHT/2

    # Direction of the snake, its speed in x and y
    delta_x = 10
    delta_y = 0
    
    # snake parameters
    snake_list = []
    snake_length = 1

    # food
    food_x = round(random.randrange(0, SCREEN_WIDTH - snake_block)/10)*10
    food_y = round(random.randrange(0, SCREEN_HEIGHT - snake_block)/10)*10

    # Game loop
    snake_into_self = False
    game_over = False
    while not game_over:
        
        # makes sure the snake stays on screen (boundies). Quits the game if it does
        if snake_x==0 or snake_x==SCREEN_WIDTH or snake_y==0 or snake_y == SCREEN_HEIGHT or snake_into_self:
            game_over = True
            user_selection = False
            while not user_selection:
                message("You lost! Press \"Q\" or \"esc\" to exit or \"enter\" to try again!", (255,0,0), SCREEN_WIDTH-500, SCREEN_HEIGHT//2) # displays end message for the user
                pygame.display.update()
                for event in pygame.event.get(): 
                    if event.type == pygame.QUIT:
                        user_selection = True
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            user_selection = True
                        elif event.key == pygame.K_ESCAPE:
                            user_selection = True
                        elif event.key == pygame.K_RETURN: # allows the user to restart
                            game_loop()
                     
        # user input to dicate the direction of the snake   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over = True
                elif event.key == pygame.K_UP:
                    delta_x = 0
                    delta_y = -10
                elif event.key == pygame.K_DOWN:
                    delta_x = 0
                    delta_y = 10
                elif event.key == pygame.K_LEFT:
                    delta_x = -10
                    delta_y = 0
                elif event.key == pygame.K_RIGHT:
                    delta_x = 10
                    delta_y = 0
        
        
        
        # the position of the snake everytime the display updates
        snake_x += delta_x
        snake_y += delta_y
        
        screen.fill((255,255,255))
        
        # Food objects
        pygame.draw.rect(screen, (255,0,0), [food_x, food_y, snake_block, snake_block])
        
        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_list.append(snake_head)
        
        if len(snake_list) > snake_length:
            del snake_list[0]
            
        for x in snake_list[:-1]:
            if x == snake_head:
                snake_into_self = True
         
        # the snake           
        snake(snake_block, snake_list)
        
        # score counter
        score_counter(snake_length-1)
        
        # update the display
        pygame.display.update()
        
        if snake_x == food_x and snake_y == food_y:
            food_x = round(random.randrange(0, SCREEN_WIDTH - snake_block)/10) * 10
            food_y = round(random.randrange(0, SCREEN_HEIGHT - snake_block)/10) * 10
            snake_length += 1
        
        
        
        clock.tick(15)
            
    pygame.quit()
    quit()
    
game_loop()
