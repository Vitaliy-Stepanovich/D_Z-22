from datetime import datetime
from datetime import time
import unittest

class Time_programm:
  def __init__(self, hour, minute, second, vibor):
    self.hour = hour
    self.minute = minute
    self.second = second
    self.vibor = vibor
  
  now = datetime.now() 
  s1 = now.strftime("%H:%M:%S")
  print("Текущее время", s1)
  print('_____________________________________________')
  print()
  
  def time_choice(self):
    while True:
      try:
        self.vibor = int(input("Выберите, что хотите изменить? 1.часы. 2.минуты. 3.секунды. 4.все полностью "))
        print()
      except ValueError:
        print()
        print(f'Error!  это ошибка, попробуйте снова.')
        print()
        continue
      
      if self.vibor >= 1 and self.vibor <=4:
            break
          
    if self.vibor == 1:
      while True:
        try:
            self.hour = int(input('Введите колличество часов '))
            self.hour = time(self.hour, Time_programm.now.minute, Time_programm.now.second)
        except ValueError:
            print()
            print(f'Error!  это ошибка, попробуйте снова.')
            print()
        else:
            print(f'Новое время: {self.hour}')
            break

    elif self.vibor == 2:
      while True:
        try:
            self.minute = int(input('Введите колличество минут '))
            self.minute = time(Time_programm.now.hour, self.minute, Time_programm.now.second)
        except ValueError:
            print()
            print(f'Error!  это ошибка, попробуйте снова.')
            print()
        else:
            print(f'Новое время: {self.minute}')
            break
          
    elif self.vibor == 3:
      while True:
        try:
            self.second = int(input('Введите колличество секунд '))
            self.second = time(Time_programm.now.hour, Time_programm.now.minute, self.second)
        except ValueError:
            print()
            print(f'Error!  это ошибка, попробуйте снова.')
            print()
        else:
            print(f'Новое время: {self.second}')
            break
          
    elif self.vibor == 4:
      while True:
        try:
            self.hour = int(input('Введите колличество часов '))
            self.minute = int(input('Введите колличество минут '))
            self.second = int(input('Введите колличество секунд '))

            self.maxi = time(self.hour, self.minute, self.second)
        except ValueError:
            print()
            print(f'Error!  где то ошибка, попробуйте снова.')
            print()
        else:
            print(f'Новое время: {self.maxi}')
            break
          
# -------------------------------------------------------
# 
# прописал отдельно для тестов аналогичный код, код основной программы не протестить
# 
# 
# -------------------------------------------------------
class Test_time:
  def hour_time(self, hour):
    self.hour = hour
    while True:
      try:
        self.hour = int(self.hour)
      except ValueError:
         print(f'Error!  это не число, попробуйте снова.')
         break
      if self.hour >= 0 and self.hour < 24:
        return self.hour
      else:
        return False

  def minute_time(self, minute):
    self.minute = minute
    while True:
      try:
        self.minute = int(self.minute)
      except ValueError:
         print(f'Error!  это не число, попробуйте снова.')
         break
      if self.minute >= 0 and self.minute < 60:
        return self.minute
      else:
        return False
        
  def second_time(self, second):
    self.second = second
    while True:
      try:
        self.second = int(self.second)
      except ValueError:
         print(f'Error!  это не число, попробуйте снова.')
         break
      if self.second >= 0 and self.second < 60:
        return self.second
      else:
        return False
    
def main():
  
  sss = Time_programm(hour=10, minute=10, second=10, vibor=4)
  sss.time_choice()


if __name__ == '__main__':
  main()

