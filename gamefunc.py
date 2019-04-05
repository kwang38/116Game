import pygame
from colorpalette import *
subImg = pygame.image.load("images/sub.png")


# PRIMARY FUNCTIONS
def avatar(px, py, username, GUI, plength, pwidth):
    GUI.blit(subImg, [px, py, pwidth, plength])
    font = pygame.font.SysFont(None, 30)
    text = font.render(username, True, red)
    GUI.blit(text, [px - 30, py - 30])


def gameover(GUI):
    GUI.fill(white)
    font = pygame.font.SysFont(None, 60)
    text = font.render("Your Submarine Sunk!", True, red)
    text2 = font.render("Press Esc to Quit", True, red)
    GUI.blit(text, [220, 250])
    GUI.blit(text2, [170, 300])


def timerUp(GUI):
    GUI.fill(white)
    font = pygame.font.SysFont(None, 60)
    text = font.render("Player01 Survived! Victory!", True, green)
    text2 = font.render("Press Esc to Quit", True, green)
    GUI.blit(text, [80, 250])
    GUI.blit(text2, [170, 300])


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
    text = font.render("Press Any Key to Begin. Use Arrow Keys to Move and Avoid the Obstacles!", True, black)
    GUI.blit(text, [0, 500])


def groundCollision(py):
    if py >= 480:
        py = 480
    return py


def ceilingCollision(py):
    if py <= 50:
        py = 50
    return py