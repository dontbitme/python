import unittest
import find_a_word as fw

class TestStringMethods(unittest.TestCase):

  def setUp(self):
  	  self.file = "file.txt"

  def test_upper(self):
      self.assertEqual(fw.countWords(self.file, "asd"),3)

if __name__ == '__main__':
    unittest.main()