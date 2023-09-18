#!/usr/bin/python3
"""
This is the testin  for the base model class
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

"""testing module class for base
"""


class test_pycodestyle(unittest.TestCase):
    "test that we conform to PEP-8"
    def test_checking(self):
        style = pycodestyle.StyleGuide(quit=True)
        result = style.check_files(['models/base.py'])
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
        booll = len(Base.__module__.__doc__) > 1
        self.assertEqual(booll, True)

    def test_class_doc(self):
        "class documentation test"
        booll = len(Base.__doc__) > 1
        self.assertEqual(booll, True)

    def test_method1_doc(self):
        "__init__ documentation test"
        booll = len(Base.__init__.__doc__) > 1
        self.assertEqual(booll, True)

    def test_method2_doc(self):
        "to_json_string documentation test"
        booll = len(Base.to_json_string.__doc__) > 1
        self.assertEqual(booll, True)

    def test_method3_doc(self):
        "save_to_file documentation test"
        booll = len(Base.save_to_file.__doc__) > 1
        self.assertEqual(booll, True)

    def test_method4_doc(self):
        "from_json_string documentation test"
        booll = len(Base.from_json_string.__doc__) > 1
        self.assertEqual(booll, True)

    def test_method5_doc(self):
        "create documentation test"
        booll = len(Base.create.__doc__) > 1
        self.assertEqual(booll, True)

    def test_method6_doc(self):
        "load_from_file documentation test"
        booll = len(Base.load_from_file.__doc__) > 1
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


class test_to_json_string(unittest.TestCase):
    """class for testing to_json_string
    """

    def test_to_json_string(self):
        """ testing test_to_json_string for only one dict
        """
        list_of_dicts = list()
        group_of_dicts = {"width": 10, "height": 5, "x": 1, "y": 0, "id": 1}
        list_of_dicts.append(group_of_dicts)
        str_json = '[{"width": 10, "height": 5, "x": 1, "y": 0, "id": 1}]'
        logic1 = Base.to_json_string(list_of_dicts) == str_json
        self.assertEqual(logic1, True)

    def test_to_json_string_more_than_one_dict(self):
        """ testing test_to_json_string for more than dict
        """
        list_of_dicts = list()
        group_of_dicts = {"width": 10, "height": 5, "x": 1, "y": 0, "id": 1}
        list_of_dicts.append(group_of_dicts)
        group_of2 = {"width": 130, "height": 51, "x": 14, "y": 3, "id": 9}
        list_of_dicts.append(group_of2)
        str_json = '[{"width": 10, "height": 5, "x": 1, "y": 0, "id": 1}, ' +\
                   '{"width": 130, "height": 51, "x": 14, "y": 3, "id": 9}]'
        logic = Base.to_json_string(list_of_dicts) == str_json
        self.assertEqual(logic, True)

    def test_for_empty_list(self):
        """Testing with normal inputs [Empty list]
        """
        self.assertEqual(Base.to_json_string([]), '[]')

    def test_for_empty_dict(self):
        """Edge cases - empty dictionary
        """
        self.assertEqual(Base.to_json_string([{}]), '[{}]')

    def test_for_None(self):
        """Edge cases - None
        """
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_for_square_2_dicts(self):
        """Testing this function with class square
        """
        square1 = Square(4, 7, 6, 5).to_dictionary()
        square2 = Square(5, 5, 5, 5).to_dictionary()
        json_data = Base.to_json_string([square1, square2])
        self.assertEqual(str, type(json_data))
        self.assertEqual(len(json_data), 76)

    def test_for_square_1_dict(self):
        """Testing this function with class square
        """
        square1 = Square(4, 7, 6, 5).to_dictionary()
        json_data = Base.to_json_string([square1])
        self.assertEqual(str, type(json_data))
        self.assertEqual(len(json_data), 38)

    def test_for_rectangle_1_dict(self):
        rectangle = Rectangle(4, 5, 1, 1).to_dictionary()
        json_data = Base.to_json_string([rectangle])
        self.assertEqual(str, type(json_data))
        self.assertEqual(len(json_data), 53)

    def test_for_rectangle_2_dicts(self):
        """Testing this function with class square
        """
        Rectangle1 = Rectangle(4, 7, 6, 5).to_dictionary()
        Rectangle2 = Rectangle(5, 5, 5, 5).to_dictionary()
        json_data = Base.to_json_string([Rectangle1, Rectangle1])
        self.assertEqual(str, type(json_data))
        self.assertEqual(len(json_data), 106)


class test_save_to_file(unittest.TestCase):
    """Test save_to_file function
    """

    def test_one_Sq(self):
        sq1 = Square(2, 3, 5)
        listOfObjs = [sq1]
        listOfObjs[0].__class__.save_to_file(listOfObjs)
        TrueFalse = os.path.exists(f'{listOfObjs[0].__class__.__name__}.json')
        self.assertTrue(TrueFalse)

    def test_one_Sq_len(self):
        sq1 = Square(2, 3, 5)
        listOfObjs = [sq1]
        listOfObjs[0].__class__.save_to_file(listOfObjs)
        filename = f'{listOfObjs[0].__class__.__name__}.json'
        with open(filename, 'r', encoding="UTF-8") as f:
            content = f.read()
            self.assertEqual(len(content), 39)

    def test_for_one_rec(self):
        """test_for_Normal_list
        """
        Rec1 = Rectangle(2, 3, 5)
        listOfObjs = [Rec1]
        listOfObjs[0].__class__.save_to_file(listOfObjs)
        TrueFalse = os.path.exists(f'{listOfObjs[0].__class__.__name__}.json')
        self.assertTrue(TrueFalse)

    def test_for_one_rec_len(self):
        """test_for_Normal_list
        """
        Rec1 = Rectangle(2, 3, 5)
        listOfObjs = [Rec1]
        listOfObjs[0].__class__.save_to_file(listOfObjs)
        filename = f'{listOfObjs[0].__class__.__name__}.json'
        with open(filename, 'r', encoding="UTF-8") as f:
            content = f.read()
            self.assertEqual(len(content), 53)

    def test_for_2Squares_list(self):
        """test_for_Normal_list
        """
        sq1 = Square(2, 3, 5)
        sq2 = Square(4, 10, 1)
        listOfObjs = [sq1, sq2]
        listOfObjs[0].__class__.save_to_file(listOfObjs)
        TrueFalse = os.path.exists(f'{listOfObjs[0].__class__.__name__}.json')
        self.assertTrue(TrueFalse)

    def test_for_2Squares_list_len(self):
        """test_for_Normal_list
        """
        sq1 = Square(2, 3, 5)
        sq2 = Square(4, 10, 1)
        listOfObjs = [sq1, sq2]
        listOfObjs[0].__class__.save_to_file(listOfObjs)
        filename = f'{listOfObjs[0].__class__.__name__}.json'
        with open(filename, 'r', encoding="UTF-8") as f:
            content = f.read()
            self.assertEqual(len(content), 79)

    def test_for_2Rectangle_list(self):
        """test_for_Normal_list
        """
        Rec1 = Rectangle(2, 3, 5)
        Rec2 = Rectangle(4, 10, 1)
        listOfObjs = [Rec1, Rec2]
        listOfObjs[0].__class__.save_to_file(listOfObjs)
        TrueFalse = os.path.exists(f'{listOfObjs[0].__class__.__name__}.json')
        self.assertTrue(TrueFalse)

    def test_for_2Rectangle_list(self):
        """test_for_Normal_list
        """
        Rec1 = Rectangle(2, 3, 5)
        Rec2 = Rectangle(4, 10, 1)
        listOfObjs = [Rec1, Rec2]
        listOfObjs[0].__class__.save_to_file(listOfObjs)
        filename = f'{listOfObjs[0].__class__.__name__}.json'
        with open(filename, 'r', encoding="UTF-8") as f:
            content = f.read()
            self.assertEqual(len(content), 107)

    def test_for_right_content(self):
        """Make sure that the file has
        the right content"""
        sq1 = Square(2, 3, 5)
        sq2 = Square(4, 10, 1)
        listOfDicts = [sq1.to_dictionary(), sq2.to_dictionary()]
        listOfObjs = [sq1, sq2]
        listOfObjs[0].__class__.save_to_file(listOfObjs)
        with open(f'{listOfObjs[0].__class__.__name__}.json', 'r') as f:
            content = f.read()
            self.assertEqual(content == Base.to_json_string(listOfDicts), True)

    def test_for_None_s(self):
        """Test by None
        """
        Base.save_to_file(None)
        if os.path.exists('Base.json'):
            with open('Base.json') as f:
                content = f.read()
        self.assertEqual(content, '[]')

    def test_for_empty_listt(self):
        """test_for_empty_listt"""
        Base.save_to_file([])
        if os.path.exists('Base.json'):
            with open('Base.json') as f:
                content = f.read()
        self.assertEqual(content, '[]')


class test_from_json_string(unittest.TestCase):
    """Testing from json file function
    """
    def test_square_one(self):
        """test_square_one
        """
        json_str = Base.to_json_string([{'size': 9, 'id': 1, 'x': 1, 'y': 0}])
        self.assertEqual(len(Base.from_json_string(json_str)[0]), 4)
        self.assertEqual(
            type(Base.from_json_string(json_str)[0]).__name__, 'dict'
        )

    def test_rectangle_one(self):
        """test_rectangle_one
        """
        json_str = Base.to_json_string([{'size': 9, 'id': 1, 'x': 1, 'y': 0}])
        self.assertEqual(len(Base.from_json_string(json_str)[0]), 4)
        self.assertEqual(
            type(Base.from_json_string(json_str)[0]).__name__, 'dict'
        )

    def test_square_two(self):
        """test_square_two
        """
        json_str = Base.to_json_string(
            [{'size': 9, 'id': 1, 'x': 1, 'y': 0},
             {'size': 10, 'id': 12, 'x': 1, 'y': 0}])
        self.assertEqual(len(Base.from_json_string(json_str)[0]), 4)
        self.assertEqual(len(Base.from_json_string(json_str)[1]), 4)
        self.assertEqual(
            type(Base.from_json_string(json_str)[0]).__name__, 'dict'
        )
        self.assertEqual(
            type(Base.from_json_string(json_str)[1]).__name__, 'dict'
        )

    def test_rectangle_two(self):
        """test_square_two
        """
        json_str = Base.to_json_string(
            [{'height': 9, 'width': 10, 'id': 1, 'x': 1, 'y': 0},
             {'weight': 10, 'width': 9, 'id': 12, 'x': 1, 'y': 0}])
        self.assertEqual(len(Base.from_json_string(json_str)[0]), 5)
        self.assertEqual(len(Base.from_json_string(json_str)[1]), 5)
        self.assertEqual(type(
            Base.from_json_string(json_str)[0]
            ).__name__, 'dict')
        self.assertEqual(
            type(Base.from_json_string(json_str)[1]).__name__, 'dict')

    def test_for_empty_string(self):
        """Tests for empty string
        """
        self.assertEqual(Base.from_json_string(''), [])

    def test_for_none(self):
        """Tests for none
        """
        self.assertEqual(Base.from_json_string(None), [])


class test_create(unittest.TestCase):
    """Test create method
    """
    def test_by_one_dict_rectangle_new(self):
        """Test for rectangle dict
        """
        rec1 = {'height': 9, 'width': 10, 'id': 1, 'x': 1, 'y': 0}
        rec_obj = Rectangle(10, 9, 1, 0, 1)
        dict1 = Rectangle.create(**rec1).to_dictionary()
        dict2 = rec_obj.to_dictionary()
        self.assertEqual(dict1, dict2)

    def test_by_one_dict_rectangle_same_obj(self):
        """Test for rectangle dict
        """
        rec1 = {'height': 9, 'width': 10, 'id': 1, 'x': 1, 'y': 0}
        newly_created = Rectangle.create(**rec1)
        strr = str(newly_created)
        self.assertEqual("[Rectangle] (1) 1/0 - 10/9", strr)

    def test_by_one_dict_square_new(self):
        """Test for square dict
        """
        square1 = {'size': 10, 'id': 1, 'x': 1, 'y': 0}
        rec_obj = Square(10, 1, 0, 1)
        dict1 = Square.create(**square1).to_dictionary()
        dict2 = rec_obj.to_dictionary()
        self.assertEqual(dict1, dict2)

    def test_by_one_dict_square_str_same_obj(self):
        """Test for rectangle dict
        """
        square1 = {'size': 10, 'id': 1, 'x': 1, 'y': 0}
        newly_created = Square.create(**square1)
        strr = str(newly_created)
        self.assertEqual("[Square] (1) 1/0 - 10", strr)

    def test_square_will_not_equal(self):
        """test_square_will_not_equal
        """
        square1 = {'size': 10, 'id': 1, 'x': 1, 'y': 0}
        rec_obj = Square(10, 1, 0, 1)
        new_obj = Square.create(**square1)
        self.assertNotEqual(rec_obj, new_obj)

    def test_rectangle_will_not_equal(self):
        """test_square_will_not_equal
        """
        rec = {'height': 9, 'width': 10, 'id': 1, 'x': 1, 'y': 0}
        rec_obj = Square(10, 1, 0, 1)
        new_obj = Square.create(**rec)
        self.assertNotEqual(rec_obj, new_obj)

    def test_square_will_not_is(self):
        """test_square_will_not_equal
        """
        square1 = {'size': 10, 'id': 1, 'x': 1, 'y': 0}
        rec_obj = Square(10, 1, 0, 1)
        new_obj = Square.create(**square1)
        self.assertIsNot(rec_obj, new_obj)

    def test_rectangle_will_not_is(self):
        """test_square_will_not_equal
        """
        rec = {'height': 9, 'width': 10, 'id': 1, 'x': 1, 'y': 0}
        rec_obj = Square(10, 1, 0, 1)
        new_obj = Square.create(**rec)
        self.assertIsNot(rec_obj, new_obj)


class test_load_from_file(unittest.TestCase):
    def test_square_normal_input(self):
        """test_square_normal_input
        """
        List = Square.load_from_file()
        self.assertTrue(type(List) is list)

    def test_rectangle_normal_input(self):
        """test_square_normal_input
        """
        List = Rectangle.load_from_file()
        self.assertTrue(type(List) is list)

    def test_for_objs_itself_rec(self):
        """test_for_objs_itself_rec
        """
        List = Rectangle.load_from_file()
        for obj in List:
            self.assertEqual(type(obj), Rectangle)

    def test_for_objs_itself_square(self):
        """test_for_objs_itself_rec
        """
        List = Square.load_from_file()
        for obj in List:
            self.assertEqual(type(obj), Square)


if __name__ == '__main__':
    unittest.TestCase()
