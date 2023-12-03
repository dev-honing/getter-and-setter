# main.py

class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

# Dog 클래스의 my_dog 인스턴스를 생성
my_dog = Dog('멍멍이', 3)

# 인스턴스를 통해 속성에 접근해서 출력
print(my_dog.name) # 멍멍이