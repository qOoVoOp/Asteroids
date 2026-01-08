import pygame
from constants import *
from logger import log_state , log_event
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
import sys
from circleshape import CircleShape
from shot import Shot


 

def main():
    pygame.init()
    clock =pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player =  Player(x, y)

    Asteroid.containers = (asteroids, updatable, drawable)

    Shot.containers = (shots, updatable, drawable)

    AsteroidField.containers = (updatable,)
    asteroidfield = AsteroidField()
    

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000

        screen.fill("black")

        updatable.update(dt)

        for asteroid in asteroids: 
            player_collision = CircleShape.collides_with(asteroid, player)
    
            if player_collision:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                shot_collision = CircleShape.collides_with(asteroid, shot)
                if shot_collision:
                    log_event("asteroid_shot")
                    asteroid.kill()



        for drawing in drawable:
            drawing.draw(screen)
        
        pygame.display.flip()

    



if __name__ == "__main__":
    main()
