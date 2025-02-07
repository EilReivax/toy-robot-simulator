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

        def test_invalid_positions(self):
            """Ensure out-of-bounds positions return False."""
            self.assertFalse(self.tabletop.is_valid_position(-1, 0))  # Negative
            self.assertFalse(self.tabletop.is_valid_position(5, 5))  # Outside grid
            self.assertFalse(self.tabletop.is_valid_position(10, 10))  # Way out

if __name__ == "__main__":
    unittest.main()
