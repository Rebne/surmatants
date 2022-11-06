import pygame
from player import Player
import Button as B
import os

print(Player)

# pygame.init()

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 640

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("MK vol 2")

player1 = Player(270, 400)
player2 = Player(810, 400)


screen.fill("white")
bg_image = pygame.image.load(os.path.join("Assets","test.jpg")).convert_alpha()

#Making the game run uniformly on 60FPS
clock = pygame.time.Clock()
FPS = 60

#Background image function
def bg():
    screen.blit(bg_image, (0,0))


def main_menu():
    # Caption for the Menu page
    pygame.display.set_caption("Menu")
    run = True 
    # Images for the start and exit buttons (Test images in this case)
    start_img = pygame.image.load(os.path.join("Assets", "test_button.png")).convert_alpha()
    exit_img = pygame.image.load(os.path.join("Assets","test_button.png")).convert_alpha() 

    # Making use of the button class in Button.py and putting buttons to middle with methods middle_pos
    start_button = B.Button(100, 600/2-36, start_img, 0.5, "START")
    start_button.left_middle_pos()
    exit_button = B.Button(450, 600, exit_img, 0.5, "EXIT")
    exit_button.right_middle_pos()
    
    while run:
        pygame.display.update()
        screen.fill((255, 255, 255))
        # Drawing and using the buttons
        if start_button.draw(screen):
            print("START")
            main()
        if exit_button.draw(screen):
            print("EXIT")
            pygame.quit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # Checks for keys pressed and makes use of 'Q' for quitting the window
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_q]:
            run = False
    pygame.display.update()
  
def main():
    play = True
    pygame.display.set_caption("Mortal Kombat vol.2")
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
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_q]:
            play = False
            
        #Updating the screen
        pygame.display.update()

            

    #exit game
    pygame.quit()

if __name__=="__main__":
    main_menu()