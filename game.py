import pygame
import random
from gamefunc import *
import math
from colorpalette import *


def startGame():

    pygame.init()
    backgroundImg = pygame.image.load("images/background.png")

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
    plength = 20
    pwidth = 10

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
    countdown = 0

    # game active state
    gameFINISH = False
    gameOVER = False
    timesUp = False

    clock = pygame.time.Clock()
    timer = 500

    counter, countdowntext = 10, "10".rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consolas', 30)

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
        avatar(px, py, name, GUI, plength, pwidth)

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
                # # timer countdown
                # seconds = clock.tick() / 1000
                countdown = 1

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
        timer -= countdown
        showTimer = math.trunc(timer)

        # timer display in GUI
        timerFont = pygame.font.SysFont(None, 30)
        timerText = timerFont.render("Time Left: " + str(showTimer), 1, [255, 0, 0])
        GUI.blit(timerText, [300, 50])

        # timer
        if showTimer <= 0:
            if gameOVER != True:
                timesUp = True

        # COLLISIONS TYPES
        frontCollision = xpos - plength
        backCollision = xpos + width
        topSpaceCollision = ypos + length
        bottomSpaceCollision = ypos + length + space - pwidth

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

        # offScreen collision
        if px <= -70:
            gameOVER = True

        # reset and re-randomize pipes
        obstaclelimit = -110
        if xpos < obstaclelimit:
            xpos = 700
            length = random.randint(30, 450)
            space = random.randint(20, 100)

        if gameOVER:
            gameover(GUI)

        if timesUp:
            timerUp(GUI)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


startGame()

