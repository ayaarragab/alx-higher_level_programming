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
from io import StringIO
from unittest.mock import patch


# Raises
# Make test fails till it passes
# Test error messages!
# Each error type
# test for line #!/usr/bin/python3

"""testing module class for square
"""


class test_pycodestyle(unittest.TestCase):
    "test that we conform to PEP-8"
    def test_checking(self):
        style = pycodestyle.StyleGuide(quit=True)
        result = style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
        print(result)


class test_documentations(unittest.TestCase):
    """Class for testing documentations
    """
    def test_first_line(self):
        """Test for first line
        """
        with open('models/square.py', 'r', encoding="UTF-8") as f:
            line = f.readline()
            self.assertEqual('#!/usr/bin/python3' in line, True)

    def test_module_doc(self):
        "module documentation test"
        booll = len(Square.__module__.__doc__) > 1
        self.assertEqual(booll, True)

    def test_class_doc(self):
        "class documentation test"
        booll = len(Square.__doc__) > 1
        self.assertEqual(booll, True)

    def test_method1_doc(self):
        "__init__ documentation test"
        booll = len(Square.__init__.__doc__) > 1
        self.assertEqual(booll, True)

    def test_method2_doc(self):
        "to_json_string documentation test"
        booll = len(Square.size.getter.__doc__) > 1
        self.assertEqual(booll, True)

    def test_method3_doc(self):
        "save_to_file documentation test"
        booll = len(Square.size.setter.__doc__) > 1
        self.assertEqual(booll, True)

    def test_method6_doc(self):
        "load_from_file documentation test"
        booll = len(Square.x.getter.__doc__) > 1
        self.assertEqual(booll, True)

    def test_method7_doc(self):
        "load_from_file documentation test"
        booll = len(Square.x.setter.__doc__) > 1
        self.assertEqual(booll, True)

    def test_method8_doc(self):
        "load_from_file documentation test"
        booll = len(Square.y.setter.__doc__) > 1
        self.assertEqual(booll, True)

    def test_method9_doc(self):
        "load_from_file documentation test"
        booll = len(Square.y.getter.__doc__) > 1
        self.assertEqual(booll, True)

    def test_method10_doc(self):
        "load_from_file documentation test"
        booll = len(Square.area.__doc__) > 1
        self.assertEqual(booll, True)

    def test_method12_doc(self):
        "load_from_file documentation test"
        booll = len(Square.display.__doc__) > 1
        self.assertEqual(booll, True)

    def test_method13_doc(self):
        "load_from_file documentation test"
        booll = len(Square.__str__.__doc__) > 1
        self.assertEqual(booll, True)

    def test_method14_doc(self):
        "load_from_file documentation test"
        booll = len(Square.update.__doc__) > 1
        self.assertEqual(booll, True)

    def test_method15_doc(self):
        "load_from_file documentation test"
        booll = len(Square.to_dictionary.__doc__) > 1
        self.assertEqual(booll, True)


class test__init__(unittest.TestCase):
    """Test __init__
    """
    def test_init(self):
        """(__init__) - making object with no id -same class type-"""
        obj1 = Base()
        obj2 = Base()

        self.assertEqual(obj2.id, obj1.id + 1)

    def test_init_diff(self):
        """making object with no id -different classes type
        """
        obj1 = Rectangle(21, 2)
        obj2 = Square(9, 9)
        obj3 = Base()
        self.assertEqual(obj2.id, obj1.id + 1)
        self.assertEqual(obj3.id, obj2.id + 1)

    def test_give_id(self):
        """test_give_id
        """
        obj1 = Rectangle(21, 2, 10, 10, 109)
        obj2 = Square(9, 9, 2, 101)
        obj3 = Base(102)
        self.assertEqual(obj1.id, 109)
        self.assertEqual(obj2.id, 101)
        self.assertEqual(obj3.id, 102)

    def test_None(self):
        """Test for giving none to
        """
        obj1 = Base(None)
        obj2 = Base(None)
        self.assertEqual(obj2.id, obj1.id + 1)

    def test_for_direct_assignment(self):
        """Test for assignment of pulic id
        """
        obj = Base()
        obj.id = 10
        self.assertEqual(obj.id, 10)

    def test_for_string_id(self):
        """Test for string id
        """
        obj = Square(2, 4, 5, "Aya")
        self.assertEqual(obj.id, "Aya")

    def test_for_boolean(self):
        """Test for boolean id
        """
        obj = Square(2, 4, 5, True)
        self.assertEqual(obj.id, 1)

    def test_for_dict(self):
        """testing for iteratives"""
        obj = Base()
        Dic = {"Key": 'val'}
        obj.id = Dic
        self.assertEqual(obj.id, Dic)

    def test_for_tup(self):
        """Tuple as id
        """
        obj = Base()
        tup = (0, 3, 4)
        obj.id = tup
        self.assertEqual(obj.id, tup)

    def test_for_list(self):
        """Testing for lists"""
        listII = [1, 3, 5, 7]
        obj = Base(listII)
        self.assertEqual(obj.id, listII)

    def test_for_set(self):
        """Test for set"""
        obj = Base()
        set4 = {2, 5, 6}
        obj.id = set4
        self.assertEqual(obj.id, set4)

    def test_more_than_1_arg(self):
        """test_more_than_1_arg
        """
        with self.assertRaises(TypeError):
            Base(10, 4)


class test_size(unittest.TestCase):
    """testing width gettter
    """
    def test_basic(self):
        """Basic testing
        """
        obj = Square(10, 30, 40, 50)
        self.assertEqual(obj.size, 10)

    def test_negative_number(self):
        """Basic testing
        """
        with self.assertRaises(
            ValueError, msg='ValueError: width must be > 0'
        ):
            obj = Square(-10, 30, 40, 50)

    def test_different_type_float(self):
        """Basic testing
        """
        with self.assertRaises(
            TypeError, msg='width must be an integer'
        ):
            obj = Square(10.4, 30, 40, 50)

    def test_different_type_str(self):
        """Basic testing
        """
        with self.assertRaises(
            TypeError, msg='width must be an integer'
        ):
            obj = Square("str", 30, 40, 50)

    def test_different_type_bool(self):
        """Basic testing
        """
        with self.assertRaises(
            TypeError, msg='width must be an integer'
        ):
            obj = Square(True, 30, 40, 50)

    def test_different_type_iteratives(self):
        """Basic testing
        """
        with self.assertRaises(
            TypeError, msg='width must be an integer'
        ):
            obj = Square([10.4], 30, 40, 50)
        with self.assertRaises(
            TypeError, msg='width must be an integer'
        ):
            obj = Square((10.4, 9), 30, 40, 50)
        with self.assertRaises(
            TypeError, msg='width must be an integer'
        ):
            obj = Square({10.4, 9}, 30, 40, 50)

    def test_for_zero(self):
        """Basic testing
        """
        with self.assertRaises(
            ValueError, msg='ValueError: width must be > 0'
        ):
            obj = Rectangle(0, 30, 40, 50)

    def test_different_type_None(self):
        """Basic testing
        """
        with self.assertRaises(
            TypeError, msg='width must be an integer'
        ):
            obj = Rectangle(None, 30, 40, 50)


class test_x(unittest.TestCase):
    """Testing x getter
    """
    def test_basic(self):
        """Basic testing
        """
        obj = Square(10, 30, 40, 50)
        self.assertEqual(obj.x, 30)

    def test_negative_number(self):
        """Testing with a negative value
        """
        with self.assertRaises(
            ValueError, msg='ValueError: x must be >= 0'
        ):
            obj = Square(10, -30, 40, 50)

    def test_different_type_float(self):
        """Testing with a float value
        """
        with self.assertRaises(
            TypeError, msg='x must be an integer'
        ):
            obj = Square(10, 30.5, 40, 50)

    def test_different_type_str(self):
        """Testing with a string value
        """
        with self.assertRaises(
            TypeError, msg='x must be an integer'
        ):
            obj = Square(10, "str", 40, 50)

    def test_different_type_bool(self):
        """Testing with a boolean value
        """
        with self.assertRaises(
            TypeError, msg='x must be an integer'
        ):
            obj = Square(10, True, 40, 50)

    def test_different_type_iteratives(self):
        """Testing with iterable types
        """
        with self.assertRaises(
            TypeError, msg='x must be an integer'
        ):
            obj = Square(10, [30.4], 40, 50)
        with self.assertRaises(
            TypeError, msg='x must be an integer'
        ):
            obj = Square(10, (30.4, 9), 40, 50)
        with self.assertRaises(
            TypeError, msg='x must be an integer'
        ):
            obj = Square(10, {30.4, 9}, 40, 50)

    def test_different_type_None(self):
        """Testing with None
        """
        with self.assertRaises(
            TypeError, msg='x must be an integer'
        ):
            obj = Square(10, None, 40, 50)


class test_y(unittest.TestCase):
    """Testing y getter
    """
    def test_basic(self):
        """Basic testing
        """
        obj = Square(10, 30, 40, 50)
        self.assertEqual(obj.y, 40)

    def test_negative_number(self):
        """Testing with a negative value
        """
        with self.assertRaises(
            ValueError, msg='ValueError: y must be >= 0'
        ):
            obj = Square(10, 30, -40, 50)

    def test_different_type_float(self):
        """Testing with a float value
        """
        with self.assertRaises(
            TypeError, msg='y must be an integer'
        ):
            obj = Square(10, 30, 40.5, 50)

    def test_different_type_str(self):
        """Testing with a string value
        """
        with self.assertRaises(
            TypeError, msg='y must be an integer'
        ):
            obj = Square(10, 30, "str", 50)

    def test_different_type_bool(self):
        """Testing with a boolean value
        """
        with self.assertRaises(
            TypeError, msg='y must be an integer'
        ):
            obj = Square(10, 30, True, 50)

    def test_different_type_iteratives(self):
        """Testing with iterable types
        """
        with self.assertRaises(
            TypeError, msg='y must be an integer'
        ):
            obj = Square(10, 30, [40.4])
        with self.assertRaises(
            TypeError, msg='y must be an integer'
        ):
            obj = Square(10, 30, (40.4, 9))
        with self.assertRaises(
            TypeError, msg='y must be an integer'
        ):
            obj = Square(10, 30, {40.4, 9})

    def test_different_type_None(self):
        """Testing with None
        """
        with self.assertRaises(
            TypeError, msg='y must be an integer'
        ):
            obj = Square(10, 30, None)


class test_area(unittest.TestCase):
    """Test cases for area
    """
    def test_basic(self):
        """Basic testing
        """
        rec = Square(6, 10, 11)
        self.assertEqual(rec.area(), 36)


class test_display(unittest.TestCase):

    def test_printed_string_only_w_h(self):
        """ Tests display function with width and height only
        """
        obj = Square(4, 2)
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            obj.display()
            printed_output = mock_stdout.getvalue().strip()
        pattern = '####\n  ####\n  ####\n  ####'
        self.assertEqual(printed_output, pattern)

    def test_printed_string_xy(self):
        """ Tests display function with x and y values
        """
        obj = Square(4, 2, 1, 1)  # Size=4, x=2, y=1
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            obj.display()
            printed_output = mock_stdout.getvalue()
        pattern = '\n  ####\n  ####\n  ####\n  ####\n'
        self.assertEqual(printed_output, pattern)

    def test_printed_string_y(self):
        """ Tests display function with x and y values
        """
        obj = Square(4, 2, 0, 1)  # Size=4, x=2, y=0
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            obj.display()
            printed_output = mock_stdout.getvalue()
        pattern = '  ####\n  ####\n  ####\n  ####\n'
        self.assertEqual(printed_output, pattern)

    def test_printed_string_x(self):
        """ Tests display function with x and y values
        """
        obj = Square(4, 0, 1, 0)  # Size=4, x=0, y=1
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            obj.display()
            printed_output = mock_stdout.getvalue()
        pattern = '\n####\n####\n####\n####\n'
        self.assertEqual(printed_output, pattern)


class test_str_square(unittest.TestCase):

    def test_str_method(self):
        """ Tests the __str__ method
        """
        obj = Square(4, 2, 1, 1)
        expected_output = "[Square] (1) 2/1 - 4"
        self.assertEqual(str(obj), expected_output)


class test_update(unittest.TestCase):

    def test_update_args(self):
        """ Tests update method with positional arguments
        """
        obj = Square(4, 2, 1, 1)
        obj.update(2, 3, 4, 5)
        self.assertEqual(obj.id, 2)
        self.assertEqual(obj.size, 3)
        self.assertEqual(obj.x, 4)
        self.assertEqual(obj.y, 5)

    def test_update_kwargs(self):
        """ Tests update method with keyword arguments
        """
        obj = Square(4, 2, 1, 1)
        obj.update(id=2, size=3, x=4, y=5)
        self.assertEqual(obj.id, 2)
        self.assertEqual(obj.size, 3)
        self.assertEqual(obj.x, 4)
        self.assertEqual(obj.y, 5)

    def test_update_mix_args_kwargs(self):
        """ Tests update method with a mix of args and kwargs
        """
        obj = Square(4, 2, 1, 1)
        obj.update(2, size=3, y=5)
        self.assertEqual(obj.id, 2)
        self.assertEqual(obj.size, 3)
        self.assertEqual(obj.x, 2)
        self.assertEqual(obj.y, 5)

    def test_update_no_args_kwargs(self):
        """ Tests update method with no args or kwargs
        """
        obj = Square(4, 2, 1, 1)
        obj.update()
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.size, 4)
        self.assertEqual(obj.x, 2)
        self.assertEqual(obj.y, 1)

    def test_update_args_overflow(self):
        """ Tests update method with too many positional arguments
        """
        obj = Square(4, 2, 1, 1)
        obj.update(2, 3, 4, 5, 6)  # Should ignore the last one
        self.assertEqual(obj.id, 2)
        self.assertEqual(obj.size, 3)
        self.assertEqual(obj.x, 4)
        self.assertEqual(obj.y, 5)


class test_to_dictionary(unittest.TestCase):
    """Tests to dictionary function
    """
    def test_basic(self):
        recdict = Square(2, 4, 5, 6).to_dictionary()
        dicc = {'size': 2, 'x': 4, 'y': 5, 'id': 6}
        self.assertEqual(recdict.items(), dicc.items())


if __name__ == '__main__':
    unittest.TestCase()
