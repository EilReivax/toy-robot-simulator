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

if __name__ == "__main__":
    unittest.main()
