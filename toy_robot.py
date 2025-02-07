from tabletop import Tabletop

class ToyRobot:
    """A class representing a robot and its commands (functions)."""

    DIRECTIONS = ['NORTH', 'EAST', 'SOUTH', 'WEST']

    def __init__(self):
        self.x = None
        self.y = None
        self.facing = None

    def is_placed(self):
        """Check if the robot is placed on the tabletop."""
        return self.x is not None and self.y is not None and self.facing is not None

    def place(self, x, y, facing, tabletop):
        """Place the robot on the tabletop if within bounds."""
        if tabletop.is_valid_position(x, y) and facing in self.DIRECTIONS:
            self.x = x
            self.y = y
            self.facing = facing

    def move(self, tabletop):
        """Move the robot one step in the direction it is facing, if within bounds."""
        if not self.is_placed():
            return # Ignore command if not placed

        move_offsets = {"NORTH": (0, 1), "EAST": (1, 0), "SOUTH": (0, -1), "WEST": (-1, 0)}
        dx, dy = move_offsets[self.facing]
        new_x, new_y = self.x + dx, self.y + dy

        if tabletop.is_valid_position(new_x, new_y):
            self.x, self.y = new_x, new_y

    def left(self):
        """Rotates the robot 90 degrees to the left by going through the list of directions."""
        if self.is_placed():
            current_index = self.DIRECTIONS.index(self.facing)
            self.facing = self.DIRECTIONS[(current_index - 1) % len(self.DIRECTIONS)]

    def right(self):
        """Rotates the robot 90 degrees to the right by going through the list of directions."""
        if self.is_placed():
            current_index = self.DIRECTIONS.index(self.facing)
            self.facing = self.DIRECTIONS[(current_index + 1) % len(self.DIRECTIONS)]

    def report(self):
        """Reports the current position and direction of the robot."""
        if not self.is_placed():
            return "Robot not placed yet."
        else:
            return f"{self.x},{self.y},{self.facing}"