from surface import Surface
from settings import COLORS


# Preview surface to show the next block
class PreviewSurface(Surface):
    
    # Calls all the necessary methods of the PreviewSurface class
    def run(self):
        self.surface.fill(COLORS[0])        # BG color
        self.draw()