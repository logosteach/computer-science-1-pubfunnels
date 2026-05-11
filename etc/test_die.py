import unittest
from die import Die

class TestDie(unittest.TestCase):
    """Test cases for the Die class."""

    def setUp(self):
        """Set up a fresh Die object before each test."""
        self.d6 = Die(6)      # Standard 6-sided die
        self.d10 = Die(10)    # 10-sided die
        self.d20 = Die(20)    # 20-sided die

    def tearDown(self):
        """Clean up after each test (optional but good practice)."""
        # Currently no resources to clean up, but we keep the method for consistency
        pass

    # ==================== Initialization Tests ====================

    def test_default_sides_is_six(self):
        """Test that a die created without arguments has 6 sides."""
        default_die = Die()
        self.assertEqual(default_die.sides, 6)

    def test_sides_is_set_correctly(self):
        """Test that the sides attribute is set to the passed value."""
        self.assertEqual(self.d6.sides, 6)
        self.assertEqual(self.d10.sides, 10)
        self.assertEqual(self.d20.sides, 20)

    def test_raises_error_for_invalid_sides(self):
        """Test that creating a die with invalid sides raises ValueError."""
        with self.assertRaises(ValueError):
            Die(1)      # Less than 2
        
        with self.assertRaises(ValueError):
            Die(0)
        
        with self.assertRaises(ValueError):
            Die(-5)
        
        with self.assertRaises(ValueError):
            Die("6")    # Not an integer

    # ==================== Rolling Tests ====================

    def test_roll_returns_integer(self):
        """Test that roll() returns an integer."""
        result = self.d6.roll()
        self.assertIsInstance(result, int)

    def test_roll_value_is_within_range(self):
        """Test that the rolled value is between 1 and number of sides (inclusive)."""
        for _ in range(50):                     # Roll many times to be confident
            roll = self.d6.roll()
            self.assertGreaterEqual(roll, 1)
            self.assertLessEqual(roll, 6)

        for _ in range(30):
            roll = self.d20.roll()
            self.assertGreaterEqual(roll, 1)
            self.assertLessEqual(roll, 20)

    def test_current_side_is_updated_after_roll(self):
        """Test that current_side is updated when roll() is called."""
        old_value = self.d6.current_side
        self.d6.roll()
        self.assertNotEqual(self.d6.current_side, old_value)

    # ==================== get_current_side Tests ====================

    def test_get_current_side_returns_integer(self):
        """Test that get_current_side() returns an integer."""
        result = self.d6.get_current_side()
        self.assertIsInstance(result, int)

    def test_get_current_side_is_within_range(self):
        """Test that get_current_side() returns a value in valid range."""
        side = self.d6.get_current_side()
        self.assertGreaterEqual(side, 1)
        self.assertLessEqual(side, self.d6.sides)

    # ==================== String Representation Tests ====================

    def test_str_representation(self):
        """Test the __str__ method produces expected output."""
        die_str = str(self.d6)
        self.assertIn(f"Die({self.d6.sides} sides)", die_str)
        self.assertIn("showing:", die_str)

    def test_str_shows_current_side(self):
        """Test that __str__ includes the actual current side value."""
        current = self.d6.current_side
        die_str = str(self.d6)
        self.assertIn(str(current), die_str)

if __name__ == "__main__":
    unittest.main(verbosity=2)
