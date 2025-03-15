import pygame, random, sys
from pygame.locals import *

WINDOWWIDTHANDHEIGHT = 500
BOXWIDTHANDHEIGHT = 10
FPS = 10

RED        =  (255,   0,   0)
BLUE       =  (  0,   0, 255)
GREEN      =  (  0, 255,   0)
BLACK      =  (  0,   0,   0)
WHITE      =  (255, 255, 255)

head_box = pygame.Rect(WINDOWWIDTHANDHEIGHT / 2, WINDOWWIDTHANDHEIGHT / 2, BOXWIDTHANDHEIGHT, BOXWIDTHANDHEIGHT)
snake = [ head_box ]
score = 0

move = "" 
def main():
       global move, snake, head_box, score

       pygame.init()
       FPSCLOCK = pygame.time.Clock()

       pygame.display.set_caption('Snake Game')
       font = pygame.font.Font( 'freesansbold.ttf', 15)
       DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTHANDHEIGHT, WINDOWWIDTHANDHEIGHT))
       DISPLAYSURF.fill(BLACK)
       
       #random food generation
       snake_positions = [(box.x, box.y) for box in snake]
       food_location = foodLocationAtRandom( snake_positions )
       food_box = pygame.Rect(food_location[0], food_location[1], BOXWIDTHANDHEIGHT, BOXWIDTHANDHEIGHT)
       
       
       while True:
            DISPLAYSURF.fill(BLACK)
            score_display = f'Score: {score}'
            TEXTSURF = font.render(score_display, True, (255,255,255))
            DISPLAYSURF.blit(TEXTSURF, (WINDOWWIDTHANDHEIGHT / 2 - 50, 0))

            for box in snake:
                pygame.draw.rect(DISPLAYSURF, RED, box)

            pygame.draw.rect(DISPLAYSURF, GREEN, food_box )
            
            #Boundary check
            if head_box.x in (-BOXWIDTHANDHEIGHT, WINDOWWIDTHANDHEIGHT) or head_box.y in (-BOXWIDTHANDHEIGHT, WINDOWWIDTHANDHEIGHT):
                print("GAME OVER | SCORE : ", score) 
                pygame.quit()
                sys.exit()
            
            #collision check to itself
            if head_box.collidelist(snake[1:]) != -1:
                print("GAME OVER | Self Destruction | SCORE : ", score)
                pygame.quit()
                sys.exit()


            #food collision
            if snake[0].colliderect(food_box):
                score += 1
                print("Score: ", score)
                snake.append(pygame.Rect(snake[-1].x, snake[-1].y, BOXWIDTHANDHEIGHT, BOXWIDTHANDHEIGHT))
                snake_positions[:] = [(box.x, box.y) for box in snake] #clears and updates the snake positions 
                food_location = foodLocationAtRandom(snake_positions)
                food_box.x  = food_location[0]
                food_box.y  = food_location[1]

            #update box positions on key press
            updateBoxPositionAfterKeyPress()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_UP and move != "DOWN":
                        move = "UP"
                    elif event.key == K_DOWN and move != "UP":
                        move = "DOWN"
                    elif event.key == K_LEFT and move != "RIGHT":
                        move = "LEFT"
                    elif event.key == K_RIGHT and move != "LEFT":
                        move = "RIGHT"       
            pygame.display.update()
            FPSCLOCK.tick(FPS)


def shiftSnakeBoxes():
    for i in range(len(snake) - 1, 0, -1):  
        snake[i] = snake[i - 1].copy()

def foodLocationAtRandom(snake_positions):

    while True:
        x = random.randrange(0, WINDOWWIDTHANDHEIGHT - BOXWIDTHANDHEIGHT + 1, BOXWIDTHANDHEIGHT)
        y = random.randrange(0, WINDOWWIDTHANDHEIGHT - BOXWIDTHANDHEIGHT + 1, BOXWIDTHANDHEIGHT)

        if (x, y) not in snake_positions:
            return (x, y)
        
def updateBoxPositionAfterKeyPress():

    if move == "DOWN":
        shiftSnakeBoxes()  # Shifts the boxes of the snake one position (10 pixels) to the right
        snake[0].y += BOXWIDTHANDHEIGHT
    elif move == "UP":
        shiftSnakeBoxes()
        snake[0].y -= BOXWIDTHANDHEIGHT
    elif move == "LEFT":
        shiftSnakeBoxes()
        snake[0].x -= BOXWIDTHANDHEIGHT
    elif move == "RIGHT":
        shiftSnakeBoxes()
        snake[0].x += BOXWIDTHANDHEIGHT

if __name__ == '__main__':
    main() 
