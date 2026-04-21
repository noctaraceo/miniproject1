import main
import unittest

class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(main.add(2, 3), 5)
    def test_sub(self):
        self.assertEqual(main.subtract(8,67), -59)
    def test_multypily(self):
        self.assertEqual(main.multiply(4, 5), 20)
    def test_subtract_type_error(self):
        with self.assertRaises(TypeError):
            main.subtract("hello", 5)
    def test_multiply_type_error(self):
        with self.assertRaises(TypeError):
            main.multiply("hello", 5)

    def test_add_type_error(self):
        with self.assertRaises(TypeError):
            main.add("hello", 5)
if __name__ == '__main__': 
    unittest.main()