import pygame
import sys
import os
#fixed h and W from main file
WIDTH, HEIGHT = 1080, 640
pygame.font.init()
# Defines the font
main_font = pygame.font.Font((os.path.join("Assets","Fonts","dimitri.ttf")), 65)

class Button():
    #attributes pos (x,y), image(picture), scale for the picture, text for the button
    def __init__(self, x, y, image, scale, text_input, on_off):
        #gets w and h from image
        self.x = x
        self.y = y
        self.on_off = on_off
        #scales image to prefered size
        # h and W for the scaled image (used to center text)
        self.text_input = text_input
        # Renders text
        if self.on_off == True:
            self.width = image.get_width()
            self.height = image.get_height()
            self.image = pygame.transform.scale(image, (int(self.width * scale), int(self.height * scale)))
            # rectangle creation
            self.rect = self.image.get_rect()
            # rectangle axis
            self.rect.topleft = (x,y)
            width =self.image.get_width()
            height = self.image.get_height()
            # variable for limiting click input
            self.clicked = False
            # greates a rectangle for text and centers it
            self.text = main_font.render(self.text_input, True, "white")
            self.text_rect = self.text.get_rect(center=(self.x - (width/2) , self.y - (height/2)))
        elif self.on_off == False:
            self.text = main_font.render(self.text_input, True, "white")
            # rectangle creation
            self.rect = self.text.get_rect(center=(x,y))
            # variable for limiting click input
            self.clicked = False




    def draw(self, surface):

        action = False

        # draws image on screen
        if self.on_off == True:
            surface.blit(self.image, (self.rect.x, self.rect.y))
            surface.blit(self.text, self.text_rect)
        else:
            surface.blit(self.text, (self.rect.x, self.rect.y))
        #get mouse position
        pos = pygame.mouse.get_pos()
        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            # conditions for mouse click 1
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
            # conditions for not pressed button, reseting the click with variable "clicked"
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        return action

    # Method for putting the button on the middle of the left hand side of the screen. This method changes the x and y.
    
    def left_middle_pos(self):
        global WIDTH, HEIGHT
        width = self.image.get_width()
        height = self.image.get_height()
        x = int((WIDTH/2 - width) / 2)
        y = int((HEIGHT/2 - height/2))
        self.rect.topleft = (x,y)
        # centers text on button
        self.text_rect = self.text.get_rect(center=(x + width/2, y + height/2))

    # Method for putting the button on the middle of the right hand side of the screen
    def right_middle_pos(self):
        global WIDTH, HEIGHT
        width = self.image.get_width()
        height = self.image.get_height()
        x = int(WIDTH/2 + (WIDTH/2 - width) / 2)
        y = int((HEIGHT/2 - height/2))
        self.rect.topleft = (x,y)
        # centers text for button
        self.text_rect = self.text.get_rect(center=(x + width/2, y + height/2))
    
    def arena_button(self):
        global WIDTH, HEIGHT
        width = self.image.get_width()
        height = self.image.get_height()
        self.rect.topleft = (self.x, self.y)
        # centers text for button
        self.text_rect = self.text.get_rect(center=(self.x + width/2, self.y + height + 30))


