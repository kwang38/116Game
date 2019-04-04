import unittest
from gamefunc import groundCollision
from gamefunc import ceilingCollision
import pygame
import sys


class TestLimits(unittest.TestCase):

    def test_ceilinglimit(self):
        self.py = 35
        self.assertEqual(ceilingCollision(self.py), 50, msg='assert equal 50')

    def test_groundlimit(self):
        self.py = 481
        self.assertEqual(groundCollision(self.py), 480, msg='assert equal 480')


if __name__ == '__main__':
    unittest.main()
