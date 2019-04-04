import pygame
import random

# color palette
black = (0, 0, 0)
yellow = (255, 255, 0)
blue = (100, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)
gray = (105, 105, 105)
navy = (0, 0, 128)
bluegray = (112, 138, 144)

# # screen details
# WIDTH = 700
# HEIGHT = 550
# FPS = 60
#
# screensize = WIDTH, HEIGHT
#
# GUI = pygame.display.set_mode(screensize)
#
# pygame.display.set_caption("AVOID THE OBSTACLES")


# IN-GAME VALUES

# # avatar position and movement
# px = 150
# py = 150
#
# # object positions
# xpos= 700
# ypos = 0
#
# # object size- randomized
# width = random.randint(30, 80)
# length = random.randint(30, 350)
# space = random.randint(20, 100)
#
# # speed
# xspeed = 0
# yspeed = 0
# movespeed = 6
# stopspeed = 0
# pipspeed = 0


def avatar(px, py, username, GUI):
    pygame.draw.rect(GUI, yellow, [px, py, 20, 10])
    font = pygame.font.SysFont(None, 30)
    text = font.render(username, True, red)
    GUI.blit(text, [px - 40, py - 50])


def gameover(GUI):
    GUI.fill(white)
    font = pygame.font.SysFont(None, 60)
    text = font.render("Game Over!", True, red)
    text2 = font.render("Press Esc to Quit.", True, red)
    GUI.blit(text, [150, 250])
    GUI.blit(text2, [150, 300])


def toppipe(xpos, ypos, width, length, GUI):
    pygame.draw.rect(GUI, bluegray, [xpos, ypos, width, length])


def bottompipe(xpos, ypos, width, length, space, GUI):
    yposb = ypos+length+space
    lengthb = length + 1000
    pygame.draw.rect(GUI, bluegray, [xpos, yposb, width, lengthb])


def ceiling(GUI):
    pygame.draw.rect(GUI, bluegray, [0, 0, 700, 50])

def ground(GUI):
    pygame.draw.rect(GUI, bluegray, [0, 500, 700, 50])

def Instruction(GUI):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Press Any Key to Begin, Up Down Left Right Arrow to Move, Avoid obstacles", True, black)
    GUI.blit(text, [0, 500])

def groundCollision(py):
    if py >= 480:
        py = 480
    return py

def ceilingCollision(py):
    if py <= 50:
        py = 50
    return py



# pygame.init()
#
# gameFINISH = False
# gameOVER = False
#
# clock = pygame.time.Clock()
#
# while not gameFINISH:
#     # background
#
#     GUI.fill(navy)
#
#     # top pipe
#     toppipe(xpos, ypos, width, length)
#
#     # bottom pipe
#     bottompipe(xpos, ypos, width, length)
#
#     # player
#     avatar(px, py, name)
#
#     # ceiling
#     ceiling()
#
#     # ground
#     ground()
#
#     # instructions
#     Instruction()
#
#     py += yspeed
#     px += xspeed
#     xpos -= pipspeed
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             gameFINISH = True
#
#         # CONTROLS
#         if event.type == pygame.KEYDOWN:
#
#             # START MOVING PIPES
#             pipspeed = 4
#
#             if event.key == pygame.K_UP:
#                 yspeed = -movespeed
#             if event.key == pygame.K_DOWN:
#                 yspeed = movespeed
#             if event.key == pygame.K_RIGHT:
#                 xspeed = movespeed
#             if event.key == pygame.K_LEFT:
#                 xspeed = -movespeed
#
#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_UP:
#                 yspeed = stopspeed
#             if event.key == pygame.K_DOWN:
#                 yspeed = stopspeed
#             if event.key == pygame.K_RIGHT:
#                 xspeed = stopspeed
#             if event.key == pygame.K_LEFT:
#                 xspeed = stopspeed
#
#         # REAL TIME UNIT TESTING
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 print('LEFT ARROW PRESSED')
#             if event.key == pygame.K_RIGHT:
#                 print('RIGHT ARROW PRESSED')
#             if event.key == pygame.K_UP:
#                 print('UP ARROW PRESSED')
#             if event.key == pygame.K_DOWN:
#                 print('DOWN ARROW PRESSED')
#             if event.key == pygame.K_ESCAPE:
#                 print('ESCAPE KEY PRESSED')
#                 quit()
#     # COLLISIONS
#
#     # top pipe collision
#     if xpos - 20 < px < xpos + width and py < ypos+length:
#         gameOVER = True
#     # bottom pipe collision
#     if xpos - 20 < px < xpos + width and py > ypos+length+space-10:
#         gameOVER = True
#
#     # ceiling collision
#     if py <= 50:
#         py = 50
#
#     # ground collision
#     if py >= 480:
#         py = 480
#
#
#     # reset and re-randomize pipes
#     if xpos < -80:
#         xpos = 700
#         length = random.randint(30, 450)
#         space = random.randint(20, 100)
#
#     if gameOVER:
#         gameover()
#
#
#     pygame.display.flip()
#     clock.tick(FPS)
#
# pygame.quit()

def startGame():

    pygame.init()

    # screen details
    WIDTH = 700
    HEIGHT = 550
    FPS = 60

    screensize = WIDTH, HEIGHT

    GUI = pygame.display.set_mode(screensize)

    pygame.display.set_caption("AVOID THE OBSTACLES")

    # IN GAME VALUES

    # player name
    name = "Player01"

    # player position
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

    gameFINISH = False
    gameOVER = False

    clock = pygame.time.Clock()

    while not gameFINISH:
        # background

        GUI.fill(navy)

        # top pipe
        toppipe(xpos, ypos, width, length, GUI)

        # bottom pipe
        bottompipe(xpos, ypos, width, length, space, GUI)

        # player
        avatar(px, py, name, GUI)

        # ceiling
        ceiling(GUI)

        # ground
        ground(GUI)

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
        # COLLISIONS

        # top pipe collision
        if xpos - 20 < px < xpos + width and py < ypos + length:
            gameOVER = True
        # bottom pipe collision
        if xpos - 20 < px < xpos + width and py > ypos + length + space - 10:
            gameOVER = True

        # ceiling collision
        if py <= 50:
            py = 50

        # ground collision
        if py >= 480:
            py = 480

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