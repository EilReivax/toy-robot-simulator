class Robot:
    """A class representing a robot and its commands (functions)."""

    DIRECTIONS = ['NORTH', 'EAST', 'SOUTH', 'WEST']

    def __init__(self):
        """Initialize the Robot with no position or direction."""
        self.x = None
        self.y = None
        self.facing = None

    def is_placed(self):
        """Check if the robot is placed on the tabletop."""
        return self.x is not None and self.y is not None and self.facing is not None

    def place(self, x, y, facing, tabletop):
        """Place the robot on the tabletop if within bounds."""
        if self.is_placed():
            print("Robot already placed.")
            return # Ignore command if robot already placed

        if tabletop.is_valid_position(x, y) and facing in self.DIRECTIONS:
            self.x = x
            self.y = y
            self.facing = facing
        else:
            print("Invalid position, ignoring command.")

    def move(self, tabletop):
        """
        Move the robot one step in the direction it is facing, if within bounds.

        Args:
            tabletop (Tabletop): The tabletop object to check valid positions.
        """
        if not self.is_placed():
            return # Ignore command if not placed

        # Define movement offsets for each direction
        move_offsets = {"NORTH": (0, 1), "EAST": (1, 0), "SOUTH": (0, -1), "WEST": (-1, 0)}
        dx, dy = move_offsets[self.facing]
        new_x, new_y = self.x + dx, self.y + dy

        # Check if the new position is valid before moving
        if tabletop.is_valid_position(new_x, new_y):
            self.x, self.y = new_x, new_y
        else:
            print("Invalid move, ignoring command.")

    def left(self):
        """
        Rotate the robot 90 degrees to the left (counter-clockwise).
        """
        if not self.is_placed():
            return # Ignore command if not placed

        # Find the current direction index and rotate left
        current_index = self.DIRECTIONS.index(self.facing)
        self.facing = self.DIRECTIONS[(current_index - 1) % len(self.DIRECTIONS)]

    def right(self):
        """
        Rotate the robot 90 degrees to the right (clockwise).
        """
        if not self.is_placed():
            return # Ignore command if not placed

        # Find the current direction index and rotate right
        current_index = self.DIRECTIONS.index(self.facing)
        self.facing = self.DIRECTIONS[(current_index + 1) % len(self.DIRECTIONS)]

    def report(self):
        """
        Report the current position and direction of the robot.

        Returns:
            str: A string representation of the robot's position and facing direction,
                 or a message if the robot is not placed.
        """
        if self.is_placed():
            return f"{self.x},{self.y},{self.facing}"
        else:
            return "Robot not placed yet."