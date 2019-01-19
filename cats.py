import pygame, time, os
from random import randint

pygame.init()

black = (0,0,0)
white = (255,255,255)
grey = (211,211,211)
red = (255,5,5)
purple = (238,130,238)
screenWidth = 800
screenHeight = 450
screen = pygame.display.set_mode((screenWidth, screenHeight)) #display is 800 by 450 pixel window
pygame.display.set_caption('Cats') # caption refers to title of displayed window

fps = 120

characterHeight = 45
characterWidth = 58

clock = pygame.time.Clock()
img = pygame.image.load('cat.png') # only loading image one time doing this as opposed to repeatedly loading everytime function is called

def gameOver():
    alertSurface('X_X')

def blocks(x_block, y_block, blockWidth, blockHeight, gap):
    pygame.draw.rect(screen, purple, [x_block, y_block, blockWidth, blockHeight]) #draw purple rectangle to surface
    pygame.draw.rect(screen, purple, [x_block, y_block + blockHeight + gap, blockWidth, screenHeight]) #draw purple rectangle to surface from bottom of screen including gap size

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
    titleTextRect.center = screenWidth/2, screenHeight/2
    screen.blit(titleTextSurf, titleTextRect)

    regTextSurf, regTextRect = makeTextObjs('press any key to continue', smallText)
    regTextRect.center = screenWidth/2, ((screenHeight/2) + 100)
    screen.blit(regTextSurf, regTextRect)

    pygame.display.update()
    time.sleep(2)

    while replay_or_quit() == None:
        clock.tick()

    main()


def cat(x, y, image): # takes an x and y coordinate and image to be loaded
    screen.blit(img,(x,y)) #blit updates an image onto display/surface

def main():
    x = 100
    y = 200
    characterYMove = 3

    x_block = screenWidth
    y_block = 0
    blockWidth = 60
    blockHeight = randint(0,screenHeight)
    gap = characterHeight * 2.5
    blockMove = 4

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN: #if keydown, keyboard up arrow detected, move character up
                if event.key == pygame.K_UP:
                    characterYMove = -2

            if event.type == pygame.KEYUP: #if keyboard up arrow detected up/depressed, move character down
                if event.key == pygame.K_UP:
                    characterYMove = 2

        y = y + characterYMove #update y based on pressed movement
        screen.fill(grey) #black background
        cat(x, y, img)

        blocks(x_block, y_block, blockWidth, blockHeight, gap)
        x_block = (x_block - blockMove) # update block position

        if y > (screenHeight - characterHeight) or y < 0: #window collision detection for game over
            gameOver()

        if x_block < (-1*blockWidth): # keep making random blocks every time they leave window
            x_block = screenWidth
            blockHeight = randint(0,(screenHeight / 2))

        if x + characterWidth > x_block:
            if x < x_block + blockWidth:
                print('within UPPER bound of x')
                if y < blockHeight:
                    print('within UPPER bound of x and UPPER bound of y')
                    if x - characterWidth < blockWidth + x_block:
                        print('game over UPPER bound hit')
                        gameOver()

        if x + characterWidth > x_block:
            if y + characterHeight > blockHeight + gap:
                print('within LOWER bound of y')

                if x < blockWidth + x_block:
                    print('game over LOWER bound hit')
                    gameOver()


        pygame.display.update()
        clock.tick(fps) #runs this main loop 60(fps) times a second
main()

pygame.quit()
quit()
