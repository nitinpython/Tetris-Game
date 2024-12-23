from surface import Surface
from settings import COLORS
import pygame as pg


# Score surface to display the score
class ScoreSurface(Surface):
    
    def __init__(self, parent_screen, width, height, x, y):
        super().__init__(parent_screen, width, height, x, y)

        self.font_size = 20
        self.font = pg.font.SysFont('consolas', self.font_size, True)

    
    def show_score(self, score):
        text = f'Score: {score}'
        color = 'black'

        rendered_text = self.font.render(text, False, color)

        self.surface.blit(rendered_text, (self.width//5, self.height//2))
    
    
    # Calls all the necessary methods of the ScoreSurface class
    def run(self, score):
        self.draw()
        self.surface.fill(COLORS[0])        # BG color
        self.show_score(score)