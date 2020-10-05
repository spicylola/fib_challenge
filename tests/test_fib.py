import unittest
from fib_challenge import app

class TestFibonacci(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
       pass

  @classmethod
  def tearDownClass(cls):
       pass

  def setUp(self):
      # creates a test client
      self.app = app.test_client()
      self.app.testing = True

  def tearDown(self):
    pass

  def test_calculate_fibonacci(self):
      response = self.app.get('/calculate_fibonacci?num=4')
      assert response.status_code == 200
      assert response.data.decode() == "The fibonacci sequence is [0, 1, 1, 2, 3] for the number: 4"

  def test_invalid_integer(self):
      response = self.app.get('/calculate_fibonacci?num=NotAnInt')
      assert response.status_code == 400

  def test_null_integer(self):
      response = self.app.get('/calculate_fibonacci?num=')
      assert response.status_code == 400

# runs the unit tests in the module
if __name__ == '__main__':
  unittest.main()

