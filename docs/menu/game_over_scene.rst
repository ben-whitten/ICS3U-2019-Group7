.. _game_over_scene:

Game Over Scene
===============

The game over scene does not take a lot of work, firstly make sure you set score and height as parameters when you call this function as you will need to use them here.

The only image bank you will need is the jungle joe image bank as it will act as the background for this scene. You will need both score and mt game studio palette to make this scene.

Now set the background like we have done in all the other scenes, after the background is set we must create the text for this scene. The text will display your final score, your final height, GAME OVER, and if you would like to retry or return to menu scene.

The code to display the text is:
.. toctree::
    text = []

    text0 = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    text0.move(22, 20)
    text0.text("Final Score: {:0>2d}".format(final_score))
    text.append(text0)

    text2 = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    text2.move(37, 30)
    text2.text("Height: {:0>2d}ft".format(final_height))
    text.append(text2)

    text1 = stage.Text(width=29, height=14, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text1.move(43, 60)
    text1.text("GAME OVER")
    text.append(text1)
    
    menu_text = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    menu_text.clear()
    menu_text.cursor(0, 0)
    menu_text.move(constants.MENU_LOCATION_X, constants.MENU_LOCATION_Y)
    menu_text.text("   MENU   ")
    text.append(menu_text)

    retry_text = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    retry_text.clear()
    retry_text.cursor(0, 0)
    retry_text.move(constants.RETRY_LOCATION_X, constants.RETRY_LOCATION_Y)
    retry_text.text("<< RETRY >>")
    text.append(retry_text)


Next we need to set up the option to go back to menu or retry the game. To do this we have to set up the buttons to accept inputs and to change which screen you go to depending on which option the user presses. To do this you will need this code which codes for the user selecting the option they desire and them using their up and down arrow keys to go to the option.
.. toctree::
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

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

        # update game logic

        #print(keys)
        if down_button == constants.button_state["button_just_pressed"] or up_button == constants.button_state["button_just_pressed"]:

            if option == 0:
                option = 1
                menu_text.clear()
                menu_text.cursor(0, 0)
                menu_text.move(constants.MENU_LOCATION_X, constants.MENU_LOCATION_Y)
                menu_text.text("<< MENU >>")
                game.render_block()
                retry_text.clear()
                retry_text.cursor(0, 0)
                retry_text.move(constants.RETRY_LOCATION_X, constants.RETRY_LOCATION_Y)
                retry_text.text("   RETRY   ")
                game.render_block()
            elif option == 1:
                option = 0
                retry_text.clear()
                retry_text.cursor(0, 0)
                retry_text.move(constants.RETRY_LOCATION_X, constants.RETRY_LOCATION_Y)
                retry_text.text("<< RETRY >>")
                game.render_block()
                menu_text.clear()
                menu_text.cursor(0, 0)
                menu_text.move(constants.MENU_LOCATION_X, constants.MENU_LOCATION_Y)
                menu_text.text("   MENU   ")
                game.render_block()

        if keys & ugame.K_X != 0 or keys & ugame.K_O != 0 or keys & ugame.K_START != 0 or keys & ugame.K_SELECT != 0:  # A, B, start or select
            if option == 0:
                sound.play(coin_sound)
                # This is so they can hear the full sound
                time.sleep(1.0)
                game_scene(game_mode)
            elif option == 1:
                sound.play(coin_sound)
                # This is so they can hear the full sound
                time.sleep(1.0)
                main_menu_scene()


After you input all this code you must add the render text option and add in all variables you need. After all this is done your code should look like this:
.. toctree::
    def game_over_scene(final_score, final_height):
    # this function is the game over scene
    option = 0
    # This is so it can get into the game scene. Only one option as you cant get here on endless
    game_mode = 0
    # an image bank for CircuitPython
    image_bank_3 = stage.Bank.from_bmp16("jungle_joe.bmp")
    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_3, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    text = []

    text0 = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    text0.move(22, 20)
    text0.text("Final Score: {:0>2d}".format(final_score))
    text.append(text0)

    text2 = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    text2.move(37, 30)
    text2.text("Height: {:0>2d}ft".format(final_height))
    text.append(text2)

    text1 = stage.Text(width=29, height=14, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text1.move(43, 60)
    text1.text("GAME OVER")
    text.append(text1)

    menu_text = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    menu_text.clear()
    menu_text.cursor(0, 0)
    menu_text.move(constants.MENU_LOCATION_X, constants.MENU_LOCATION_Y)
    menu_text.text("   MENU   ")
    text.append(menu_text)

    retry_text = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    retry_text.clear()
    retry_text.cursor(0, 0)
    retry_text.move(constants.RETRY_LOCATION_X, constants.RETRY_LOCATION_Y)
    retry_text.text("<< RETRY >>")
    text.append(retry_text)

    up_button = constants.button_state["button_up"]
    down_button = constants.button_state["button_up"]

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = text + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

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

        # update game logic

        #print(keys)
        if down_button == constants.button_state["button_just_pressed"] or up_button == constants.button_state["button_just_pressed"]:

            if option == 0:
                option = 1
                menu_text.clear()
                menu_text.cursor(0, 0)
                menu_text.move(constants.MENU_LOCATION_X, constants.MENU_LOCATION_Y)
                menu_text.text("<< MENU >>")
                game.render_block()
                retry_text.clear()
                retry_text.cursor(0, 0)
                retry_text.move(constants.RETRY_LOCATION_X, constants.RETRY_LOCATION_Y)
                retry_text.text("   RETRY   ")
                game.render_block()
            elif option == 1:
                option = 0
                retry_text.clear()
                retry_text.cursor(0, 0)
                retry_text.move(constants.RETRY_LOCATION_X, constants.RETRY_LOCATION_Y)
                retry_text.text("<< RETRY >>")
                game.render_block()
                menu_text.clear()
                menu_text.cursor(0, 0)
                menu_text.move(constants.MENU_LOCATION_X, constants.MENU_LOCATION_Y)
                menu_text.text("   MENU   ")
                game.render_block()

        if keys & ugame.K_X != 0 or keys & ugame.K_O != 0 or keys & ugame.K_START != 0 or keys & ugame.K_SELECT != 0:  # A, B, start or select
            if option == 0:
                sound.play(coin_sound)
                # This is so they can hear the full sound
                time.sleep(1.0)
                game_scene(game_mode)
            elif option == 1:
                sound.play(coin_sound)
                # This is so they can hear the full sound
                time.sleep(1.0)
                main_menu_scene()
