.. _background:

Background
==========

The game scene's background is split up into two different portions. These being the jungle side, which takes up roughly 2/5ths of the screen, and the game portion, which takes up roughlt 3/5ths of the screen. To do this, your going to need to paint the first 2/5ths of the screen (x grid = 0-4) with the tree sprite (sprites 2 and 3 of backgrounds) and the other 3/5ths (5-10) with the grey background sprite (sprite 5 of backgrounds) using the code below. Finally, this last step is optional, but if you want you can randomize the tree sprites on the left hand of the screen using the lines of the code below.
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

    constants.py:
    SCREEN_GRID_X = 16
    SCREEN_GRID_Y = 8
    SCREEN_GRID_2_X = 4
