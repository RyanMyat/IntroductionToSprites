'''
Chapter 13: Introduction to Sprites
Homework Assignment
Ryan Myat
May 22, 2020
'''

import sys
import pygame
import time

class Trainer(pygame.sprite.Sprite):
    
    def __init__(self,x,y):
        super().__init__()

        # load the sprite sheet
        sheet = pygame.image.load("player.png").convert()

        # lists for different animation frames
        self.frameup = []
        self.framedown = []
        self.frameright =[]
        self.frameleft = []

        self.direction = "None"
        
        for i in range(4):
            self.frameup.append(pygame.Surface([79,85]).convert())
            patch = (79*i,255,79,85)
            self.frameup[i].blit(sheet,(0,0),patch)
            self.frameup[i].set_colorkey((255,255,255))

        for i in range(4):
            self.framedown.append(pygame.Surface([79,85]).convert())
            patch = (79*i,0,79,85)
            self.framedown[i].blit(sheet,(0,0),patch)
            self.framedown[i].set_colorkey((255,255,255))

        for i in range(4):
            self.frameright.append(pygame.Surface([79,85]).convert())
            patch = (79*i,170,79,85)
            self.frameright[i].blit(sheet,(0,0),patch)
            self.frameright[i].set_colorkey((255,255,255))

        for i in range(4):
            self.frameleft.append(pygame.Surface([79,85]).convert())
            patch = (79*i,85,79,85)
            self.frameleft[i].blit(sheet,(0,0),patch)
            self.frameleft[i].set_colorkey((255,255,255))

        # set the image and rect properities to the first frame
        self.anim_frame = 0
        self.image = self.framedown[0] 
        self.rect = self.image.get_rect()

        # set the initial position & other atributes
        self.rect.x = x
        self.rect.y = y
        self.deltax = 0
        self.deltay = 0

    def update(self):
        self.anim_frame = (self.anim_frame+1)%4

        if self.direction == "Up":
            self.image = self.frameup[self.anim_frame]
        elif self.direction == "Down":
            self.image = self.framedown[self.anim_frame]
        elif self.direction == "Right":
            self.image = self.frameright[self.anim_frame]
        elif self.direction == "Left":
            self.image = self.frameleft[self.anim_frame]

        # set the boundary for the trainer
        if self.rect.x < 0:
            self.rect.x = 0
            self.deltax = 0
            self.direction == "None"
        if self.rect.x > 461:
            self.rect.x = 461
            self.deltax = 0
            self.direction == "None"
        if self.rect.y < 140:
            self.rect.y = 140
            self.deltay = 0
            self.direction == "None"
        if self.rect.y > 395:
            self.rect.y = 395
            self.deltay = 0
            self.direction == "None"

        self.rect.x += self.deltax
        self.rect.y += self.deltay

def main():
    
    pygame.init()

    # create a display surface to draw on
    main_surface = pygame.display.set_mode((640,480))
    
    pygame.display.set_caption("Pokemon Trainer")
    
    # create the sprite(s)
    ash = Trainer(281,310)

    # initialize the sprite group(s)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(ash)

    # game loop
    while True:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                key = event.dict['key']
                if event.type == pygame.K_UP:
                    ash.deltax = 0
                    ash.deltay -= -2
                    ash.direction = "Up"
                elif event.type == pygame.K_DOWN:
                    ash.deltax = 0
                    ash.deltay += 2
                    ash.direction = "Down"
                elif event.type == pygame.K_RIGHT:
                    ash.deltax += 2
                    ash.deltay = 0
                    ash.direction = "Right"
                elif event.type == pygame.K_LEFT:
                    ash.deltax -= 2
                    ash.deltay = 0
                    ash.direction = "Left"
                elif key == 32:
                    ash.deltax = 0
                    ash.deltay = 0
                    ash.direction = "None"

        # update
        all_sprites.update()

        # draw the background
        background = pygame.image.load("pokemonroad.png")
        main_surface.blit(background,(0,0))
    
        all_sprites.draw(main_surface)

        # flip the updated screen
        pygame.display.flip()

        # keep it from going too fast
        time.sleep(0.01)

if __name__=='__main__':
    main()
