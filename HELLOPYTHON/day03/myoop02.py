class JindoDog:

    def __init__(self):
        self.power_bark = 0

    def tranning(self):
        self.power_bark += 1

        
class SokchoBird:

    def __init__(self):
        self.flag_Icanfly = False

    def practice(self):
        self.flag_Icanfly = True


class Gaesae(JindoDog, SokchoBird):

    def __init__(self): # super(Human, self).__init__()    #super는 첫번째 부모만 인식하므로 다중상속하는 경우 해당 조상클래스를 직접 입력하며 self도 써줘야함
        JindoDog.__init__(self) 
        SokchoBird.__init__(self) 


gaesae = Gaesae()
print(gaesae.flag_Icanfly)
print(gaesae.power_bark)

gaesae.practice()
print("날기연습")
print(gaesae.flag_Icanfly)
print(gaesae.power_bark)

gaesae.tranning()
print("짖기연습")
print(gaesae.flag_Icanfly)
print(gaesae.power_bark)  
