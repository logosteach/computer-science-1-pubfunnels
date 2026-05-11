# die.py
from random import randint


class Die:
    """Represents a single die used in many board games.
    
    The die can have any number of sides (default is 6).
    """

    def __init__(self, sides: int = 6):
        """Initialize a new die.
        
        Args:
            sides (int): Number of sides on the die. Must be >= 2.
            
        Raises:
            ValueError: If sides is not an integer or is less than 2.
        """
        if not isinstance(sides, int) or sides < 2:
            raise ValueError("Number of sides must be an integer >= 2")
        
        self.sides = sides
        self.current_side = None   # No value until rolled
        self.roll()                # Start with a rolled value

    def roll(self):
        """Roll the die and update the current side.
        
        Returns:
            int: The new value showing on the die.
        """
        self.current_side = randint(1, self.sides)
        return self.current_side

    def get_current_side(self):
        """Return the current side showing on the die.
        
        If the die has not been rolled yet, it will roll automatically.
        """
        if self.current_side is None:
            self.roll()
        return self.current_side

    def __str__(self):
        """Return a nice string representation of the die."""
        return f"Die({self.sides} sides) showing: {self.current_side}"
