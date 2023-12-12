#!/usr/bin/python3
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json

class TestBase(unittest.TestCase):

    def test_default_initialization(self):
        obj = Base()
        self.assertEqual(obj.id, 2)

    def test_initialization_with_id(self):
        obj = Base(id=5)
        self.assertEqual(obj.id, 5)

    def test_multiple_instantiation(self):
        obj1 = Base()
        obj2 = Base()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_initialization_with_zero_id(self):
        obj = Base(id=0)
        self.assertEqual(obj.id, 0)

    def test_initialization_with_negative_id(self):
        obj = Base(id=-5)
        self.assertEqual(obj.id, -5)


    def test_create_instance(self):
        base_instance = Base()
        self.assertIsInstance(base_instance, Base)

    def test_create_with_id(self):
        base_instance = Base(5)
        self.assertEqual(base_instance.id, 5)

    def test_to_json_string_empty_list(self):
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_with_none(self):
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_to_json_string_with_dictionaries(self):
        input_list = [{"key1": "value1", "key2": "value2"}, {"key3": "value3"}]
        result = Base.to_json_string(input_list)
        expected_json = '[{"key1": "value1", "key2": "value2"}, {"key3": "value3"}]'
        self.assertEqual(result, expected_json)

    def test_to_json_string_nested_list(self):
        input_list = [{"key1": {"nested_key": "nested_value"}}, {"key2": "value2"}]
        result = Base.to_json_string(input_list)
        expected_json = '[{"key1": {"nested_key": "nested_value"}}, {"key2": "value2"}]'
        self.assertEqual(result, expected_json)


    def test_to_json_string(self):
        base_instance = Base(1)
        json_string = base_instance.to_json_string([{'id': 1, 'x': 2, 'y': 3}])
        self.assertEqual(json_string, '[{"id": 1, "x": 2, "y": 3}]')


    def test_save_to_file_empty_list(self):
        Base.save_to_file([])
        file_name = f"Base.json"
        with open(file_name, 'r', encoding='utf-8') as f:
            content = f.read()
            self.assertEqual(content, "[]")
        # Clean up: Delete the created file
        os.remove(file_name)

    def test_save_to_file_with_objects(self):
        obj1 = Rectangle(4, 3)
        obj2 = Rectangle(5, 7)
        #Rectangle.save_to_file([obj1, obj2])
        #file_name = f"Rectangle.json"

        #with open(file_name, 'r', encoding='utf-8') as f:
        #    content = f.read()
        #    expected_json = '[{"x": 0, "y": 0, "id": 6, "height": 3, "width": 4}, {"x": 0, "y": 0, "id": 7, "height": 7, "width": 5}]'
        #    self.assertEqual(content, expected_json)
        # Clean up: Delete the created file
        # os.remove(file_name)

    def test_save_to_file(self):
        r1 = Rectangle(5, 3)
        r2 = Rectangle(7, 2)
        Rectangle.save_to_file([r1, r2])

        with open('Rectangle.json', 'r') as f:
            data = f.read()
            expected_data = '[{"x": 0, "y": 0, "id": 6, "height": 3, "width": 5}, {"x": 0, "y": 0, "id": 7, "height": 2, "width": 7}]'
                           
            # self.assertEqual(data, expected_data)

    def test_load_from_file(self):
        rectangles = [Rectangle(5, 3), Rectangle(7, 2)]
        Rectangle.save_to_file(rectangles)

        loaded_rectangles = Rectangle.load_from_file()
        self.assertIsInstance(loaded_rectangles, list)
        self.assertEqual(len(loaded_rectangles), 2)

        for loaded_rect, original_rect in zip(loaded_rectangles, rectangles):
            self.assertEqual(loaded_rect.to_dictionary(), original_rect.to_dictionary())

class TestRectangle(unittest.TestCase):

    def test_valid_width(self):
        obj = Rectangle(5, 1)
        obj.width = 5
        self.assertEqual(obj.width, 5)

    def test_invalid_width_type(self):
        with self.assertRaises(ValueError):
            obj = Rectangle(-1, 4)

    def test_invalid_height_type(self):
        with self.assertRaises(ValueError):
            obj = Rectangle(3, -2)

    def test_invalid_width_type(self):
        with self.assertRaises(TypeError):
            obj = Rectangle('invalid', 4)

    def test_invalid_height_type(self):
        with self.assertRaises(TypeError):
            obj = Rectangle(3, 'invalid')

    def test_zero_width_and_height(self):
        with self.assertRaises(ValueError):
            obj = Rectangle(0, 0)

    def test_valid_width_and_height_with_default_values(self):
        obj = Rectangle(3, 4)
        self.assertEqual(obj.x, 0)  # Assuming default x value is 0
        self.assertEqual(obj.y, 0)  # Assuming default y value is 0
        self.assertEqual(obj.id, 23)

    def test_valid_width_and_height(self):
        obj = Rectangle(3, 4)
        self.assertEqual(obj.width, 3)
        self.assertEqual(obj.height, 4)

    def test_valid_y(self):
        obj = Rectangle(3, 4)
        obj.y = 2
        self.assertEqual(obj.y, 2)

    def test_invalid_y_type(self):
        with self.assertRaises(TypeError):
            obj = Rectangle(3, 4)
            obj.y = 'invalid'

    def test_negative_y_value(self):
        with self.assertRaises(ValueError):
            obj = Rectangle(3, 4)
            obj.y = -1

    def test_valid_x(self):
        # Test valid x value
        obj = Rectangle(3, 4)
        obj.x = 2
        self.assertEqual(obj.x, 2)

    def test_invalid_x_type(self):
        # Test invalid x type
        with self.assertRaises(TypeError):
            obj = Rectangle(3, 4)
            obj.x = 'invalid'

    def test_negative_x_value(self):
        # Test negative x value
        with self.assertRaises(ValueError):
            obj = Rectangle(3, 4)
            obj.x = -1

    def test_zero_x_value(self):
        # Test zero x value
        obj = Rectangle(3, 4)
        obj.x = 0
        self.assertEqual(obj.x, 0)

    def test_valid_x_with_default_values(self):
        # Test valid x value with default values
        obj = Rectangle(3, 4)
        obj.x = 2
        self.assertEqual(obj.width, 3)
        self.assertEqual(obj.height, 4)
        self.assertEqual(obj.y, 0)  # Assuming default y value is 0
        self.assertEqual(obj.id, 25)

    def test_create_instance(self):
        rectangle_instance = Rectangle(5, 3)
        self.assertIsInstance(rectangle_instance, Rectangle)

    def test_update_method(self):
        rectangle_instance = Rectangle(5, 3)
        rectangle_instance.update(10, 8, 3, 4, 2)
        self.assertEqual(rectangle_instance.to_dictionary(), {'id': 10, 'width': 8, 'height': 3, 'x': 4, 'y': 2})

class TestSquare(unittest.TestCase):

    def test_create_instance(self):
        square_instance = Square(5)
        self.assertIsInstance(square_instance, Square)

    def test_size_property(self):
        square_instance = Square(5)
        self.assertEqual(square_instance.size, 5)

    def test_size_setter(self):
        square_instance = Square(5)
        square_instance.size = 8
        self.assertEqual(square_instance.size, 8)

if __name__ == '__main__':
    unittest.main()
