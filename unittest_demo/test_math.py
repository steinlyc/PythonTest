import unittest
from test_func import *


class TestMathFunc(unittest.TestCase):
    """Test mathfuc.py"""

    # def setUp(self):
    #     print("do something before test.Prepare environment.")

    # def tearDown(self):
    #     print("do something after test.Clean up.")

    #  所有case执行之前准备一次环境，并在所有case执行结束之后再清理环境
    @classmethod
    def setUpClass(cls):
        print("This setUpClass() method only called once.")

    @classmethod
    def tearDownClass(cls):
        print("This tearDownClass() method only called once too.")

    def test_add(self):
        """Test method add(a, b)"""
        self.skipTest("don't run this case")
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 2))

    def test_minus(self):
        """Test method minus(a, b)"""
        self.assertEqual(1, minus(3, 2))

    def test_multi(self):
        """Test method multi(a, b)"""
        self.assertEqual(6, multi(2, 3))

    def test_divide(self):
        """Test method divide(a, b)"""
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(2.5, divide(5, 2))


if __name__ == '__main__':
    unittest.main(verbosity=2)
