"""
Test code for the MetalGear package
test foxhound.py
"""

import unittest
from MetalGear.foxhound import main

class TestFoxHound(unittest.TestCase):
    @staticmethod
    def test_fox():
        print(f'{__name__} => ')
        main()


if __name__ == '__main__':
    unittest.main()
