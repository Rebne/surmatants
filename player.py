import pygame

class Player():
    def __init__(self, x, y, hBarRatio, animationData, side):
        self.healthHeight = 30
        self.width = 80
        self.height = 180
        self.rect = pygame.Rect((x, y, self.width, self.height))
        self.isDucking = False
        self.jumpSpeed = 0
        self.isJumping = False
        self.isAttacking = False
        self.actionTime = 0
        self.actionCD = 100
        self.movingRight = side
        self.moving = False
        
        self.alive = True
        self.healthNr = 100
        self.health = pygame.Rect(x, y - 40, self.healthNr, self.healthHeight)
        self.healthBG = pygame.Rect(x, y - 40, 100, self.healthHeight)
        self.healthBorder = pygame.Rect(x - 3, y - 43, 106, self.healthHeight + 6)
        
        self.updateTime = pygame.time.get_ticks()
        self.offset = animationData[4]
        self.size = animationData[2] #Has to be a real size of the sprite
        self.imageScale = animationData[3] #Scaling ratio for the sprites
        self.animationList = self.extractImages(animationData[1], animationData[0])
        self.frameIndex = 0
        self.action = 0 #0:Idle 1:Walking 2:Jumping 3:Roundabout kick 4:Death 5:Projectile 6:Punch 7:Kick 8:Uppercut 9:Double punch 
        #10:Double kick 11:High kick 12:Falling kick 13:Double sided punch 14:Rising kick #15:Rising punch
        self.figther = self.animationList[self.action][self.frameIndex]
        
        
    def extractImages(self, spriteSheet, animationCount):
        spriteImages = []
        for column, animation in enumerate(animationCount):
            rowImgs = []
            for img in range(animation):
                tempImg = spriteSheet.subsurface(img * self.size, column * self.size, self.size, self.size)
                
                rowImgs.append(pygame.transform.scale(tempImg, (self.size * self.imageScale, self.size * self.imageScale)))
            spriteImages.append(rowImgs)
#         print(spriteImages)
        return spriteImages
        
        

    def move(self, side, screen_width, screen_height, surface, enemy):
        #Movement speed
        SPEED = 10
        GRAVITY = 1.5
        #Ground pixel level
        ground = 400
        #Side pixel buffer
        buffer = 20
        #dx and dy are current change in coordinates
        dx = 0
        dy = 0
        
        self.moving = False
        #Detecting keypresses
        key = pygame.key.get_pressed()
        
        self.jumpSpeed += GRAVITY
        dy += self.jumpSpeed
        
        if self.alive:
            
            if side == "left":
                #Moving is disabled while attacking
                if self.isAttacking == False and pygame.time.get_ticks() - self.actionTime > self.actionCD:
                    #Moving lef/right mechanics
                    if key[pygame.K_a] and self.isDucking == False:
                        self.movingRight = False
                        self.moving = True
                        dx = -SPEED
                    if key[pygame.K_d] and self.isDucking == False:
                        self.movingRight = True
                        self.moving = True
                        dx = SPEED
                        
                    #Jumping mechanics
                    if key[pygame.K_w] and self.isJumping == False:
                        self.isJumping = True
                        self.jumpSpeed = -30    
                    
                    
                    #Ducking mechanics
                    if key[pygame.K_s] and self.isJumping == False:
                        if self.isDucking == False:
                            self.height = self.height / 2
                            self.rect.update(self.rect.x, self.rect.y + self.height, self.width, self.height)
                        self.isDucking = True
                    elif self.isJumping == False:
                        self.isDucking = False
                        self.height = 180
                        self.rect.y = ground
                        self.rect.update(self.rect.x, self.rect.y, self.width, self.height)
                        
                    #Attacking mechanics
                    if key[pygame.K_h] and self.isAttacking == False:
                        self.actionTime = pygame.time.get_ticks()
                        #print(self.actionTime)
                        self.isAttacking = True
                        self.attacking(surface, enemy)
                        
            if side == "right":
                #Moving is disabled while attacking
                if self.isAttacking == False and pygame.time.get_ticks() - self.actionTime > self.actionCD:
                    #Moving lef/right mechanics
                    if key[pygame.K_LEFT] and self.isDucking == False:
                        self.movingRight = False
                        self.moving = True
                        dx = -SPEED
                    if key[pygame.K_RIGHT] and self.isDucking == False:
                        self.movingRight = True
                        self.moving = True
                        dx = SPEED
                        
                    #Jumping mechanics
                    if key[pygame.K_UP] and self.isJumping == False:
                        self.isJumping = True
                        self.jumpSpeed = -30    
                    
                    
                    #Ducking mechanics
                    if key[pygame.K_DOWN] and self.isJumping == False:
                        if self.isDucking == False:
                            self.height = self.height / 2
                            self.rect.update(self.rect.x, self.rect.y + self.height, self.width, self.height)
                        self.isDucking = True
                    elif self.isJumping == False:
                        self.isDucking = False
                        self.height = 180
                        self.rect.y = ground
                        self.rect.update(self.rect.x, self.rect.y, self.width, self.height)
                        
                    #Attacking mechanics
                    if key[pygame.K_KP0] and self.isAttacking == False:
                        self.actionTime = pygame.time.get_ticks()
                        #print(self.actionTime)
                        self.isAttacking = True
                        self.attacking(surface, enemy)
                
            
            #Ensures that player stays on screen
                #Screen height wise
            if self.rect.y + dy > ground:
                self.isJumping = False
                dy = 0
                #Screen length wise
            if self.rect.x + dx < buffer:
                dx = buffer - self.rect.x
            if self.rect.right + dx > screen_width - buffer:
                dx = screen_width - buffer - self.rect.right
                
            
            #Player moves according to delta position
            self.rect.y += dy    
            self.rect.x += dx
            
            #Healthbars
            self.healthBorder.update(self.rect.x - 3, self.rect.y - 43, 106, self.healthHeight + 6)
            self.healthBG.update(self.rect.x, self.rect.y - 40, 100, self.healthHeight)
            self.health.update(self.rect.x, self.rect.y - 40, self.healthNr, self.healthHeight)
        
    def update(self):
        animationCd = 100

        if self.alive == False:
            self.action = 4
        elif self.isAttacking:
            self.action = 3
        elif self.isJumping:
            self.action = 2
        elif self.moving:
            self.action = 1
        else:
            self.action = 0
        
        
        if self.frameIndex >= len(self.animationList[self.action]):
            if self.alive == False:
                self.frameIndex = len(self.animationList[self.action]) - 1
            else:
                self.frameIndex = 0
                if self.action == 3:
                    self.isAttacking = False
                
            
        self.fighter = self.animationList[self.action][self.frameIndex]
        
        if pygame.time.get_ticks() - self.updateTime > animationCd:
            self.frameIndex += 1
            self.updateTime = pygame.time.get_ticks()
        
#         lastAction = self.action
        
    def draw(self, surface):
        
#         pygame.draw.rect(surface, (0, 0, 255), self.rect)
        
        img = pygame.transform.flip(self.fighter, not self.movingRight, False)
        surface.blit(img, (self.rect.x - self.offset[0], self.rect.y - self.offset[1]))
        
        pygame.draw.rect(surface, (0,0,0), self.healthBorder)
        pygame.draw.rect(surface, (255,0,0), self.healthBG)
        pygame.draw.rect(surface, (0, 255, 0), self.health)
        
        
        
    def attacking(self, surface, enemy):
        
        if self.alive:
            #Ducking gives extra reach on the attack
            if self.isDucking == True:
                ratio = 2
                
            #Jumping gives negative reach on the attack
            elif self.isJumping == True:
                ratio = 1
            else:
                ratio = 1.5
                
            #Last movement input determines attack direction
            if self.movingRight == True:
                attackrect = pygame.Rect(self.rect.centerx, self.rect.y, self.width * ratio, self.height)
            elif self.movingRight == False:
                attackrect = pygame.Rect(self.rect.centerx - (self.width * ratio), self.rect.y, self.width * ratio, self.height)
#             pygame.draw.rect(surface, (255, 0, 0), attackrect)
            if pygame.Rect.colliderect(attackrect, enemy):
                #print(f"Player {enemy} HIT")
                enemy.healthNr -= 10
                enemy.health.update(enemy.rect.x, enemy.rect.y - 40, enemy.healthNr, enemy.healthHeight)
                if enemy.healthNr <= 0:
                    enemy.alive = False
            
        
        