import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game): ############################check
        """Initialise the ship and set its starting position."""

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the image and gets its rect.
        self.image = pygame.image.load('images/ship_pixian_ai.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's horizontal and vertical position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag; starting with no movement.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """Update the ship's position based on movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed # Move right
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed # Move left

        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed # Move up
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed # Move down
        
        self.rect.x = self.x  # Update rect object from self.x
        self.rect.y = self.y  # Update rect object from self.y

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)