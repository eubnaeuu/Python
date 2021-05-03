import random
com =""
mine = input("가위/바위/보를 선택해주세요")
result = ""
comnum = random.random()


if comnum < 1/3:
    comans = "가위"
elif comnum <2/3:
    comans = "바위"
else :
    comans = "보"



# 가위 < 바위 < 보    
if comans == mine:
    result="비김"
elif comans < mine :
    if mine == "보" and comans == "가위":
        result="짐"            
    else :
        result="이김"
else :
    if comans == "보" and mine == "가위":
        result="이김"            
    else :
        result="짐"
         
         
print(mine)
# print(comnum)
print(comans)
print(result)
    
