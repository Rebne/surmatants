import pygame
from player import Player
import Button as B
import os
import sys
from pygame import mixer

print(Player)

pygame.init()
mixer.init()

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 640

title_font= pygame.font.Font((os.path.join("Assets","Fonts","snowmelt.ttf")), 80)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player1 = Player(270, 400, SCREEN_WIDTH)
player2 = Player(810, 400, SCREEN_WIDTH)

bg_image = pygame.image.load(os.path.join("Assets","test.jpg")).convert_alpha()
bg_menu = pygame.image.load(os.path.join("Assets","white_rain.jpg")).convert_alpha()
#Making the game run uniformly on 60FPS
clock = pygame.time.Clock()
FPS = 60

#Background image function
# def bg():
#     screen.blit(bg_image, (0,0))

click_sound = mixer.Sound((os.path.join("Assets","sounds", "click.mp3")))
click_sound.set_volume(0.5)
thunder_sound = mixer.Sound((os.path.join("Assets","sounds", "thunder.mp3")))
thunder_sound.set_volume(0.6)

def main_menu():
    # Caption for the Menu page
    pygame.display.set_caption("Menu")
    mixer.music.load((os.path.join("Assets","sounds", "bg_storm.mp3")))
    mixer.music.play(-1)
    mixer.music.set_volume(0.5)

    # Loading of sound and setting volume


    run = True 
    # Images for the start and exit buttons (Test images in this case)
    start_img = pygame.image.load(os.path.join("Assets", "test_button.png")).convert_alpha()
    exit_img = pygame.image.load(os.path.join("Assets","test_button.png")).convert_alpha() 

    # Making use of the button class in Button.py and putting buttons to middle with methods middle_pos
    start_button = B.Button(SCREEN_WIDTH/2, 250, "", 0.5, "Alusta", False)

    exit_button = B.Button(SCREEN_WIDTH/2, 450, "", 0.5, "Sulge", False)
    level_button = B.Button(SCREEN_WIDTH/2, 350, start_img, 0.5, "Areen", False)
    
    # Title font stuff
    title = title_font.render("Surmatants", 1, (255,255,255))
    title_rect  = title.get_rect(center=(SCREEN_WIDTH/2, 100))

    
    while run:
        
        #screen.fill((0,0,0))
        screen.blit(bg_menu, (0,0))
        keys_pressed = pygame.key.get_pressed()
        # Drawing and using the buttons
        screen.blit(title, title_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if start_button.draw(screen):
            thunder_sound.play()
            mixer.music.fadeout(500)
            print("START")
            main()
            
        elif exit_button.draw(screen):
            run = False
            print("EXIT")
            pygame.quit()
            break
        elif level_button.draw(screen):
            click_sound.play()
            areen()

       # Checks for keys pressed and makes use of 'Q' for quitting the window
        elif keys_pressed[pygame.K_q]:
            run = False
            break
        pygame.display.update()
    pygame.quit()
    sys.exit()

def areen():
    global bg_image
    pygame.display.set_caption("Areen")
    run = True
    areen_sound = mixer.Sound((os.path.join("Assets","sounds", "areen_select2.wav")))
    areen_sound.set_volume(0.2)
    #Areenid images
    galaktika = pygame.image.load(os.path.join("Assets", "galaktika_resize.jpg")).convert_alpha()
    estcube = pygame.image.load(os.path.join("Assets", "estcube2.jpg")).convert_alpha()

    galaktika_button = B.Button(100, SCREEN_HEIGHT/2, galaktika, 0.25, "Galaktika", True )
    galaktika_button.arena_button()
    estcube_button = B.Button(500, SCREEN_HEIGHT/2, estcube, 0.25, "Galaktika", True )
    estcube_button.arena_button()
    tagasi_button = B.Button(SCREEN_WIDTH/2, 540, "", 0.5, "Tagasi", False)

    while run:
        screen.blit(bg_menu,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
        if galaktika_button.draw(screen):
            areen_sound.play()
            bg_image = galaktika
            main_menu()
            run = False
        elif estcube_button.draw(screen):
            areen_sound.play
            bg_image = estcube
            main_menu()
            run = False
        elif tagasi_button.draw(screen):
            click_sound.play()
            main_menu()
            run = False
        pygame.display.update()


  
def main():
    play = True
    pygame.display.set_caption("Surmatants")
    #Game loop
    while play == True:
        
        #Makes this loop run 60FPS
        clock.tick(FPS)
        
        #Displays the background image
        screen.blit(bg_image, (0,0))
        
        #Move fighter
        player1.move("left" ,SCREEN_WIDTH, SCREEN_HEIGHT, screen, player2)
        player2.move("right" ,SCREEN_WIDTH, SCREEN_HEIGHT, screen, player1)
        
        #Draw the fighters on the screen
        player1.draw(screen)
        player2.draw(screen)
        
        #Closing the program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
                break
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_q]:
            play = False
            break
            
        #Updating the screen
        pygame.display.update()

            

    #exit game
    pygame.quit()
    sys.exit()

if __name__=="__main__":
    main_menu()