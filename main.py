import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock() 
    
    dt = 0
    
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    Player.containers = updatable_group, drawable_group
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    
    shot_group = pygame.sprite.Group()
    Shot.containers = shot_group,updatable_group,drawable_group
    
    asteroid_group = pygame.sprite.Group()
    Asteroid.containers = asteroid_group, updatable_group, drawable_group

    AsteroidField.containers = updatable_group
    AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        updatable_group.update(dt)
        
        for asteroid in asteroid_group:
            if player.collision(asteroid):
                print("Game Over") 
                exit()
            for shot in shot_group:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()
        
        for task in drawable_group:
            task.draw(screen)
            
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
    
if __name__ == "__main__":
    main()