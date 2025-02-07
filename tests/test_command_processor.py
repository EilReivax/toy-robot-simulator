import unittest
from command_processor import CommandProcessor
from robot import Robot
from tabletop import Tabletop

class TestCommandProcessor(unittest.TestCase):

    def setUp(self):
        """Setup a fresh robot and tabletop before each test."""
        self.tabletop = Tabletop(5, 5)
        self.robot = Robot()
        self.processor = CommandProcessor(self.tabletop, self.robot)

    def test_ignore_commands_before_place(self):
        """Ensure commands are ignored before PLACE."""
        commands = ["MOVE", "LEFT", "RIGHT", "REPORT"]
        self.processor.process_commands(commands)
        self.assertEqual(self.robot.report(), "Robot not placed yet.")

    def test_ignore_blank_lines(self):
        """Test that blank lines are ignored."""
        commands = ["", "  ", "\n", "PLACE 0,0,NORTH", "", "MOVE", "  ", "REPORT"]
        self.processor.process_commands(commands)
        self.assertEqual(self.robot.report(), "0,1,NORTH")

    def test_valid_place_and_move(self):
        """Ensure PLACE and MOVE commands work correctly."""
        commands = ["PLACE 0,0,NORTH", "MOVE", "REPORT"]
        self.processor.process_commands(commands)
        self.assertEqual(self.robot.report(), "0,1,NORTH")

    def test_invalid_place_command(self):
        """Ensure invalid PLACE commands are ignored."""
        commands = ["PLACE invalid", "REPORT"]
        self.processor.process_commands(commands)
        self.assertEqual(self.robot.report(), "Robot not placed yet.")

if __name__ == "__main__":
    unittest.main()
