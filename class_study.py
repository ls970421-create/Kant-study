# 부모 클래스 Base Class, Super Class, Parent Class
class Animal:
    # 공통 기능
    def breath(self):
        print("숨을 쉽니다.")

# 상속 (Inheritance)
class Dog(Animal):
    # 상속 받은 클래스에서만 있는 고유 기능
    def bark(self):
        print("멍멍")

# 인스턴스 생성
dog1 = Dog()    # Dog() : 설계도 / dog1 : 도면을 현재 가지고 있는 인스턴스
dog1.breath()   # 부모 클래스로부터 물려받은 메서드를 그대로 사용 가능
dog1.bark()     # 자식 클래스의  고유 기능

# 메서드 오버라이딩 (Method Overriding)
# 부모 클래스에서 정의된 메서드를 수정 또는 추가하는 기능(재정의)
class Cat(Animal):
    def sound(self):
        print("야옹")   # 부모 클래스에 있는 "숨을 쉽니다."를 출력하는 것이 아닌, 야옹을 출력하겠다 -> 재정의
                        # 부모가 만든 기능을 사용하는 것이 아닌, 새롭게 정의해서 사용하겠단 의미
nabi = Cat()
nabi.sound()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)      # super의 의미 :  상속 받은 부모 클래스에 접근하겠다.
                                    # super() 통해서 부모 클래스의 생성자(.__init__(name))에 접근해서 name 속성을 설정
        self.major = major          # 여기가 NAME 속성을 설정하는 역할

std1 = Student("손흥민", 32, "스포츠댄스")
print(std1.age)    # 부모 클래스로부터 물려받은 속성
print(std1.major)   # 자식 고유의 속성

class Secret:
    def __init__(self):
        self.__password = "1234"    # 외부 노출을 원치 않은 경우에는 __를 붙임 (_ 두 개)

my_password = Secret()
print(my_password._Secret__password)

class Wallet:
    def __int__(self):
        self.__money = 1000 # 숨겨진 데이터

    def get_money(self):    # Getter : 값을 안전하게 전달하는 용도
        return self.__money

    def set_money(self, amount):    # Setter : 올바른 값이 들어왔는지 검증 로직을 추가할 수 있음
        if amount >= 0:
            self.__money = amount

        else:
            print("잘못된 값입니다.")

wallet = Wallet()
wallet.set_money(2000)
print(wallet.get_money())