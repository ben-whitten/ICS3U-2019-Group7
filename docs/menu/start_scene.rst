.. _start_scene:

Start Scene
===========

[IMPORTANT] Most of the menu scene here is COMPLETELY optional. You can easily make a good menu where you press start to go to gaem scene. as such, I will not explain how I turned it into a menu that you would find in any other modern game but I will give you a quick summary. Basically, this program only changes the text to give off the appearance that the option is selected, while in actuality I just have the buttons change the option number (to change the text/start game) and the game mode(to change game mode). Other than that, the rest is very simple. i simply painted the top 6/8ths of the screen with blue, the bottom 2/8ths of the screen black and placed the tree top sprites just over it. Also, I decided to spawn clouds by choosing a randon Y value to spawn at (off screen) and then having their x value increase by 1 each time the game goes through the while true loop. Fianlly, I placed jungle joe and the sun just like any other sprites and placed text on the screen where I wanted. I did all this using the code below.
.. toctree::
    code.py
    # this function is the main menu scene
    text = []
    sprites = []
    sun = []
    game_mode_text = []
    game_mode = 0
    option = 1

    image_bank_5 = stage.Bank.from_bmp16("Backgrounds.bmp")
    image_bank_5 = stage.Bank.from_bmp16("backgrounds.bmp")
    image_bank_3 = stage.Bank.from_bmp16("jungle_joe.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_5, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.TREE_TOP_GRID_Y, constants.TREE_TOP_GRID_2_Y):
            background.tile(x_location, y_location, 1)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.BLACK_BACK_GRID_Y, constants.BLACK_BACK_GRID_2_Y):
            background.tile(x_location, y_location, 7)

    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    text_1 = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    text_1.move(40, 20)
    text_1.text("JUNGLE JOE")
    text.append(text_1)

    text_2 = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    text_2.move(40, 30)
    text_2.text("& SNAKOB'S")
    text.append(text_2)

    text_3 = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    text_3.move(25, 40)
    text_3.text("BONGO BANANZA!")
    text.append(text_3)

    text_3 = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    text_3.move(0, 0)
    text_3.text("Version:{0}".format(constants.VERSION_NUMBER))
    text.append(text_3)

    start_text = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    start_text.clear()
    start_text.cursor(0, 0)
    start_text.move(constants.START_X, constants.START_Y)
    start_text.text("   START   ")
    text.append(start_text)

    game_mode_text = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    game_mode_text.clear()
    game_mode_text.cursor(0, 0)
    game_mode_text.move(constants.GAME_MODE_1_X, constants.GAME_MODE_Y)
    game_mode_text.text("<< NORMAL MODE >>")
    text.append(game_mode_text)

    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    up_button = constants.button_state["button_up"]
    down_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # Displays the sun
    sun_top_left = stage.Sprite(image_bank_5, 11, 128, 0)
    sun.append(sun_top_left)
    sun_top_right = stage.Sprite(image_bank_5, 10, 144, 0)
    sun.append(sun_top_right)
    sun_bottom_left = stage.Sprite(image_bank_5, 8, 128, 16)
    sun.append(sun_bottom_left)
    sun_bottom_right = stage.Sprite(image_bank_5, 9, 144, 16)
    sun.append(sun_bottom_right)
    # Displays Jungle Joe
    jungle_joe = stage.Sprite(image_bank_3, 15, 71, 66)
    sprites.append(jungle_joe)
    jungle_joe_jumping = stage.Sprite(image_bank_3, 14, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
    sprites.append(jungle_joe_jumping)

    clouds = []
    for cloud_number in range(constants.TOTAL_CLOUDS):
        a_single_cloud = stage.Sprite(image_bank_5, 4, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        clouds.append(a_single_cloud)

    def Show_clouds():
        for cloud_number in range(len(clouds)):
            if clouds[cloud_number].y < 0:
                clouds[cloud_number].move(constants.OFF_LEFT_SCREEN, random.randint(0 - constants.SPRITE_SIZE, constants.CLOUD_SPAWN_Y - constants.SPRITE_SIZE))
                break

    cloud_count = 6
    Show_clouds()
    Show_clouds()

    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers, items show up in order
    game.layers = sprites + text + clouds + sun + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    # wait until refresh rate finishes
    game.render_block()
    # repeat forever, game loop

    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        #print(keys)
        if keys & ugame.K_UP != 0:
            if up_button == constants.button_state["button_up"]:
                up_button = constants.button_state["button_just_pressed"]
            elif up_button == constants.button_state["button_just_pressed"]:
                up_button = constants.button_state["button_still_pressed"]
        else:
            if up_button == constants.button_state["button_still_pressed"]:
                up_button = constants.button_state["button_released"]
            else:
                up_button = constants.button_state["button_up"]

        if keys & ugame.K_DOWN != 0:
            if down_button == constants.button_state["button_up"]:
                down_button = constants.button_state["button_just_pressed"]
            elif down_button == constants.button_state["button_just_pressed"]:
                down_button = constants.button_state["button_still_pressed"]
        else:
            if down_button == constants.button_state["button_still_pressed"]:
                down_button = constants.button_state["button_released"]
            else:
                down_button = constants.button_state["button_up"]

        if keys & ugame.K_X != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]

        if keys & ugame.K_O != 0:
            if b_button == constants.button_state["button_up"]:
                b_button = constants.button_state["button_just_pressed"]
            elif b_button == constants.button_state["button_just_pressed"]:
                b_button = constants.button_state["button_still_pressed"]
        else:
            if b_button == constants.button_state["button_still_pressed"]:
                b_button = constants.button_state["button_released"]
            else:
                b_button = constants.button_state["button_up"]

        if keys & ugame.K_SELECT != 0:
            if select_button == constants.button_state["button_up"]:
                select_button = constants.button_state["button_just_pressed"]
            elif select_button == constants.button_state["button_just_pressed"]:
                select_button = constants.button_state["button_still_pressed"]
        else:
            if select_button == constants.button_state["button_still_pressed"]:
                select_button = constants.button_state["button_released"]
            else:
                select_button = constants.button_state["button_up"]

        if keys & ugame.K_START != 0:
            if start_button == constants.button_state["button_up"]:
                start_button = constants.button_state["button_just_pressed"]
            elif start_button == constants.button_state["button_just_pressed"]:
                start_button = constants.button_state["button_still_pressed"]
        else:
            if start_button == constants.button_state["button_still_pressed"]:
                start_button = constants.button_state["button_released"]
            else:
                start_button = constants.button_state["button_up"]

        if down_button == constants.button_state["button_just_pressed"] or up_button == constants.button_state["button_just_pressed"]:
            if option == 0:
                option = 1
                start_text.clear()
                start_text.cursor(0, 0)
                start_text.move(constants.START_X, constants.START_Y)
                start_text.text("   START   ")
                game.render_block()
                if game_mode == 0:
                    game_mode_text.clear()
                    game_mode_text.cursor(0, 0)
                    game_mode_text.move(constants.GAME_MODE_1_X, constants.GAME_MODE_Y)
                    game_mode_text.text("<< NORMAL MODE >>")
                    game.render_block()
                elif game_mode == 1:
                    game_mode_text.clear()
                    game_mode_text.cursor(0, 0)
                    game_mode_text.move(constants.GAME_MODE_2_X, constants.GAME_MODE_Y)
                    game_mode_text.text("<< ENDLESS MODE >>")
                    game.render_block()
            elif option == 1:
                option = 0
                start_text.clear()
                start_text.cursor(0, 0)
                start_text.move(constants.START_X, constants.START_Y)
                start_text.text("<< START >>")
                game.render_block()
                if game_mode == 0:
                    game_mode_text.clear()
                    game_mode_text.cursor(0, 0)
                    game_mode_text.move(constants.GAME_MODE_1_X, constants.GAME_MODE_Y)
                    game_mode_text.text("   NORMAL MODE   ")
                    game.render_block()
                elif game_mode == 1:
                    game_mode_text.clear()
                    game_mode_text.cursor(0, 0)
                    game_mode_text.move(constants.GAME_MODE_2_X, constants.GAME_MODE_Y)
                    game_mode_text.text("   ENDLESS MODE   ")
                    game.render_block()

        if (start_button == constants.button_state["button_just_pressed"] or select_button == constants.button_state["button_just_pressed"]
            or a_button == constants.button_state["button_just_pressed"] or b_button == constants.button_state["button_just_pressed"]):
            if option == 0:
                sound.play(coin_sound)
                jungle_joe_jumping.move(jungle_joe.x, jungle_joe.y)
                jungle_joe.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                while True:
                    if jungle_joe_jumping.y > 50:
                        jungle_joe_jumping.move(jungle_joe_jumping.x, jungle_joe_jumping.y - constants.JUNGLE_JOE_Y_SPEED)
                        game.render_sprites(sprites)
                        game.tick()
                    else:
                        break
                while True:
                    jungle_joe_jumping.move(jungle_joe_jumping.x, jungle_joe_jumping.y + constants.JUNGLE_JOE_Y_SPEED)
                    game.render_sprites(sprites)
                    game.tick()
                    if jungle_joe_jumping.y > constants.SCREEN_Y:
                        game_scene(game_mode)
            elif option == 1:
                if game_mode == 1:
                    game_mode = 0
                    game_mode_text.clear()
                    game_mode_text.cursor(0, 0)
                    game_mode_text.move(constants.GAME_MODE_1_X, constants.GAME_MODE_Y)
                    game_mode_text.text("<< NORMAL MODE >>")
                    game.render_block()
                elif game_mode == 0:
                    game_mode = 1
                    game_mode_text.clear()
                    game_mode_text.cursor(0, 0)
                    game_mode_text.move(constants.GAME_MODE_2_X, constants.GAME_MODE_Y)
                    game_mode_text.text("<< ENDLESS MODE >>")
                    game.render_block()

        # update game logic
        for cloud_number in range (len(clouds)):
            if clouds[cloud_number].y > 0:
                clouds[cloud_number].move(clouds[cloud_number].x
                                          + constants.CLOUD_SPEED,
                                          clouds[cloud_number].y)
                if clouds[cloud_number].x > constants.SCREEN_X + constants.SPRITE_SIZE:
                    clouds[cloud_number].move(constants.OFF_SCREEN_X,
                                              constants.OFF_SCREEN_Y)
                    Show_clouds()
                if clouds[cloud_number].x > constants.SCREEN_X / 2:
                    Show_clouds()
        # redraw sprite list
        pass # just a placeholder until you write the code

        game.render_sprites(clouds)
        game.tick()
       
    constants.py
    VERSION_NUMBER = "1.0.1"
    TREE_TOP_GRID_Y = 5
    TREE_TOP_GRID_2_Y = 6
    BLACK_BACK_GRID_Y = 6
    BLACK_BACK_GRID_2_Y = 8
    SPRITE_SIZE = 16
    TOTAL_CLOUDS = 5
    CLOUD_SPEED = 0.25
    CLOUD_SPAWN_Y = 80
    GAME_MODE_1_X = 10
    GAME_MODE_2_X = 8
    GAME_MODE_Y = 100
    START_X = 35
    START_Y = 118

