.. _space_ship:

Jungle Joe
==========

Jungle Joe is completely optional to the actual game, but he adds alot to it with his animations. To start, you need to make two sprites using sprites 14 and 15 of the image bank, jungle_joe. To make his animations, you are going to want to make a new function called score_update to save space and so you wont need to write the code six times. A quick sumary of how the code works is that the game checks to see where jungle joe is, then moves him accordingly so that he is above the next log up. Finally, it moves everything downwards and spawns a new log.
.. toctree::
    code.py:
    # Displays Jungle Joe and logs
    jungle_joe_standing = stage.Sprite(image_bank_3, 15, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y )
    jungle_joe.append(jungle_joe_standing)
    jungle_joe_jumping = stage.Sprite(image_bank_3, 14, constants.JUNGLE_JOE_START_X, constants.OFF_TOP_SCREEN)
    jungle_joe.append(jungle_joe_jumping)

     logs = []
    for log_number in range(constants.TOTAL_NUMBER_OF_A_LOGS):
        a_single_log = stage.Sprite(image_bank_3, 13, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        logs.append(a_single_log)

    logs[0].move(constants.LOG_1_START_X, constants.LOG_1_START_Y)
    logs[1].move(constants.RIGHT_LOG, constants.LOG_2_START_Y)

    def score_update():
        # I know this is a function that is using variables outside of itself!
        #   BUT this code is going to be used in multiple places
        # update the score when you correctly hit a button or when you hit a milestone
        score = score + 1
        # Refreshes score text
        score_text.clear()
        score_text.cursor(0, 0)
        score_text.move(1, 1)
        score_text.text("Score:{0}".format(score))
        game.render_block()
        if score % 10 == 0:
            sound.play(coin_sound)
            height = height + 24
            button_speed += constants.SPEED_INCREASE
            jungle_joe[1].move(jungle_joe[0].x, jungle_joe[0].y)
            jungle_joe[0].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
            while True:
                if logs[0].y < 50:
                    if jungle_joe[1].x > logs[0].x:
                        jungle_joe[1].move(jungle_joe[1].x - constants.JUNGLE_JOE_X_SPEED, jungle_joe[1].y)
                    if jungle_joe[1].y > logs[0].y - constants.SPRITE_SIZE:
                        jungle_joe[1].move(jungle_joe[1].x, jungle_joe[1].y - constants.JUNGLE_JOE_Y_SPEED)
                if jungle_joe[1].x == logs[0].x and jungle_joe[1].y == logs[0].y - constants.SPRITE_SIZE and jungle_joe[1].y < 50:
                    jungle_joe[0].move(jungle_joe[1].x, jungle_joe[1].y)
                    jungle_joe[1].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    break
                    
    constants.py
    JUNGLE_JOE_START_X = 0
    JUNGLE_JOE_NORMAL_Y = 97
    TOTAL_NUMBER_OF_A_LOGS = 2
    SCROLL_SPEED = 4
    LOG_1_START_X = 0
    LOG_1_START_Y = 112
    RIGHT_LOG = 40
    LOG_2_START_Y = 48
    INCOMING_LOG_HEIGHT = 0
    LEFT_LOG = 0
    JUNGLE_JOE_X_SPEED = 0.5
    JUNGLE_JOE_Y_SPEED = 1
    SCROLL_SPEED = 1
    SPEED_INCREASE = 0.5
