import unittest
from message_delete import reverse_string, capitalize_string, is_capitalized

class TestStringMethods(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string("Miaw"),"waiM")

    def test_capitalize_string(self):
        self.assertEqual(capitalize_string("miaw"), "Miaw")

    def test_is_capitalizef(self):
        self.assertTrue(is_capitalized("Miaw"))
        self.assertFalse(is_capitalized("miaw"))

if __name__ == "__main__":
    unittest.main()

import unittest
import math

def get_sqrt(n):
  return math.sqrt(n)

def divide(a, b):
  return a / b

class TestUnexpected(unittest.TestCase):

  def test_get_sqrt(self):
    self.assertEqual(get_sqrt(144), 12)

  def test_neg_sqrt(self):
    with self.assertRaises(ValueError):
      get_sqrt(-3)

  def test_divide(self):
    self.assertEqual(divide(64,8), 8)

  def test_zero_divide(self):
    with self.assertRaises(ZeroDivisionError):
      divide(10, 0)

if __name__ == "__main__":
  unittest.main()    

