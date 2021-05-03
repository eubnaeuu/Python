#ex01
# 입력받은 두 숫자의 합
def ex01():
    a = int(input("첫 숫자를 입력하시오"))
    b = int(input("끝 숫자를 입력하시오"))

    print("ex01: 숫자의 합은",a+b,"입니다")
    print("ex01: 숫자의 합은 {}입니다".format(a+b))

#ex02
# 입력받은 두 숫자 사이의 합?
def ex02():
    a = int(input("첫 숫자를 입력하시오"))
    b = int(input("끝 숫자를 입력하시오"))
    sum = 0
    
    for i in range(a, b+1):
        sum += i
    print("ex02: ",sum)

#ex03
# 출력할 구구단은?
def ex03():
    a = int(input("출력할 구구단은?"))
    gugudan(a)

#ex04
# 입력받은 숫자 사이의 짝수 합
def ex04():
    a = int(input("첫 숫자를 입력하시오"))
    b = int(input("끝 숫자를 입력하시오"))
    sum = 0
    for i in range(a,b+1):
        if i%2 == 0:
            sum += i
    print("짝수의 합은 {} 입니다 ".format(sum))
        
#ex05
# 입력받은 숫자 사이의 홀수 합
def ex05():        
    a = int(input("첫 숫자를 입력하시오"))
    b = int(input("끝 숫자를 입력하시오"))
    sum = 0
    for i in range(a,b+1):
        if i%2 == 1:
            sum += i
    print("홀수의 합은 {} 입니다".format(sum))

def gugudan(n):
    for i in range(1,10):
        print(n,"*",i,"=",n*i)
        
        
