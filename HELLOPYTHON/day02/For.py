arra = [1,2,3,4,5]

# len : 길이
print(len(arra))

arrb = range(5) # [0,1,2,3,4]
arrc = range(1,5) # [1,2,3,4]

print(arrc[0])
print(arrc[1])
print(arrc[2])
print(arrc[3])

# 개행없이 출력하는 방법
print("hell",end="")
print("o")

print(arra) # [1, 2, 3, 4, 5]
print(arrb) # range(0, 4)
print(arra[0]) # 1  
print(arrb[0]) # 0
print(arrc[0]) # 1

for i in arra:
    print(i)
    if 3%i==0 :
        print("짝")



