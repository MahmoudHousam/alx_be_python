import unittest
import pytest
from simple_calculator import SimpleCalculator


class test_simple_calculator_class(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        with pytest.raises(TypeError):
            self.calc.add("2", 4)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(13, 4), 9)
        with pytest.raises(TypeError):
            self.calc.subtract("2", 4)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 9), 36)

    def test_divide(self):
        self.assertEqual(self.calc.divide(36, 9), 4)
        with pytest.raises(ZeroDivisionError):
            self.calc.divide(36, 0)


if __name__ == "__main__":
    unittest.main()
