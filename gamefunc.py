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
    style = pygame.font.SysFont(None, 60)
    words = style.render("Your Submarine Sunk!", True, red)
    words2 = style.render("Press Esc to Quit", True, red)
    GUI.blit(words, [120, 250])
    GUI.blit(words2, [170, 300])


def timerUp(GUI):
    GUI.fill(white)
    style = pygame.font.SysFont(None, 60)
    words = style.render("You Survived!", True, green)
    words2 = style.render("Press Esc to Quit", True, green)
    GUI.blit(words, [200, 250])
    GUI.blit(words2, [170, 300])


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
    style = pygame.font.SysFont(None, 25)
    words = style.render("Press Any Key to Begin. Use Arrow Keys to Move and Avoid the Obstacles!", True, black)
    GUI.blit(words, [0, 500])


def groundCollision(py):
    if py >= 480:
        py = 480
    return py


def ceilingCollision(py):
    if py <= 50:
        py = 50
    return py