from surface import Surface
from settings import COLORS


# Score surface to display the score
class ScoreSurface(Surface):
    
    # Calls all the necessary methods of the ScoreSurface class
    def run(self):
        self.surface.fill(COLORS[0])        # BG color
        self.draw()