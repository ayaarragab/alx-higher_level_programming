#!/usr/bin/python3
"""
This is the testing  for the Rectangle model class
"""
import pycodestyle
from models.base import Base
import unittest
from models.rectangle import Rectangle
from models.square import Square
import os

# Raises
# Make test fails till it passes
# Test error messages!
# Each error type
# test for line #!/usr/bin/python3

"""testing module class for Rectangle
"""


class test_pycodestyle(unittest.TestCase):
    "test that we conform to PEP-8"
    def test_checking(self):
        style = pycodestyle.StyleGuide(quit=True)
        result = style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
        print(result)
