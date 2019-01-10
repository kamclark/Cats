import pygame

black = (0,0,0)
white = (255,255,255)

pygame.init()

surface = pygame.display.set_mode((800,400))

pygame.display.set_caption('Birds')

clock = pygame.time.Clock()

def cat(x, y, image):
    surface.blit(img,(x,y))

img = pygame.image.load('cat.png')
x = 100
y = 100

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    surface.fill(black)
    cat(x, y, img)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
