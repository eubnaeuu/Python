class Animal :
    def __init__(self):
        self.fullness = 0
        
    def eat(self):
        self.fullness += 1
        
    def manddang(self):
        self.fullness = 10

class Human(Animal):
    def __init__(self):
        super(Human, self).__init__() # python에서는 조상을 수동으로 불러와야 함.
        self.flag_cook = False
    # pass : 중괄호 닫는 효과
    def gotoSchool(self):
        self.flag_cook = True

hum = Human()
hum.eat()
print(hum.fullness)    
print(hum.flag_cook)
hum.eat()
print(hum.fullness)
print(hum.flag_cook)
hum.manddang()
print(hum.fullness)
print(hum.flag_cook)
hum.gotoSchool()
print(hum.fullness)
print(hum.flag_cook)