import pygame
import os

class Menu_animation:
    def __init__(self):
        self.animation_frames = []
        self.animation_frames.append(pygame.image.load(os.path.join("assets","menu_frames", "00001.jpg" )))
        self.animation_frames.append(pygame.image.load(os.path.join("assets","menu_frames", "00004.jpg" )))
        self.animation_frames.append(pygame.image.load(os.path.join("assets","menu_frames", "00007.jpg" )))
        self.animation_frames.append(pygame.image.load(os.path.join("assets","menu_frames", "00010.jpg" )))
        self.animation_frames.append(pygame.image.load(os.path.join("assets","menu_frames", "00013.jpg" )))
        self.animation_frames.append(pygame.image.load(os.path.join("assets","menu_frames", "00016.jpg" )))
        self.animation_frames.append(pygame.image.load(os.path.join("assets","menu_frames", "00019.jpg" )))
        self.animation_frames.append(pygame.image.load(os.path.join("assets","menu_frames", "00022.jpg" )))
        self.animation_frames.append(pygame.image.load(os.path.join("assets","menu_frames", "00025.jpg" )))
        self.animation_frames.append(pygame.image.load(os.path.join("assets","menu_frames", "00028.jpg" )))
        self.animation_frames.append(pygame.image.load(os.path.join("assets","menu_frames", "00031.jpg" )))
        self.animation_frames.append(pygame.image.load(os.path.join("assets","menu_frames", "00034.jpg" )))
        self.animation_frames.append(pygame.image.load(os.path.join("assets","menu_frames", "00037.jpg" )))
        self.animation_frames.append(pygame.image.load(os.path.join("assets","menu_frames", "00040.jpg" )))
        self.animation_frames.append(pygame.image.load(os.path.join("assets","menu_frames", "00043.jpg" )))
        self.animation_frames.append(pygame.image.load(os.path.join("assets","menu_frames", "00046.jpg" )))
        self.animation_frames.append(pygame.image.load(os.path.join("assets","menu_frames", "00049.jpg" )))
        self.animation_frames.append(pygame.image.load(os.path.join("assets","menu_frames", "00052.jpg" )))
        self.animation_frames.append(pygame.image.load(os.path.join("assets","menu_frames", "00055.jpg" )))
        self.current_frame = 0
        self.frame = self.animation_frames[self.current_frame]

    def update(self):
        self.current_frame += 0.015
        if self.current_frame >= len(self.animation_frames):
            self.current_frame = 0
        self.frame = self.animation_frames[int(self.current_frame)]

    def update_areen(self):
        self.current_frame += 0.017
        if self.current_frame >= len(self.animation_frames):
            self.current_frame = 0
        self.frame = self.animation_frames[int(self.current_frame)]

class Lightning:
    def __init__(self):
        self.animation_frames = []
        #self.animation_frames.append(pygame.image.load(os.path.join("assets","menu_frames","lightning","1.jpg")))
        self.animation_frames.append(pygame.image.load(os.path.join("assets","menu_frames","lightning","2.jpg")))
        #self.animation_frames.append(pygame.image.load(os.path.join("assets","menu_frames","lightning","3.jpg")))
        self.animation_frames.append(pygame.image.load(os.path.join("assets","menu_frames","lightning","4.jpg")))
        self.animation_frames.append(pygame.image.load(os.path.join("assets","menu_frames","lightning","5.jpg")))
        self.animation_frames.append(pygame.image.load(os.path.join("assets","menu_frames","lightning","5.jpg")))
        self.animation_frames.append(pygame.image.load(os.path.join("assets","menu_frames","lightning","5.jpg")))
        self.animation_frames.append(pygame.image.load(os.path.join("assets","menu_frames","lightning","5.jpg")))
        self.animation_frames.append(pygame.image.load(os.path.join("assets","menu_frames","lightning","5.jpg")))
        self.animation_frames.append(pygame.image.load(os.path.join("assets","menu_frames","lightning","5.jpg")))
        self.animation_frames.append(pygame.image.load(os.path.join("assets","menu_frames","lightning","5.jpg")))
        self.animation_frames.append(pygame.image.load(os.path.join("assets","menu_frames","lightning","5.jpg")))
        self.animation_frames.append(pygame.image.load(os.path.join("assets","menu_frames","lightning","5.jpg")))
        self.current_frame = 0
        self.frame = self.animation_frames[self.current_frame]
    
    def update(self):
        self.current_frame += 0.0030
        if self.current_frame >= len(self.animation_frames):
            return -1
        self.frame = self.animation_frames[int(self.current_frame)]