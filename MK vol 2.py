import pygame
# from player import *

class player():
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y, 80, 180))
        
    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 255), self.rect)
#         print("Here")
    def move(self):
        SPEED = 10
        dx = 0
        dy = 0
        
        key = pygame.key.get_pressed()
        
        if key[pygame.K_a]:
            dx = -SPEED
        if key[pygame.K_d]:
            dx = SPEED
            
        self.rect.x += dx
        
        
print(player)

pygame.init()

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 640
play = True

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("MK vol 2")

player1 = player(270, 400)
player2 = player(810, 400)


bg_image = pygame.image.load("test.jpg").convert_alpha()

clock = pygame.time.Clock()
FPS = 60

def bg():
    screen.blit(bg_image, (0,0))
    
    
#Game loop
while play == True:
    
    clock.tick(FPS)
    
    bg()
    
    #Move fighter
    player1.move()
    player2.move()
    
    #Draw the fighters on the screen
    player1.draw(screen)
    player2.draw(screen)
    
    #Closing the program
    for event in pygame.event.get():
#         print(event)
        if event.type == pygame.QUIT:
            play = False
         
    #Updating the screen
    pygame.display.update()
            

#exit game
pygame.quit()