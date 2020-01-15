.. _background:

Background
==========

The game scene's background is split up into two different portions. These being the jungle side, which takes up roughly 2/5ths of the screen, and the game portion, which takes up roughlt 3/5ths of the screen. To do this, your going to need to paint the first 2/5ths of the screen (x grid = 0-4) with the tree sprite (sprites 2 and 3 of backgrounds) and the other 3/5ths (5-10) with the grey background sprite (sprite 5 of backgrounds) using the code below. Finally, these last steps are optional, but if you want you can randomize the tree sprites on the left hand of the screen using the lines of the code below. Another thing you can do is generate a border between the two backgrounds. You can make this by using the border sprite (sprite 6 of backgrounds) and the code below.
.. toctree::
    code.py:
    image_bank_5 = stage.Bank.from_bmp16("backgrounds.bmp")

    background = stage.Grid(image_bank_5, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
        for x_location in range(constants.SCREEN_GRID_2_X):
            for y_location in range(constants.SCREEN_GRID_Y):
                tile_picked = random.randint(2,3)
                background.tile(x_location, y_location, tile_picked)
        for x_location in range(constants.SCREEN_GRID_2_X, constants.SCREEN_GRID_X):
            for y_location in range(constants.SCREEN_GRID_Y):
                background.tile(x_location, y_location, 5)
                
    # Displays the border.
    border_1 = stage.Sprite(image_bank_5, 6, constants.BORDER_LOCATION, 0)
    border.append(border_1)
    border_2 = stage.Sprite(image_bank_5, 6, constants.BORDER_LOCATION, 16)
    border.append(border_2)
    border_3 = stage.Sprite(image_bank_5, 6, constants.BORDER_LOCATION, 32)
    border.append(border_3)
    border_4 = stage.Sprite(image_bank_5, 6, constants.BORDER_LOCATION, 48)
    border.append(border_4)
    border_5 = stage.Sprite(image_bank_5, 6, constants.BORDER_LOCATION, 64)
    border.append(border_5)
    border_6 = stage.Sprite(image_bank_5, 6, constants.BORDER_LOCATION, 80)
    border.append(border_6)
    border_7 = stage.Sprite(image_bank_5, 6, constants.BORDER_LOCATION, 96)
    border.append(border_7)
    border_8 = stage.Sprite(image_bank_5, 6, constants.BORDER_LOCATION, 112)
    border.append(border_8)

    constants.py:
    SCREEN_GRID_X = 16
    SCREEN_GRID_Y = 8
    SCREEN_GRID_2_X = 4
