import pygame

from config import BACKGROUND_COLOR, FPS, WINDOW_SIZE, WINDOW_TITLE


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption(WINDOW_TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self) -> None:
        self.clock.tick(FPS)

    def render(self) -> None:
        self.screen.fill(BACKGROUND_COLOR)
        pygame.display.flip()

    def run(self) -> None:
        try:
            while self.running:
                self.handle_events()
                self.update()
                self.render()
        finally:
            self.shutdown()

    def shutdown(self) -> None:
        self.running = False
        pygame.quit()
