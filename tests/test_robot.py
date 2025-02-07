import unittest
from robot import Robot
from tabletop import Tabletop

class TestRobot(unittest.TestCase):

    def setUp(self):
        """Setup a fresh Robot and Tabletop before each test."""
        self.tabletop = Tabletop(5, 5)
        self.robot = Robot()

    def test_initial_state(self):
        """Test that the robot starts unplaced."""
        self.assertFalse(self.robot.is_placed())
        self.assertIsNone(self.robot.x)
        self.assertIsNone(self.robot.y)
        self.assertIsNone(self.robot.facing)

    def test_valid_place(self):
        """Test placing the robot in a valid position."""
        self.robot.place(0, 0, "NORTH", self.tabletop)
        self.assertTrue(self.robot.is_placed())
        self.assertEqual(self.robot.x, 0)
        self.assertEqual(self.robot.y, 0)
        self.assertEqual(self.robot.facing, "NORTH")

    def test_invalid_place(self):
        """Test placing the robot out of bounds."""
        self.robot.place(6, 6, "NORTH", self.tabletop)  # Out of bounds
        self.assertFalse(self.robot.is_placed())  # Should not be placed

    def test_move_valid(self):
        """Test moving the robot within bounds."""
        self.robot.place(0, 0, "NORTH", self.tabletop)
        self.robot.move(self.tabletop)
        self.assertEqual((self.robot.x, self.robot.y), (0, 1))

    def test_move_invalid(self):
        """Test moving the robot off the edge."""
        self.robot.place(0, 4, "NORTH", self.tabletop)
        self.robot.move(self.tabletop)  # Should not move past (0,4)
        self.assertEqual((self.robot.x, self.robot.y), (0, 4))

if __name__ == "__main__":
    unittest.main()
