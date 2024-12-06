# Game surface specifications
ROWS = 20
COLUMNS = 10
BLOCK_SIZE = 30
GAME_SURFACE_WIDTH = COLUMNS * BLOCK_SIZE
GAME_SURFACE_HEIGHT = ROWS * BLOCK_SIZE
PADDING = 20

# Side panel specifications (contains preview and score surfaces)
SIDE_PANEL_WIDTH = GAME_SURFACE_WIDTH // 2

PREVIEW_HEIGHT_FRACTION = 0.7                          # 70 % height of game surface height
SCORE_HEIGHT_FRACTION = 1 - PREVIEW_HEIGHT_FRACTION               # Remaining 30 % height

PREVIEW_SURFACE_HEIGHT = GAME_SURFACE_HEIGHT * PREVIEW_HEIGHT_FRACTION - PADDING // 2
SCORE_SURFACE_HEIGHT = GAME_SURFACE_HEIGHT * SCORE_HEIGHT_FRACTION - PADDING // 2

PREVIEW_SURFACE_X = GAME_SURFACE_WIDTH + 2 * PADDING
SCORE_SURFACE_Y = PREVIEW_SURFACE_HEIGHT + 2 * PADDING

# Game window (display surface) specifications
SCREEN_WIDTH = GAME_SURFACE_WIDTH + SIDE_PANEL_WIDTH + 3 * PADDING
SCREEN_HEIGHT = GAME_SURFACE_HEIGHT + 2 * PADDING
CAPTION = 'Tetris'
BG_COLOR = 'brown'

# Game image files
IMAGE_FILES = {
    'icon': 'Images/icon.png',
    'resume': 'Images/resume.png',
    'restart': 'Images/restart.png',
    'exit': 'Images/exit.png'
}
