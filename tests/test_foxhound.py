"""
Test code for the MetalGear
package
"""
import unittest
from MetalGear import foxhound

class TestFoxHound(unittest.TestCase):
    @staticmethod
    def test_fox():
        # call foxound
        foxhound.main()


if __name__ == '__main__':
    unittest.main()
