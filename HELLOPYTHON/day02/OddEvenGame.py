import random
mine = input("홀/짝을 선택하세요")
rand = round(random.random())
com = ""
result = ""

if rand < 0.5:
    com = "짝"
else:
    com = "홀" 
    
if com==mine:
    result="이김"
else :
    result="짐"

print("com :",com)
print("mine :",mine)
print("result :",result)