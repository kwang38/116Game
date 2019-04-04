import pygame
import random
from gamefunc import *
from colorpalette import *
backgroundImg = pygame.image.load("images/background.png")
subImg = pygame.image.load("images/sub.png")


def startGame():

    pygame.init()

    # screen details
    WIDTH = 700
    HEIGHT = 550
    FPS = 60
    screensize = WIDTH, HEIGHT
    GUI = pygame.display.set_mode(screensize)

    pygame.display.set_caption("Under Da Sea Adventures")

    # IN GAME VALUES

    # player name
    name = "Player01"

    # player position at start of game
    px = 150
    py = 150

    # object positions
    xpos = 700
    ypos = 0

    # object size- randomized
    width = random.randint(30, 80)
    length = random.randint(30, 350)
    space = random.randint(20, 100)

    # speed
    xspeed = 0
    yspeed = 0
    movespeed = 6
    stopspeed = 0
    pipspeed = 0

    # game active state
    gameFINISH = False
    gameOVER = False

    clock = pygame.time.Clock()

    while not gameFINISH:
        # background

        GUI.blit(backgroundImg, [0, 0])

        # top pipe
        toppipe(xpos, ypos, width, length, GUI)

        # bottom pipe
        bottompipe(xpos, ypos, width, length, space, GUI)

        # ceiling
        ceiling(GUI)

        # ground
        ground(GUI)

        # player
        avatar(px, py, name, GUI)

        # instructions
        Instruction(GUI)

        # movement
        py += yspeed
        px += xspeed
        xpos -= pipspeed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameFINISH = True

            # CONTROLS
            if event.type == pygame.KEYDOWN:

                # START MOVING PIPES
                pipspeed = 4

                if event.key == pygame.K_UP:
                    yspeed = -movespeed
                if event.key == pygame.K_DOWN:
                    yspeed = movespeed
                if event.key == pygame.K_RIGHT:
                    xspeed = movespeed
                if event.key == pygame.K_LEFT:
                    xspeed = -movespeed

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    yspeed = stopspeed
                if event.key == pygame.K_DOWN:
                    yspeed = stopspeed
                if event.key == pygame.K_RIGHT:
                    xspeed = stopspeed
                if event.key == pygame.K_LEFT:
                    xspeed = stopspeed

            # REAL TIME UNIT TESTING
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print('LEFT ARROW PRESSED')
                if event.key == pygame.K_RIGHT:
                    print('RIGHT ARROW PRESSED')
                if event.key == pygame.K_UP:
                    print('UP ARROW PRESSED')
                if event.key == pygame.K_DOWN:
                    print('DOWN ARROW PRESSED')
                if event.key == pygame.K_ESCAPE:
                    print('ESCAPE KEY PRESSED')
                    quit()

        # COLLISIONS TYPES
        frontCollision = xpos - 20
        backCollision = xpos + width
        topSpaceCollision = ypos + length
        bottomSpaceCollision = ypos + length + space - 10

        # top pipe collision
        if frontCollision < px < backCollision and py < topSpaceCollision:
            gameOVER = True

        # bottom pipe collision
        if frontCollision < px < backCollision and py > bottomSpaceCollision:
            gameOVER = True

        # ceiling collision
        if py <= 50:
            py = 50

        # ground collision
        if py >= 490:
            py = 490

        # reset and re-randomize pipes
        if xpos < -80:
            xpos = 700
            length = random.randint(30, 450)
            space = random.randint(20, 100)

        if gameOVER:
            gameover(GUI)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


startGame()

