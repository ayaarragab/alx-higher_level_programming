#!/usr/bin/python3
"""
This module contains the base class
"""

import json
import csv
import turtle


class Base:
    """
    Base class
    """
    __nb_objects = 0  # Tell sara

    def __init__(self, id=None):
        """
        class constructor
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        If list_dictionaries is None or empty, return the string: "[]"
        Otherwise, return the JSON string representation of list_dictionaries
        """
        if list_dictionaries and list_dictionaries is not []:
            json_represenation = json.dumps(list_dictionaries)
            return json_represenation
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        with open(filename, mode='w', encoding='utf-8') as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                json_str = Base.to_json_string(list_dicts)
                file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string
        """
        if json_string and json_string is not None or "":
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        """that returns an instance with all attributes already set
        """
        obj = cls(1, 1)
        if dictionary:
            obj.update(**dictionary)
        return (obj)

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        filename = f"{cls.__name__}.json"

        try:
            with open(filename, 'r') as file:
                json_data = file.read()
        except FileNotFoundError:
            return []

        json_rep_list = cls.from_json_string(json_data)
        newlist = list()
        for dic in json_rep_list:
            obj = cls.create(**dic)
            # astreisk for **dictionary in function def
            newlist.append(obj)
        return newlist

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        writes the csv string representation of list_objs to a file
        """
        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', encoding='utf-8', newline="") as file:
            if list_objs is None:
                pass
            else:
                if cls.__name__ == 'Rectangle':
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                else:
                    fieldnames = ['id', 'size', 'x', 'y']
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for row in list_dicts:
                    writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """
        returns a list of instances
        """
        data = []

        with open(f'{cls.__name__}.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if cls.__name__ == 'Rectangle':
                    obj = cls.create(
                        width=int(row['width']),
                        height=int(row['height']),
                        x=int(row["x"]), y=int(row["y"]),
                        id=int(row["id"])
                    )
                else:
                    obj = cls.create(
                        size=int(row['size']),
                        x=int(row["x"]), y=int(row["y"]), id=int(row["id"])
                    )
                data.append(obj)
        return data

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles and squares"""
        if list_squares and list_squares != []:
            for square in list_squares:
                sq = turtle.Turtle()
                sq.speed(1)
                for i in range(4):
                    sq.forward(square.size)
                    sq.left(90)
        if list_rectangles and list_rectangles != []:
            for rectangle in list_rectangles:
                rec = turtle.Turtle()
                rec.speed(1)
                for _ in range(2):
                    rec.forward(rectangle.width)
                    rec.left(90)
                    rec.forward(rectangle.height)
                    rec.left(90)
        turtle.done()
