import unittest
from rectangle import *

class RectangleTestCase (unittest.TestCase):
    def test_area_positive_integers(self):
        self.assertEqual(area(5, 3), 15)
        
    def test_area_positive_floats(self):
        self.assertAlmostEqual(area(2.5, 4.2), 10.5)
        
    def test_area_zero_dimension(self):
        self.assertEqual(area(10, 0), 0)
        self.assertEqual(area(0, 5), 0)
        
    def test_area_square(self):
        self.assertEqual(area(10, 10), 100)
        
    def test_area_large_numbers(self):
        self.assertEqual(area(1000, 500), 500000)
    
    
    
    def test_perimeter_positive_integers(self):
        self.assertEqual(perimeter(5, 3), 16)
        
    def test_perimeter_positive_floats(self):
        self.assertAlmostEqual(perimeter(2.5, 4.2), 13.4)
        
    def test_perimeter_zero_dimension(self):
        self.assertEqual(perimeter(10, 0), 20)
        self.assertEqual(perimeter(0, 5), 10)
        
    def test_perimeter_square(self):
        self.assertEqual(perimeter(10, 10), 40)
        
    def test_perimeter_large_numbers(self):
        self.assertEqual(perimeter(1000, 500), 2000)
