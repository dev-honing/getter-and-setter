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
        self._name = name
        self._age = age

    def bark(self):
        """
        개가 짖는 소리를 출력하는 메서드
        """
        print('멍멍!')

    @property
    def age(self):
        """
        개의 나이를 반환하는 getter
        """
        return self._age
    
    @age.setter
    def age(self, new_age):
        """
        개의 나이를 설정하는 setter

        :param new_age: 새로 설정할 개의 나이
        :type new_age: int
        """
        if new_age >= 0:
            self._age = new_age
        else:
            print('나이는 음수일 수 없다.')

    def is_adult(self):
        """
        개의 성인 여부를 확인하는 메서드
        Returns:
            bool: 개가 성인인 경우 True, 그렇지 않으면 False
        """
        return self._age >= 3

# Dog 클래스를 호출하여 새로운 인스턴스(my_dog)를 생성하고 초기화
my_dog = Dog('멍멍이', 3)

# my_dog 인스턴스에 접근해 개의 이름을 출력
print(my_dog._name)  # 멍멍이

# age 속성에 접근해 나이 출력
print(my_dog.age)  # 3

# 개의 성인 여부를 확인
print(my_dog.is_adult())  # True

# setter를 통한 나이 변경 (유효한 경우)
my_dog.age = 5
print(my_dog.age) # 5

# setter를 통한 나이 변경 (유효하지 않은 경우)
my_dog.age = -3 # 나이는 음수일 수 없다.
print(my_dog.age) # 5 (이전에 유효했던 값이 유지됨)