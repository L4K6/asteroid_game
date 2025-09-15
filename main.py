import pygame
from constants import *
from player import Player
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
Player.containers = (updatable, drawable)
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        screen.fill("black")
        
        for drawing in drawable:
            drawing.draw(screen)

        pygame.display.flip()
        #clock.tick(60)
        dt = clock.tick(60)/1000
        
        
if __name__ == "__main__":
    main()
