import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid (CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        
        
        
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position, self.radius, 2)
    
    def update(self,dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        
        if(self.radius <= ASTEROID_MIN_RADIUS):
            return True
        else:
           projectile_angle = random.uniform(20,50) 
           split_radius = self.radius - ASTEROID_MIN_RADIUS
           
           split1 = Asteroid(self.position.x, self.position.y, split_radius)
           split2 = Asteroid(self.position.x, self.position.y, split_radius)
           
           split1.velocity = pygame.Vector2.rotate(self.velocity, projectile_angle) * 1.2
           split2.velocity = pygame.Vector2.rotate(self.velocity, -projectile_angle) * 1.2
           
           self.position
        