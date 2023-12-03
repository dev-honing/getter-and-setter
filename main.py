# main.py

class Dog:
    def __init__(self, name, age):
        """
        Dog 클래스의 생성자 함수

        :param name: 개의 이름
        :type name: str
        :param age: 개의 나이
        :type age: int
        """
        self.name = name
        self.age = age

    def bark(self):
        """
        개가 짖는 소리를 출력하는 메서드
        """
        print('멍멍!')

    def is_adult(self):
        """
        개의 성인 여부를 확인하는 메서드
        Returns:
            bool: 개가 성인인 경우 True, 그렇지 않으면 False
        """
        return self.age >= 3

# Dog 클래스를 호출하여 새로운 인스턴스(my_dog)를 생성하고 초기화
my_dog = Dog('멍멍이', 3)

# my_dog 인스턴스에 접근해 개의 이름을 출력
print(my_dog.name)  # 멍멍이

# 개가 짖는 소리 출력
my_dog.bark()  # 멍멍!

# 개의 성인 여부를 확인
print(my_dog.age) # 3
print(my_dog.is_adult()) # True