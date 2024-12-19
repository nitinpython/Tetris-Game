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

# Game behaviour
FPS = 60
GAME_SPEED = 500

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
    'exit': 'Images/exit.png',
    'restart game': 'Images/restart game.png'
}

# Game sound files
SOUND_FILES = {
    'bgm': 'Sounds/bgm.mp3',
    'move': 'Sounds/move.mp3',
    'clear': 'Sounds/clear.mp3',
    'game over': 'Sounds/game over.mp3'
}


# Menu button specifications
OFFSET_X = 40
RESUME_BUTTON_COORDINATES = (SCREEN_WIDTH//2 - OFFSET_X, SCREEN_HEIGHT//6)
RESTART_BUTTON_COORDINATES = (SCREEN_WIDTH//2 - OFFSET_X, SCREEN_HEIGHT//2.4)
EXIT_BUTTON_COORDINATES = (SCREEN_WIDTH//2 - OFFSET_X, SCREEN_HEIGHT//1.5)

# Game colors
COLORS = {
    0: 'pink',
    1: 'red',
    2: 'green',
    3: 'cyan',
    4: 'orange',
    5: 'yellow',
    6: 'purple',
    7: 'blue'
}