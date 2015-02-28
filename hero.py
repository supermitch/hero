import pygame

from classes.game import Game

def main():
    pygame.init()
    game = Game()
    game.main_loop()
    print('Goodbye.')

if __name__=='__main__':
    main()

