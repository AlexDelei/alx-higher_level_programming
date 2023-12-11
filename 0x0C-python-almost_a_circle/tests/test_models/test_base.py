import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json

class TestBase(unittest.TestCase):

    def test_create_instance(self):
        base_instance = Base()
        self.assertIsInstance(base_instance, Base)

    def test_create_with_id(self):
        base_instance = Base(5)
        self.assertEqual(base_instance.id, 5)

    def test_to_json_string(self):
        base_instance = Base(1)
        json_string = base_instance.to_json_string([{'id': 1, 'x': 2, 'y': 3}])
        self.assertEqual(json_string, '[{"id": 1, "x": 2, "y": 3}]')

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
