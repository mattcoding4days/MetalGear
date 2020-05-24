"""
Test code for the MetalGear package
test foxhound.py
"""

import unittest
from MetalGear.foxhound import main

class TestFoxHound(unittest.TestCase):
    def test_fox(self):
        print(f'{self.test_fox.__name__} =>')
        main()


if __name__ == '__main__':
    unittest.main()
