"""
Test code for the MetalGear package
Test bigboss.py
"""

import unittest
from MetalGear.bigboss import Boss

class TestBigBoss(unittest.TestCase):
    def test_bigboss(self):
        big_boss = Boss()
        assert big_boss.__str__(), 'Return should not be empty'
        print(f'{self.test_bigboss.__name__} => {big_boss}')


if __name__ == '__main__':
    unittest.main()
