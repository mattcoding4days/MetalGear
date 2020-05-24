"""
Test code for the MetalGear package
Test solidsnake.py
"""

import unittest
from MetalGear.solidsnake import Snake

class TestSolidSnake(unittest.TestCase):
    def test_solidsnake(self):
        solid_snake = Snake()
        assert solid_snake.__str__(), 'Return should not be empty'
        print(f'{self.test_solidsnake.__name__} => {solid_snake}')


if __name__ == '__main__':
    unittest.main()
