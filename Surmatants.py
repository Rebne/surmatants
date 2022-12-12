import pygame
from player import Player
from Button import *
import os
import sys
from pygame import mixer
import time

print(Player)

#Initializing
pygame.init()
mixer.init()

#Screen parameters
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 640

title_font= pygame.font.Font((os.path.join("Assets","Fonts","snowmelt.ttf")), 80)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player1 = Player(270, 400, SCREEN_WIDTH)
player2 = Player(810, 400, SCREEN_WIDTH)

bg_image = pygame.image.load(os.path.join("Assets","areen", "test.jpg")).convert_alpha()
bg_menu = pygame.image.load(os.path.join("Assets","white_rain.jpg")).convert_alpha()

#Loading animation sheets ...
catSheet = pygame.image.load(os.path.join("Assets","sprite_base.png")).convert_alpha()

#Animation data
animationSize = 64
catScale = 6
catOffset = [140,142]
catAnimationSteps = [4,8,8,10,9,7,6,8,13,10,12,6,8,8,8,6]
data = [catAnimationSteps, catSheet, animationSize, catScale, catOffset]
# data2 = 

#Making the game run uniformly on 60FPS
clock = pygame.time.Clock()
FPS = 60

#Background image function

click_sound = mixer.Sound((os.path.join("Assets","sounds", "click.mp3")))
click_sound.set_volume(0.5)
thunder_sound = mixer.Sound((os.path.join("Assets","sounds", "thunder.mp3")))
thunder_sound.set_volume(0.6)
sound = mixer.Sound((os.path.join("Assets","sounds", "sound.wav")))
sound.set_volume(0.6)

def main_menu():
    global current_time
    current_time = time.time()
    # Caption for the Menu page
    pygame.display.set_caption("Menu")
    mixer.music.load((os.path.join("Assets","sounds", "bg_storm.mp3")))
    mixer.music.play(-1)
    mixer.music.set_volume(0.5)


    run = True 

    # Making use of the button class in Button.py and putting buttons to middle with methods middle_pos
    start_button = Button(SCREEN_WIDTH/2, 250, 0.5, "Alusta")
    exit_button = Button(SCREEN_WIDTH/2, 450, 0.5, "Sulge")
    level_button = Button(SCREEN_WIDTH/2, 350, 0.5, "Areen")
    button = Button(1,1,1,"",)
    button.saladus()


    
    # Title font stuff
    title = title_font.render("Surmatants", 1, (255,255,255))
    title_rect  = title.get_rect(center=(SCREEN_WIDTH/2, 100))
    vajutuste_piiraja = 1
    while run:
        
        #screen.fill((0,0,0))
        screen.blit(bg_menu, (0,0))
        keys_pressed = pygame.key.get_pressed()
        # Drawing and using the buttons
        screen.blit(title, title_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if start_button.draw(screen) and time.time() - current_time > 0.1:
            thunder_sound.play()
            mixer.music.fadeout(500)
            print("START")
            main()
            
        elif exit_button.draw(screen) and time.time() - current_time > 0.1:
            run = False
            print("EXIT")
            pygame.quit()
            break
        elif level_button.draw(screen) and time.time() - current_time > 0.1:
            current_time = time.time()
            click_sound.play()
            areen()
        elif button.draw(screen) and time.time() - current_time > 0.1 and vajutuste_piiraja == 1:
            sound.play()
            vajutuste_piiraja = 0
       # Checks for keys pressed and makes use of 'Q' for quitting the window
        elif keys_pressed[pygame.K_q]:
            run = False
            break
        pygame.display.update()
    pygame.quit()
    sys.exit()

def areen():
    global bg_image, current_time
    pygame.display.set_caption("Areen")
    run = True
    areen_sound = mixer.Sound((os.path.join("Assets","sounds", "areen_select2.wav")))
    areen_sound.set_volume(0.2)
    praegune_kuu = time.localtime()[1]

    #Areenid images
    galaktika = pygame.image.load(os.path.join("Assets","areen", "galaktika.jpg")).convert_alpha()
    physicum = pygame.image.load(os.path.join("Assets","areen", "physicum.jpg")).convert_alpha()
    taj_mahal = pygame.image.load(os.path.join("Assets","areen", "taj_mahal.jpg")).convert_alpha()
    toomkirik = pygame.image.load(os.path.join("Assets","areen", "toomkirik.jpg")).convert_alpha()
    versailles = pygame.image.load(os.path.join("Assets","areen", "versailles.jpg")).convert_alpha()

    if praegune_kuu == 12:
        raekoda = pygame.image.load(os.path.join("Assets","areen", "raekoda_talv.jpg")).convert_alpha()
    else:
        raekoda = pygame.image.load(os.path.join("Assets","areen", "raekoda.jpg")).convert_alpha()
    
    esimene_rida = 54
    teine_rida = 324
    veerg_1 = 67
    veerg_2 = 404
    veerg_3 = 741

    galaktika_button = arena_button(veerg_1, esimene_rida, galaktika, 0.25, "galaktika")
    physicum_button = arena_button(veerg_2, esimene_rida, physicum, 0.25, "physicum")
    tajmahal_button = arena_button(veerg_3, esimene_rida, taj_mahal, 0.25, "taj mahal")
    toomkirik_button = arena_button(veerg_1, teine_rida, toomkirik, 0.25, "toomkirik")
    versailles_button = arena_button(veerg_2, teine_rida, versailles, 0.25, "versailles")
    raekoda_button = arena_button(veerg_3, teine_rida, raekoda, 0.25, "raekoda")

    tagasi_button = Button(SCREEN_WIDTH/2, SCREEN_HEIGHT - 50, 0.5, "Tagasi")

    while run:
        screen.blit(bg_menu,(0,0))
        keys_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

        if galaktika_button.draw(screen) and time.time() - current_time > 0.1:
            areen_sound.play()
            bg_image = galaktika
            main_menu()
        elif physicum_button.draw(screen) and time.time() - current_time > 0.1:
            areen_sound.play()
            bg_image = physicum
            main_menu()
        elif tajmahal_button.draw(screen) and time.time() - current_time > 0.1:
            areen_sound.play()
            bg_image = taj_mahal
            main_menu()
        elif toomkirik_button.draw(screen) and time.time() - current_time > 0.1:
            areen_sound.play()
            bg_image = toomkirik
            main_menu()
        elif versailles_button.draw(screen) and time.time() - current_time > 0.1:
            areen_sound.play()
            bg_image = versailles
            main_menu()
        elif raekoda_button.draw(screen) and time.time() - current_time > 0.1:
            areen_sound.play()
            bg_image = raekoda
            main_menu()

        elif tagasi_button.draw(screen) and time.time() - current_time > 0.1:
            click_sound.play()
            main_menu()

        elif keys_pressed[pygame.K_q]:
            run = False
            break
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