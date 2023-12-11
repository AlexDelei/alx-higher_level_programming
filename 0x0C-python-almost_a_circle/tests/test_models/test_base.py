import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def test_base_creation(self):
        b = Base()
        self.assertIsInstance(b, Base)
        self.assertEqual(b.id, 1)

    def test_base_custom_id(self):
        b = Base(100)
        self.assertEqual(b.id, 100)

    def test_base_to_json_string(self):
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_base_save_to_file(self):
        # Add test for saving to file
        pass

    def test_base_from_json_string(self):
        result = Base.from_json_string("[]")
        self.assertEqual(result, [])

  #  def test_base_create(self):
 #       result = Base.create()
#        self.assertIsInstance(result, Base)

    def test_base_load_from_file(self):
        # Add test for loading from file
        pass


class TestRectangle(unittest.TestCase):

    def test_rectangle_creation(self):
        r = Rectangle(5, 10)
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 3)

    def test_rectangle_area(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_rectangle_display(self):
        # Add test for display method
        pass

    def test_rectangle_update(self):
        # Add test for update method
        pass

    def test_rectangle_to_dictionary(self):
        r = Rectangle(3, 4)
        result = r.to_dictionary()
        expected = {'id': 4, 'width': 3, 'height': 4, 'x': 0, 'y': 0}
        self.assertEqual(result, expected)


class TestSquare(unittest.TestCase):

    def test_square_creation(self):
        s = Square(5)
        self.assertIsInstance(s, Square)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertEqual(s.id, 5)

    def test_square_update(self):
        # Add test for update method
        pass

    def test_square_to_dictionary(self):
        s = Square(3)
        result = s.to_dictionary()
        expected = {'id': 6, 'size': 3, 'x': 0, 'y': 0}
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
