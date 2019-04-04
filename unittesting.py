import unittest
from game import groundCollision
from game import ceilingCollision
import pygame
import sys


# def testCONTROLSREGISTER():
#
#     pygame.init
#     pygame.display.set_mode((100, 100))
#     pygame.display.set_caption('Keyboard Register')
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     print('LEFT ARROW PRESSED')
#                 if event.key == pygame.K_RIGHT:
#                     print('RIGHT ARROW PRESSED')
#                 if event.key == pygame.K_UP:
#                     print('UP ARROW PRESSED')
#                 if event.key == pygame.K_DOWN:
#                     print('DOWN ARROW PRESSED')
#                 if event.key == pygame.K_ESCAPE:
#                     print('ESCAPE KEY PRESSED')
#                     sys.exit()
#
#         pygame.display.flip()
#
# testCONTROLSREGISTER()


class TestLimits(unittest.TestCase):

    def test_ceilinglimit(self):
        self.py = 35
        self.assertEqual(ceilingCollision(self.py), 50, msg='assert equal 50')

    def test_groundlimit(self):
        self.py = 481
        self.assertEqual(groundCollision(self.py), 480, msg='assert equal 480')




if __name__ == '__main__':
    unittest.main()