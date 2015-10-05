import unittest
import find_a_word as fw

class TestStringMethods(unittest.TestCase):

  #setup
  def setUp(self):
      self.file = "file.txt"

  # tests
  def test_count(self):
      file_content = "asd asd asd aswdasd"
      self.__write_to_file(file_content)
      self.assertEqual(fw.countWords(self.file, "asd"),3)

  def test_count_unspaced(self):
      file_content = "sad fasdasd"
      self.__write_to_file(file_content)
      self.assertEqual(fw.countWords(self.file, "asd"), 2)
   
  #private
  def __write_to_file(self, string):
      open(self.file, 'w').write(string)

  def __read_file(self):
      file = open(self.file,'r')
      return file.read()


if __name__ == '__main__':
    unittest.main()