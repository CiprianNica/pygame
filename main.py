import pygame, sys
class Game():
    runners = []
    _startLine =20
    _finishLine = 620
    def __init__(self):
        self._screen = pygame.display.set_mode((640, 480))
        self._background = pygame.image.load("carreraTortugas/background.png")
        pygame.display.set_caption("Carrera bichos")

    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
            self._screen.blit(self._background, (0, 0))
            pygame.display.flip()
        pygame.quit()
        sys.exit
if __name__ == "__main__":
    game = Game()
    pygame.font.init()
    game.competir()
