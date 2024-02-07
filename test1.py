import unittest
import PYstrings_PythonCore
#from PythonPractise import PYstrings_PythonCore
#target = __import__("PYstrings_PythonCore.py")
#writelower = target.writelower

class TestString(unittest.TestCase):
    def test_program(self):
        """
        Test
        """
        target = PYstrings_PythonCore
        writelower = target.writelower
        data = "piyyyyY"
        result = writelower(data)
        self.assertEqual(result, False)
if __name__ == '__main__':
    unittest.main()
