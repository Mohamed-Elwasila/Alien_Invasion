import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialise the game, and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # Create a fullscreen window.
        self.screen = pygame.display.set_mode((0, 0), (pygame.FULLSCREEN))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self.update_screen()
            self.clock.tick(60)


    def _check_events(self):
        """Respond to keypresses and mouse events."""
    # Watch for keyboard and mouth events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.SCALED:
                    self.settings.screen_width = self.screen.get_rect().width
                    self.settings.screen_height = self.screen.get_rect().height
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    # Move the ship to the right.
                    self.ship.moving_right = True  # self.ship.rect.x += 3
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    # Move the ship to the left.
                    self.ship.moving_left = True   # self.ship.rect.x -= 3
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    # Move the ship up.
                    self.ship.moving_up = True   # self.ship.rect.y -= 3
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    # Move the ship down.
                    self.ship.moving_down = True   # self.ship.rect.y += 3
                elif event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_ESCAPE:
                    self.screen = pygame.display.set_mode((1200, 800))

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    # Stop moving the ship to the right.
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    # Stop moving the ship to the left.
                    self.ship.moving_left = False
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    # Stop moving the ship up.
                    self.ship.moving_up = False
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    # Stop moving the ship down.
                    self.ship.moving_down = False


    def update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()
        
        

if __name__ == '__main__':
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()