import pygame
import os
from time import time
#fixed h and W from main file
WIDTH, HEIGHT = 1080, 640
pygame.font.init()
# https://youtu.be/G8MYGDf_9ho
# Defines the font
main_font = pygame.font.Font((os.path.join("assets","fonts","dimitri.ttf")), 65)
arena_font = pygame.font.Font((os.path.join("assets","fonts","dimitri.ttf")), round(65 * 0.8))

class Button():
    #attributes mouse_position (x,y), image(picture), scale for the picture, text for the button
    def __init__(self, x, y, scale, text_input):
        #gets w and h from image
        self.x = x
        self.y = y
        # h and W for the scaled image (used to center text)
        self.text_input = text_input
        # Renders text
        self.text = main_font.render(self.text_input, True, "white")
        # rectangle creation
        self.rect = self.text.get_rect(center=(x,y))
        # variable for limiting click input
        self.clicked = False

    def draw(self, surface):
        action = False
        surface.blit(self.text, self.rect)
        #get mouse position
        mouse_position = pygame.mouse.get_pos()
        #check mouseover and clicked conditions
        if self.rect.collidepoint(mouse_position):
            # conditions for mouse click 1
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
            # conditions for not pressed button, reseting the click with variable "clicked"
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        return action

    def saladus(self):
        self.rect = pygame.Rect((817,75), (50, 56))




class arena_button(Button):
    def __init__(self, x, y, image, scale, text_input):
        super().__init__(x, y, scale, text_input)
        self.image = image
        width = self.image.get_width()
        height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.clicked = False
        self.text = arena_font.render(self.text_input, True, "white")
        self.rect.topleft = (x, y)
        # centers text for button
        self.text_rect = self.text.get_rect(center=(self.x + (scale * width) // 2, self.y + (scale *height) + 30))

    def draw(self, surface):
        action = False
        surface.blit(self.image, (self.rect.x, self.rect.y))
        surface.blit(self.text, self.text_rect)
        #get mouse position
        mouse_position = pygame.mouse.get_pos()
        #check mouseover and clicked conditions
        if self.rect.collidepoint(mouse_position) or self.text_rect.collidepoint(mouse_position):
            #conditions for mouse click 1
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
            # conditions for not pressed button, reseting the click with variable "clicked"
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        return action

