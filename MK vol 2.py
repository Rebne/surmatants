import pygame
from player import Player

print(Player)

pygame.init()

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 640
play = True

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("MK vol 2")

player1 = Player(270, 400)
player2 = Player(810, 400)


bg_image = pygame.image.load("test.jpg").convert_alpha()

#Making the game run uniformly on 60FPS
clock = pygame.time.Clock()
FPS = 60

#Background image function
def bg():
    screen.blit(bg_image, (0,0))
    
    
#Game loop
while play == True:
    
    #Makes this loop run 60FPS
    clock.tick(FPS)
    
    #Displays the background image
    bg()
    
    #Move fighter
    player1.move("left" ,SCREEN_WIDTH, SCREEN_HEIGHT, screen)
    player2.move("right" ,SCREEN_WIDTH, SCREEN_HEIGHT, screen)
    
    #Draw the fighters on the screen
    player1.draw(screen)
    player2.draw(screen)
    
    #Closing the program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
         
    #Updating the screen
    pygame.display.update()
            

#exit game
pygame.quit()