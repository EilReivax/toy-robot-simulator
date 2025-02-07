class Tabletop:
    """
    Represents the tabletop on which the robot moves.
    """

    def __init__(self, width, height):
        """
        Initialize the Tabletop with given dimensions.

        Args:
            width (int): The width of the tabletop.
            height (int): The height of the tabletop.
        """
        self.width = width
        self.height = height

    def is_valid_position(self, x, y):
        """
        Check if a given position is within the tabletop boundaries.

        Args:
            x (int): The x-coordinate to check.
            y (int): The y-coordinate to check.

        Returns:
            bool: True if the position is valid, False otherwise.
        """
        return 0 <= x < self.width and 0 <= y < self.height