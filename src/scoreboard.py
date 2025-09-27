import pygame

class Scoreboard:
    """A class to report scoring information."""
    def __init__(self, screen, initial_score=0):
        self.screen = screen
        self.score = initial_score
        self.font = pygame.font.SysFont(None, 48)
        self.text_color = (30, 30, 30)
        self.bg_color = (230, 230, 230)
        self.position = (20, 20)

    def prep_score(self):
        """Turn the score into a rendered image."""
        score_str = f"Score: {self.score}"
        self.score_image = self.font.render(score_str, True, self.text_color, self.bg_color)

        # Get the rect of the image and position it
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen.get_rect().right - 20
        self.score_rect.top = 20
        
    def show_score(self):
        """Draw the score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)