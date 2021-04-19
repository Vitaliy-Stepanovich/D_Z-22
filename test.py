import unittest
from main import Test_time

class Test_Uni_Time(unittest.TestCase):
  def test_hour(self):
    test = Test_time()
    self.assertEqual(test.hour_time(4), 4)  
    self.assertEqual(test.hour_time(0), 0)
    self.assertEqual(test.hour_time(120), False)
    self.assertEqual(test.hour_time(-2), False)
    
  def test_minute(self):
    test = Test_time()
    self.assertEqual(test.minute_time(0), 0)
    self.assertEqual(test.minute_time(12), 12)
    self.assertEqual(test.minute_time(-2), False)  
    self.assertEqual(test.minute_time(200), False) 
    
  def test_second(self):
    test = Test_time()
    self.assertEqual(test.second_time(4), 4)  
    self.assertEqual(test.second_time(70), False)
    self.assertEqual(test.second_time(-12), False)
    self.assertEqual(test.second_time(0), 0)
  
  
def main():
    unittest.main()
  
#  запускать с помощью командной строки
if __name__ == '__main__':
  main()