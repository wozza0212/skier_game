'''
Created on 13 Sep 2021

@author: thomaswasnidge
'''
import sys
import cfg 
import pygame 
import random 

class SkierClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.direction = 0
        self.imagepaths = cfg.SKIER_IMAGE_PATHS[:-1]
        self.image = pygame.image.load(self.imagepaths[self.direction])
        self.rect = self.image.get_rect()
        self.rect.center = [320, 100]
        self.speed = [self.direction, 6 - abs(self.direction) * 2]
        
    def turn(self, num):
        self.direction += num
        self.direction = max(-2, self.direction)
        self.direction = min(2, self.direction)
        
        center = self.rect.center
        self.image = pygame.image.load(self.imagepaths[self.direction])
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speed = [self.direction, 6-abs(self.direction)*2]
        return self.speed
    
    def move(self):
        self.rect.centerx += self.speed[0]
        self.rect.centerx = max(20, self.rect.centerx)
        self.rect.center = min(620, self.rect.centerx)
        
    
    def setFall(self):
        self.image = pygame.image.load(cfg.SKIER_IMAGE_PATHS[-1])
        
    def setForward(self):
        self.direction = 0
        self.image = pygame.image.load(self.imagepaths[self.direction])
            
            
            
class ObstacleClass(pygame.sprite.Sprite):
    def __init__(self, img_path, location, attribute):
        pygame.sprite.Sprite.__init__(self)
        self.img_path = img_path
        self.image = pygame.image.load(self.img_path)
        self.location = location
        self.rect = self.image.get_rect()
        self.rect.center = self.location
        self.attribute = attribute
        self.passed = False
        
    def move(self, num):
        self.rect.centery = self.location[1] - num
        
def creatObstacles(s, e, num=10):
    obstacles = pygame.sprite.Group()
    locations = []
    
    for i in range(num):
        row = random.randint(s, e)
        col = random.randint(0, 9)
        location = [col*64+20, row*64+20]
        if location not in locations:
            locations.append(location)
            attribute = random.choice(list(cfg.OBSTACLE_PATHS.keys()))
            img_path = cfg.OBSTACLE_PATHS[attribute]
            obstacle = ObstacleClass(img_path, location, attribute)
            obstacles.add(obstacle)
    return obstacles 

def AddObstacles(obstacles0, obstacles1):
    obstacles = pygame.sprite.Group()
    for obstacle in obstacles0:
        obstacles.add(obstacle)
    for obstacle in obstacles1:
        obstacles.add(obstacle)
    return obstacles
            
            
            
            
    
        
            
        
        
        