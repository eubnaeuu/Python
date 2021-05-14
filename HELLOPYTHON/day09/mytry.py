try:
    a = 4/0
    print(a)
except ZeroDivisionError as e:  
    print('예외가 발생했습니다.')