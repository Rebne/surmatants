import pygame

class Player():
    def __init__(self, x, y, hBarRatio):
        self.healthHeight = 30
        self.width = 80
        self.height = 180
        self.rect = pygame.Rect((x, y, self.width, self.height))
        self.isDucking = False
        self.jumpSpeed = 0
        self.isJumping = False
        self.isAttacking = False
        self.actionTime = 0
        self.actionCD = 400
        self.movingRight = False
        self.healthNr = 100
        self.health = pygame.Rect(x, y - 40, self.healthNr, self.healthHeight)
        

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
        
        #Detecting keypresses
        key = pygame.key.get_pressed()
        
        self.jumpSpeed += GRAVITY
        dy += self.jumpSpeed
        
        if side == "left":
            #Moving is disabled while attacking
            if self.isAttacking == False and pygame.time.get_ticks() - self.actionTime > self.actionCD:
                #Moving lef/right mechanics
                if key[pygame.K_a] and self.isDucking == False:
                    self.movingRight = False
                    dx = -SPEED
                if key[pygame.K_d] and self.isDucking == False:
                    self.movingRight = True
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
                    dx = -SPEED
                if key[pygame.K_RIGHT] and self.isDucking == False:
                    self.movingRight = True
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
        self.health.update(self.rect.x, self.rect.y - 40, self.healthNr, self.healthHeight)
        
        
    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 255), self.rect)
        pygame.draw.rect(surface, (0, 255, 0), self.health)
        
        
    def attacking(self, surface, enemy):
        
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
        pygame.draw.rect(surface, (255, 0, 0), attackrect)
        if pygame.Rect.colliderect(attackrect, enemy):
            print(f"Player {enemy} HIT")
            enemy.healthNr -= 10
            enemy.health.update(enemy.rect.x, enemy.rect.y - 40, enemy.healthNr, enemy.healthHeight)
            #print(enemy.healthNr)
        self.isAttacking = False
        
        