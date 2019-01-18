import pygame
import time
from random import randint

pygame.init()

black = (0,0,0)
white = (255,255,255)
red = (255,5,5)
purple = (238,130,238)

fps = 120

surfaceWidth = 800
surfaceHeight = 450

characterHeight = 45
characterWidth = 58

surface = pygame.display.set_mode((surfaceWidth, surfaceHeight)) #display is 800 by 450 pixel window
pygame.display.set_caption('Cats')
clock = pygame.time.Clock()
img = pygame.image.load('cat.png')

def gameOver():
    alertSurface('X_X')

def blocks(x_block, y_block, block_width, block_height, gap):
    pygame.draw.rect(surface, purple, [x_block, y_block, block_width, block_height])
    pygame.draw.rect(surface, purple, [x_block, y_block + block_height + gap, block_width, surfaceHeight])
    
def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN,pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type== pygame.KEYDOWN:
            continue

        return event.key
    
    return None
    
def makeTextObjs(text, font):
    alertSurface=font.render(text, True, red)
    return alertSurface, alertSurface.get_rect()

def alertSurface(text):
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    largeText = pygame.font.Font('freesansbold.ttf', 120)

    titleTextSurf, titleTextRect = makeTextObjs(text, largeText)
    titleTextRect.center = surfaceWidth/2, surfaceHeight/2
    surface.blit(titleTextSurf, titleTextRect)

    regTextSurf, regTextRect = makeTextObjs('press any key to continue', smallText)
    regTextRect.center = surfaceWidth/2, ((surfaceHeight/2) + 100)
    surface.blit(regTextSurf, regTextRect)

    pygame.display.update()
    time.sleep(2)

    while replay_or_quit() == None:
        clock.tick()

    main()
    

def cat(x, y, image):
    surface.blit(img,(x,y))

def main():
    x = 100
    y = 200
    y_move = 3
    
    x_block = surfaceWidth
    y_block = 0
    block_width = 60
    block_height = randint(0,surfaceHeight)
    gap = characterHeight * 3
    block_move = 5
    
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -2

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_move = 2    

        y = y + y_move
        surface.fill(black)
        cat(x, y, img)

        blocks(x_block, y_block, block_width, block_height, gap)
        x_block = (x_block - block_move)

        if y > (surfaceHeight - characterHeight) or y < 0:
            gameOver()

        if x_block < (-1*block_width):
            x_block = surfaceWidth
            block_height = randint(0,(surfaceHeight / 2))

        if x + characterWidth > x_block:
            if x < x_block + block_width:
                print('within upper bound of x')
                if y < block_height:
                    print('within upper bound of x and upper bound of x')
                    if x - characterWidth < block_width + x_block:
                        print('game over UPPER')
                        gameOver()
                        
        if x + characterWidth > x_block:
            if y + characterHeight > block_height + gap:
                print('y bound lower')

                if x < block_width + x_block:
                    print('game over LOWER')
                    gameOver()
                
                        
        pygame.display.update()
        clock.tick(fps)
main()
pygame.quit()
quit()
