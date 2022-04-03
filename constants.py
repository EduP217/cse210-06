from game.elements.color import Color
#----------------------------------------------
# GENERAL GAME CONSTANTS
#----------------------------------------------

# GAME
GAME_NAME = "Ping Ppong"
FRAME_RATE = 60

#SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

#FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

#FONT
FONT_FILE = "ping_pong/assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

#SOUND
BOUNCE_SOUND = 'ping_pong/assests/sounds/boing.wav'
WELCOME_SOUND = "ping_pong/assets/sounds/start.wav"
OVER_SOUND = 'ping_pong/assests/sounds/over.wav'

#TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

#COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

#KEYS
LEFT = 'left'
RIGHT = 'right'
SPACE = 'space'
ENTER = "enter"
PAUSE = 'p'

#SCENES
NEW_GAME = 0
TRY_AGAIN = 1
IN_PLAY = 2
GAME_OVER = 3

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

#-------------------------------------------------
# CASTING CONSTANTS
#-------------------------------------------------

#STATS
STATS_GROUP = 'stats'
DEFAULT_LIVES = 3

#HUD 
HUD_MARGING = 15
LIVES_GROUP = 'lives'
SCORE_GROUP = 'score'
LIVES_FORMAT = 'LIVES: {}'
SCORE_FORMAT = 'SCORE: {}'

#BALL
BALL_GROUP = 'balls'
BALL_IMAGE = "ping_pong/assets/images/000.png"
BALL_WIDTH = 28
BALL_HEIGHT = 28
BALL_VELOCITY = 6

#RACKET
RACKET_GROUP = "rackets"
RACKET_IMAGE = "ping_pong/assets/images/white.gif"
RACKET_WIDTH = 106
RACKET_HEIGHT = 28
RACKET_VELOCITY = 7

#YARD_LINES
YARD_LINES_GROUP = 'lines'
YARD_LINES_IMAGE = 'ping_pong/assets/images/white.gif'
YARD_LINES_WIDTH = 80
YARD_LINES_HEIGHT = 28

#DIALOG
DIALOG_GROUP = 'dialogs'
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME_OVER"

