import pygame
from colorpalette import *


# PRIMARY FUNCTIONS
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