import main
import unittest

class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(main.add(2, 3), 5)
    def test_sub(self):
        self.assertEqual(main.subtract(8,67), -59)
        
    
if __name__ == '__main__': 
    unittest.main()