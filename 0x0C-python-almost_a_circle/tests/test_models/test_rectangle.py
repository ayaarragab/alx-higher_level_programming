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


class test_documentations(unittest.TestCase):
    """Class for testing documentations
    """
    def test_first_line(self):
        """Test for first line
        """
        with open('models/base.py', 'r', encoding="UTF-8") as f:
            line = f.readline()
            self.assertEqual('#!/usr/bin/python3' in line, True)

    def test_module_doc(self):
        "module documentation test"
        booll = len(Rectangle.__module__.__doc__) > 1
        self.assertEqual(booll, True)

    def test_class_doc(self):
        "class documentation test"
        booll = len(Rectangle.__doc__) > 1
        self.assertEqual(booll, True)

    def test_method1_doc(self):
        "__init__ documentation test"
        booll = len(Rectangle.__init__.__doc__) > 1
        self.assertEqual(booll, True)

    def test_method2_doc(self):
        "to_json_string documentation test"
        booll = len(Rectangle.width.getter.__doc__) > 1
        self.assertEqual(booll, True)

    def test_method3_doc(self):
        "save_to_file documentation test"
        booll = len(Rectangle.width.setter.__doc__) > 1
        self.assertEqual(booll, True)

    def test_method4_doc(self):
        "from_json_string documentation test"
        booll = len(Rectangle.height.getter.__doc__) > 1
        self.assertEqual(booll, True)

    def test_method5_doc(self):
        "create documentation test"
        booll = len(Rectangle.height.setter.__doc__) > 1
        self.assertEqual(booll, True)

    def test_method6_doc(self):
        "load_from_file documentation test"
        booll = len(Rectangle.x.getter.__doc__) > 1
        self.assertEqual(booll, True)

    def test_method7_doc(self):
        "load_from_file documentation test"
        booll = len(Rectangle.x.setter.__doc__) > 1
        self.assertEqual(booll, True)

    def test_method8_doc(self):
        "load_from_file documentation test"
        booll = len(Rectangle.y.setter.__doc__) > 1
        self.assertEqual(booll, True)

    def test_method9_doc(self):
        "load_from_file documentation test"
        booll = len(Rectangle.y.getter.__doc__) > 1
        self.assertEqual(booll, True)

    def test_method10_doc(self):
        "load_from_file documentation test"
        booll = len(Rectangle.area.__doc__) > 1
        self.assertEqual(booll, True)

    def test_method12_doc(self):
        "load_from_file documentation test"
        booll = len(Rectangle.display.__doc__) > 1
        self.assertEqual(booll, True)

    def test_method13_doc(self):
        "load_from_file documentation test"
        booll = len(Rectangle.__str__.__doc__) > 1
        self.assertEqual(booll, True)

    def test_method14_doc(self):
        "load_from_file documentation test"
        booll = len(Rectangle.update.__doc__) > 1
        self.assertEqual(booll, True)

    def test_method15_doc(self):
        "load_from_file documentation test"
        booll = len(Rectangle.to_dictionary.__doc__) > 1
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


class test_width(unittest.TestCase):
    """testing width gettter
    """
    def test_basic(self):
        """Basic testing
        """
        obj = Rectangle(10, 20, 30, 40, 50)
        self.assertEqual(obj.width, 10)

    def test_negative_number(self):
        """Basic testing
        """
        with self.assertRaises(
            ValueError, msg='ValueError: width must be > 0'
        ):
            obj = Rectangle(-10, 20, 30, 40, 50)

    def test_different_type_float(self):
        """Basic testing
        """
        with self.assertRaises(
            TypeError, msg='width must be an integer'
        ):
            obj = Rectangle(10.4, 20, 30, 40, 50)

    def test_different_type_str(self):
        """Basic testing
        """
        with self.assertRaises(
            TypeError, msg='width must be an integer'
        ):
            obj = Rectangle("str", 20, 30, 40, 50)

    def test_different_type_bool(self):
        """Basic testing
        """
        with self.assertRaises(
            TypeError, msg='width must be an integer'
        ):
            obj = Rectangle(True, 20, 30, 40, 50)

    def test_different_type_iteratives(self):
        """Basic testing
        """
        with self.assertRaises(
            TypeError, msg='width must be an integer'
        ):
            obj = Rectangle([10.4], 20, 30, 40, 50)
        with self.assertRaises(
            TypeError, msg='width must be an integer'
        ):
            obj = Rectangle((10.4, 9), 20, 30, 40, 50)
        with self.assertRaises(
            TypeError, msg='width must be an integer'
        ):
            obj = Rectangle({10.4, 9}, 20, 30, 40, 50)

    def test_for_zero(self):
        """Basic testing
        """
        with self.assertRaises(
            ValueError, msg='ValueError: width must be > 0'
        ):
            obj = Rectangle(0, 20, 30, 40, 50)


if __name__ == '__main__':
    unittest.TestCase()
