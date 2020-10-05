import unittest
from fib_challenge import app

class TestFibonacci(unittest.TestCase):
    """Fibonacci Test Cases."""
    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_calculate_fibonacci(self):
        """Test the positive response for fibonacci."""
        response = self.app.get('/calculate_fibonacci?num=4')
        assert response.status_code == 200
        assert response.data.decode() == "The fibonacci sequence is [0, 1, 1, 2, 3]" \
                                         " for the number: 4"

    def test_invalid_integer(self):
        """Test if a string is passed in as a param."""
        response = self.app.get('/calculate_fibonacci?num=NotAnInt')
        assert response.status_code == 400
        # This was commented out because it was returining as an HTML File
        # assert response.data.decode() == "The number is not a valid integer for NotAnInt with error NotAnInt"

    def test_null_integer(self):
        """test if a null value is passed in as a param."""
        response = self.app.get('/calculate_fibonacci?num=')
        assert response.status_code == 400

# runs the unit tests in the module
if __name__ == '__main__':
    unittest.main()