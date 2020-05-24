"""
Test code for the MetalGear package
Test solidsnake.py
"""

import unittest
from MetalGear.solidsnake import Snake

class TestFoxHound(unittest.TestCase):
    @staticmethod
    def test_solidsnake():
        solid_snake = Snake()
        print(f'{__name__} => \n{solid_snake}')


if __name__ == '__main__':
    unittest.main()
