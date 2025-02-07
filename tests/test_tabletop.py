import unittest
from tabletop import Tabletop

class TestTabletop(unittest.TestCase):

    def setUp(self):
        """Setup a fresh Tabletop before each test."""
        self.tabletop = Tabletop(5, 5)

    def test_valid_positions(self):
        """Ensure valid positions return True."""
        self.assertTrue(self.tabletop.is_valid_position(0, 0))
        self.assertTrue(self.tabletop.is_valid_position(4, 4))

if __name__ == "__main__":
    unittest.main()
