.. _splash_scene:

Splash Scene
============

in our version of the game, we have a splash screen with our company logo, Elemental Studios. However, this step will most likely vary from person to person as you may want to use your own company logo. To do this, we used two seperate image banks so we can have more sprites on the screen for the elements in the corners. This, hwoever, meant that we needed to render each part of the elements in the corners as seperate sprites. You can do something similar with the following code.
.. toctree::
    code.py
    def game_splash_scene():
    # this function is the game scene
    text = []
    sprites = []
    image_bank_3 = stage.Bank.from_bmp16("jungle_joe.bmp")
    image_bank_4 = stage.Bank.from_bmp16("elemental_studios.bmp")
    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_3, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    text_1 = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    text_1.move(13, 60)
    text_1.text("ELEMENTAL STUDIOS")
    text.append(text_1)

    text_2 = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    text_2.move(40, 80)
    text_2.text("PRESENTS...")
    text.append(text_2)

    fire_upper_right = stage.Sprite(image_bank_4, 0, 16, 0)
    sprites.append(fire_upper_right)
    fire_bottom_right = stage.Sprite(image_bank_4, 1, 16, 16)
    sprites.append(fire_bottom_right)
    fire_upper_left = stage.Sprite(image_bank_4, 2, 0, 0)
    sprites.append(fire_upper_left)
    fire_bottom_left = stage.Sprite(image_bank_4, 3, 0, 16)
    sprites.append(fire_bottom_left)
    water_upper_right = stage.Sprite(image_bank_4, 6, 144, 0)
    sprites.append(water_upper_right)
    water_bottom_right = stage.Sprite(image_bank_4, 7, 144, 16)
    sprites.append(water_bottom_right)
    water_upper_left = stage.Sprite(image_bank_4, 4, 128, 0)
    sprites.append(water_upper_left)
    water_bottom_left = stage.Sprite(image_bank_4, 5, 128, 16)
    sprites.append(water_bottom_left)
    earth_upper_right = stage.Sprite(image_bank_4, 10, 16, 98)
    sprites.append(earth_upper_right)
    earth_bottom_right = stage.Sprite(image_bank_4, 11, 16, 112)
    sprites.append(earth_bottom_right)
    earth_upper_left = stage.Sprite(image_bank_4, 8, 0, 98)
    sprites.append(earth_upper_left)
    earth_bottom_left = stage.Sprite(image_bank_4, 9, 0, 112)
    sprites.append(earth_bottom_left)
    wind_upper_right = stage.Sprite(image_bank_4, 14, 144, 98)
    sprites.append(wind_upper_right)
    wind_bottom_right = stage.Sprite(image_bank_4, 15, 144, 112)
    sprites.append(wind_bottom_right)
    wind_upper_left = stage.Sprite(image_bank_4, 12, 128, 98)
    sprites.append(wind_upper_left)
    wind_bottom_left = stage.Sprite(image_bank_4, 13, 128, 112)
    sprites.append(wind_bottom_left)
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = sprites + text + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    # wait until refresh rate finishes
    game.render_block()
    # repeat forever, game loop
    while True:
        # get user input
        # update game logic
        time.sleep(1.0)
        main_menu_scene()
        # redraw sprite list
        pass # just a placeholder until you write the code

    constants.py
    SCREEN_GRID_X = 16
    SCREEN_GRID_Y = 8
