#!/usr/bin/env python3

# Created by: Ben Lapuhapo
# Created on: Jan 16 2020
# This file is the "Space Aliens" game
#   for CircuitPython

import ugame
import stage
import board
import neopixel
import time
import random

import constants


def mt_splash_scene():
    # this function is the MT splash scene

    # an image bank for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # used this program to split the iamge into tile: https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white

    text = []

    text1 = stage.Text(width=29, height=14, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)

    # get sound ready
    # follow this guide to convert your other sounds to something that will work
    #    https://learn.adafruit.com/microcontroller-compatible-audio-file-conversion

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
        # play coin sound
        coin_sound = open("coin.wav", 'rb')
        sound = ugame.audio
        sound.stop()
        sound.mute(False)
        sound.play(coin_sound)
        # update game logic
        # Wait for 1 seconds
        time.sleep(2.0)
        our_splash_scene()

        # redraw sprite list

def our_splash_scene():
    # this function is the MT splash scene

    # an image bank for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("splash3.bmp")




    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    text = []

    text1 = stage.Text(width=50, height=20, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text1.move(35, 30)
    text1.text("Ben & Dylan")
    text.append(text1)

    # sets background to the image 5 in the bank
    background.tile(0, 0, 5)
    background.tile(1, 0, 5)
    background.tile(2, 0, 5)
    background.tile(3, 0, 5)
    background.tile(4, 0, 5)
    background.tile(5, 0, 5)
    background.tile(6, 0, 5)
    background.tile(7, 0, 5)
    background.tile(8, 0, 5)
    background.tile(9, 0, 5)

    background.tile(0, 1, 5)
    background.tile(1, 1, 5)
    background.tile(2, 1, 5)
    background.tile(3, 1, 5)
    background.tile(4, 1, 5)
    background.tile(5, 1, 5)
    background.tile(6, 1, 5)
    background.tile(7, 1, 5)
    background.tile(8, 1, 5)
    background.tile(9, 1, 5)

    background.tile(0, 2, 5)
    background.tile(1, 2, 5)
    background.tile(2, 2, 5)
    background.tile(3, 2, 5)
    background.tile(4, 2, 5)
    background.tile(5, 2, 5)
    background.tile(6, 2, 5)
    background.tile(7, 2, 5)
    background.tile(8, 2, 5)
    background.tile(9, 2, 5)

    background.tile(0, 3, 5)
    background.tile(1, 3, 5)
    background.tile(2, 3, 5)
    background.tile(3, 3, 5)
    background.tile(6, 3, 5)
    background.tile(7, 3, 5)
    background.tile(8, 3, 5)
    background.tile(9, 3, 5)

    background.tile(0, 4, 5)
    background.tile(1, 4, 5)
    background.tile(2, 4, 5)
    background.tile(3, 4, 5)
    background.tile(6, 4, 5)
    background.tile(7, 4, 5)
    background.tile(8, 4, 5)
    background.tile(9, 4, 5)

    background.tile(0, 5, 5)
    background.tile(1, 5, 5)
    background.tile(2, 5, 5)
    background.tile(3, 5, 5)
    background.tile(4, 5, 5)
    background.tile(5, 5, 5)
    background.tile(6, 5, 5)
    background.tile(7, 5, 5)
    background.tile(8, 5, 5)
    background.tile(9, 5, 5)

    background.tile(0, 6, 5)
    background.tile(1, 6, 5)
    background.tile(2, 6, 5)
    background.tile(3, 6, 5)
    background.tile(4, 6, 5)
    background.tile(5, 6, 5)
    background.tile(6, 6, 5)
    background.tile(7, 6, 5)
    background.tile(8, 6, 5)
    background.tile(9, 6, 5)

    background.tile(0, 7, 5)
    background.tile(1, 7, 5)
    background.tile(2, 7, 5)
    background.tile(3, 7, 5)
    background.tile(4, 7, 5)
    background.tile(5, 7, 5)
    background.tile(6, 7, 5)
    background.tile(7, 7, 5)
    background.tile(8, 7, 5)
    background.tile(9, 7, 5)

    # shows our splash screen, make a 160x128 palette then cut to 4 and puzzle it together
    background.tile(4, 3, 1)
    background.tile(5, 3, 3)
    background.tile(4, 4, 2)
    background.tile(5, 4, 4)


    text2 = stage.Text(width=29, height=14, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text2.move(30, 100)
    text2.text("Game Studios")
    text.append(text2)


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
        transition_sound = open("transition.wav", 'rb')
        sound = ugame.audio
        sound.stop()
        sound.mute(False)
        sound.play(transition_sound)
        # update game logic
        time.sleep(2)
        menu_scene()

def menu_scene():
    # import sound
    transition_sound = open("transition.wav", 'rb')
    sound = ugame.audio # load sound
    sound.stop()
    sound.mute(False)
    sound.play(transition_sound) # play sound

    # an image bank for CircuitPython
    image_bank_3 = stage.Bank.from_bmp16("sprite.bmp")
    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_3, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    background.tile(0, 0, 9)
    background.tile(1, 0, 9)
    background.tile(2, 0, 9)
    background.tile(3, 0, 9)
    background.tile(4, 0, 9)
    background.tile(5, 0, 9)
    background.tile(6, 0, 9)
    background.tile(7, 0, 9)
    background.tile(8, 0, 9)
    background.tile(9, 0, 9)

    background.tile(0, 1, 9)
    background.tile(1, 1, 9)
    background.tile(2, 1, 9)
    background.tile(3, 1, 9)
    background.tile(4, 1, 9)
    background.tile(5, 1, 9)
    background.tile(6, 1, 9)
    background.tile(7, 1, 9)
    background.tile(8, 1, 9)
    background.tile(9, 1, 9)

    background.tile(0, 2, 9)
    background.tile(1, 2, 9)
    background.tile(2, 2, 9)
    background.tile(3, 2, 9)
    background.tile(4, 2, 9)
    background.tile(5, 2, 9)
    background.tile(6, 2, 9)
    background.tile(7, 2, 9)
    background.tile(8, 2, 9)
    background.tile(9, 2, 9)

    background.tile(0, 3, 9)
    background.tile(1, 3, 9)
    background.tile(2, 3, 9)
    background.tile(3, 3, 9)
    background.tile(4, 3, 9)
    background.tile(5, 3, 9)
    background.tile(6, 3, 9)
    background.tile(7, 3, 9)
    background.tile(8, 3, 9)
    background.tile(9, 3, 9)

    background.tile(0, 4, 9)
    background.tile(1, 4, 9)
    background.tile(2, 4, 9)
    background.tile(3, 4, 9)
    background.tile(4, 4, 9)
    background.tile(5, 4, 9)
    background.tile(6, 4, 9)
    background.tile(7, 4, 9)
    background.tile(8, 4, 9)
    background.tile(9, 4, 9)

    background.tile(0, 5, 9)
    background.tile(1, 5, 9)
    background.tile(2, 5, 9)
    background.tile(3, 5, 9)
    background.tile(4, 5, 9)
    background.tile(5, 5, 9)
    background.tile(6, 5, 9)
    background.tile(7, 5, 9)
    background.tile(8, 5, 9)
    background.tile(9, 5, 9)

    background.tile(0, 6, 9)
    background.tile(1, 6, 9)
    background.tile(2, 6, 9)
    background.tile(3, 6, 9)
    background.tile(4, 6, 9)
    background.tile(5, 6, 9)
    background.tile(6, 6, 9)
    background.tile(7, 6, 9)
    background.tile(8, 6, 9)
    background.tile(9, 6, 9)

    background.tile(0, 7, 9)
    background.tile(1, 7, 9)
    background.tile(2, 7, 9)
    background.tile(3, 7, 9)
    background.tile(4, 7, 9)
    background.tile(5, 7, 9)
    background.tile(6, 7, 9)
    background.tile(7, 7, 9)
    background.tile(8, 7, 9)
    background.tile(9, 7, 9)

    text = []

    text1 = stage.Text(width=29, height=15, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text1.move(40, 10)
    text1.text("Jumpy Bun")
    text.append(text1)

    text2 = stage.Text(width=60, height=30, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text2.move(35, 100)
    text2.text("PRESS START")
    text.append(text2)
    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = text + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    while True:
        # get user input
        # update game logic
        keys = ugame.buttons.get_pressed()
        #print(keys)
        if keys & ugame.K_START != 0:  # Start button
            menu_sound = open("menu.wav", 'rb')
            sound = ugame.audio # load sound
            sound.stop()
            sound.mute(False)
            sound.play(menu_sound) # play sound
            game_scene()

def game_scene():
    # this function is the game scene

    # game score
    score = 0

    def show_alien():
        # I know this is a function that is using variables outside of itself!
        #   BUT this code is going to be used in 2 places :)
        # make an alien show up on screen in the x-axis
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x < 0: # meaning it is off the screen, so available to move on the screen
                aliens[alien_number].move(random.randint(0 + constants.SPRITE_SIZE, constants.SCREEN_X - constants.SPRITE_SIZE), constants.OFF_TOP_SCREEN)
                break
    # buttons that you want to keep state information on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]


    # an image bank for CircuitPython
    image_bank_1 = stage.Bank.from_bmp16("sprite.bmp")
    image_bank_2 = stage.Bank.from_bmp16("sprite.bmp")
    # a list of sprites that will be updated every frame
    background  = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    background.tile(0, 0, 1)
    background.tile(1, 0, 2)
    background.tile(2, 0, 1)
    background.tile(3, 0, 2)
    background.tile(4, 0, 1)
    background.tile(5, 0, 2)
    background.tile(6, 0, 1)
    background.tile(7, 0, 2)
    background.tile(8, 0, 1)
    background.tile(9, 0, 2)

    background.tile(0, 1, 1)
    background.tile(1, 1, 2)
    background.tile(2, 1, 1)
    background.tile(3, 1, 2)
    background.tile(4, 1, 1)
    background.tile(5, 1, 2)
    background.tile(6, 1, 1)
    background.tile(7, 1, 2)
    background.tile(8, 1, 1)
    background.tile(9, 1, 2)

    background.tile(0, 2, 1)
    background.tile(1, 2, 2)
    background.tile(2, 2, 1)
    background.tile(3, 2, 2)
    background.tile(4, 2, 1)
    background.tile(5, 2, 2)
    background.tile(6, 2, 1)
    background.tile(7, 2, 2)
    background.tile(8, 2, 1)
    background.tile(9, 2, 2)

    background.tile(0, 3, 13)
    background.tile(1, 3, 13)
    background.tile(2, 3, 13)
    background.tile(3, 3, 13)
    background.tile(4, 3, 13)
    background.tile(5, 3, 13)
    background.tile(6, 3, 13)
    background.tile(7, 3, 13)
    background.tile(8, 3, 13)
    background.tile(9, 3, 13)

    background.tile(0, 4, 13)
    background.tile(1, 4, 13)
    background.tile(2, 4, 13)
    background.tile(3, 4, 13)
    background.tile(4, 4, 13)
    background.tile(5, 4, 13)
    background.tile(6, 4, 13)
    background.tile(7, 4, 13)
    background.tile(8, 4, 13)
    background.tile(9, 4, 13)

    background.tile(0, 5, 13)
    background.tile(1, 5, 13)
    background.tile(2, 5, 13)
    background.tile(3, 5, 13)
    background.tile(4, 5, 13)
    background.tile(5, 5, 13)
    background.tile(6, 5, 13)
    background.tile(7, 5, 13)
    background.tile(8, 5, 13)
    background.tile(9, 5, 13)

    background.tile(0, 6, 10)
    background.tile(1, 6, 11)
    background.tile(2, 6, 10)
    background.tile(3, 6, 11)
    background.tile(4, 6, 10)
    background.tile(5, 6, 11)
    background.tile(6, 6, 10)
    background.tile(7, 6, 11)
    background.tile(8, 6, 10)
    background.tile(9, 6, 11)

    background.tile(0, 7, 12)
    background.tile(1, 7, 12)
    background.tile(2, 7, 12)
    background.tile(3, 7, 12)
    background.tile(4, 7, 12)
    background.tile(5, 7, 12)
    background.tile(6, 7, 12)
    background.tile(7, 7, 12)
    background.tile(8, 7, 12)
    background.tile(9, 7, 12)
    sprites = []

    # create lasers for when we shoot
    # create aliens
    aliens = []
    for alien_number in range(constants.TOTAL_NUMBER_OF_PLATFORMS):
        a_single_alien = stage.Sprite(image_bank_1, 6, constants.OFF_SCREEN_X, constants.OFF_SCREEN_X)
        aliens.append(a_single_alien)


    # current number of aliens that should be moving down screen, start with just 1
    alien_count = 1
    show_alien()
    # add text at top of screen for score
    score_text = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    score_text.clear()
    score_text.cursor(0, 0)
    score_text.move(1, 1)
    score_text.text("Score: {0}".format(score))

    ship = stage.Sprite(image_bank_1, 3, int(constants.SCREEN_X / 2), constants.SCREEN_Y - constants.SPRITE_SIZE)
    sprites.append(ship) # insert at the top of sprite list



    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = sprites + aliens + [score_text] + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        #print(keys)

        if keys & ugame.K_X != 0:  # A button
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]

        # update game logic

        # if right D-Pad is pressed
        if keys & ugame.K_RIGHT != 0:
            # if ship moves off right screen, move it back
            if ship.x > constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.x = constants.SCREEN_X - constants.SPRITE_SIZE
            # else move ship right
            else:
                ship.move(ship.x + constants.SHIP_SPEED, ship.y)

        # if left D-Pad is pressed
        if keys & ugame.K_LEFT != 0:
            # if ship moves off left screen, move it back
            if ship.x < 0:
                ship.x = 0
            # else move ship left
            else:
                ship.move(ship.x - constants.SHIP_SPEED, ship.y)

        # each frame move the aliens down the screen
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0: # meaning it is on the screen
                aliens[alien_number].move(aliens[alien_number].x, aliens[alien_number].y + constants.ALIEN_SPEED)
                if aliens[alien_number].y > constants.SCREEN_Y:
                    aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    show_alien() # make it randomly show up at top again


        # each frame check if any of the aliens are touching the ship
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                # https://circuitpython-stage.readthedocs.io/en/latest/#stage.collide
                # and https://stackoverflow.com/questions/306316/determine-if-two-rectangles-overlap-each-other
                if stage.collide(aliens[alien_number].x + 1, aliens[alien_number].y,
                                 aliens[alien_number].x + 15, aliens[alien_number].y + 15,
                                 ship.x, ship.y,
                                 ship.x + 15, ship.y + 15):
                    # Wait for 1 seconds
                    time.sleep(4.0)
                    game_over_scene(score)

        # redraw sprite list
        game.render_sprites(sprites + aliens)
        game.tick() # wait until refresh rate finishes

if __name__ == "__main__":
    mt_splash_scene()