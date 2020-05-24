"""
Test code for the MetalGear package
Test bigboss.py
"""

import unittest
from MetalGear.bigboss import Boss

class TestFoxHound(unittest.TestCase):
    @staticmethod
    def test_bigboss():
        big_boss = Boss()
        print(f'{__name__} => \n{big_boss}')


if __name__ == '__main__':
    unittest.main()
