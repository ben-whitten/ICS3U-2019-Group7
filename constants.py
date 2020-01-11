#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: October 2019
# This constants file is CircuitPython Stage game

# CircuitPython screen size is 160x128 and sprites are 16x16
SCREEN_X = 160
SCREEN_Y = 128
SCREEN_GRID_X = 16
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
TOTAL_CLOUDS = 5
CLOUD_SPEED = 0.25
OFF_LEFT_SCREEN = -1 * SPRITE_SIZE
OFF_TOP_SCREEN = -1 * SPRITE_SIZE
OFF_BOTTOM_SCREEN = SCREEN_Y + SPRITE_SIZE
OFF_SCREEN_X = -100
OFF_SCREEN_Y = -100
A_BUTTON = 144
B_BUTTON = 128
UP_BUTTON = 96
DOWN_BUTTON = 112
LEFT_BUTTON = 64
RIGHT_BUTTON = 80
TOTAL_NUMBER_OF_A_BUTTON = 3
TOTAL_NUMBER_OF_B_BUTTON = 3
TOTAL_NUMBER_OF_UP_BUTTON = 3
TOTAL_NUMBER_OF_DOWN_BUTTON = 3
TOTAL_NUMBER_OF_LEFT_BUTTON = 3
TOTAL_NUMBER_OF_RIGHT_BUTTON = 3
FPS = 60
SCREEN_GRID_2_X = 4
BORDER_LOCATION = 48
BUTTON_HEIGHT = 110
JUNGLE_JOE_START_X = 0
JUNGLE_JOE_START_Y = 97
TOTAL_NUMBER_OF_A_LOGS = 2
SCROLL_SPEED = 4
LOG_1_START_X = 0
LOG_1_START_Y = 112
RIGHT_LOG = 40
LOG_2_START_Y = 48
INCOMING_LOG_HEIGHT = 0
LEFT_LOG = 0
DEATH_LOCATION = 20
JUNGLE_JOE_X_SPEED = 0.5
JUNGLE_JOE_Y_SPEED = 1
SCROLL_SPEED = 1
SPEED_INCREASE = 0.5


MT_GAME_STUDIO_PALETTE = (b'\xf8\x1f\x00\x00\xcey\x00\xff\xf8\x1f\xff\x19\xfc\xe0\xfd\xe0'
       b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')

SCORE_PALETTE = (b'\xf8\x1f\x00\x00\xcey\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'
       b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')

# Using for button state
button_state = {
    "button_up": "up",
    "button_just_pressed": "just pressed",
    "button_still_pressed": "still pressed",
    "button_released": "released",
}
