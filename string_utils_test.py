import unittest
import os
from string_utils import StringUtils


class StringUtilsTest(unittest.TestCase):
    def setUp(self):
        self.stringUtils = StringUtils("")

    def test_toUpper(self):
        self.stringUtils.string = "hello world"
        result = self.stringUtils.toUpper()
        self.assertEqual(result, "HELLO WORLD")

    def test_toAlternate(self):
        self.stringUtils.string = "hello world"
        result = self.stringUtils.toAlternate()
        self.assertEqual(result, "hElLo wOrLd")

    def test_generateCSV(self):
        self.stringUtils.string = "hello world"
        csv_file = self.stringUtils.generateCSV("testing_string_utils.csv")
        expected_csv_content = "h,e,l,l,o, ,w,o,r,l,d"

        with open(csv_file, "r") as file:
            csv_content = file.read()
        
        os.remove("testing_string_utils.csv") 
        self.assertEqual(csv_content, expected_csv_content)


if __name__ == "__main__":
    unittest.main()