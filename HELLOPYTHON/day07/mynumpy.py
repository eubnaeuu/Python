import numpy as np

"""
arr과 numpy의 비교
"""
arr = [1,2,3,4,5]   
arr_n = np.array(arr) # arr을 numpy 형태로 변환
print(arr) # [1, 2, 3, 4, 5]
print(arr_n) # [1 2 3 4 5]

arr = arr * 5
print(arr) # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
arr_n = arr_n * 5
print(arr_n) # [ 5 10 15 20 25]

# numpy 와 arr 굉장히 비슷
"""
1. numpy 속도 빠름
2. arr의 내부 연산 가능 -> java에서는 for문을 통해 구현해야하는 기능 
"""


arr1 = [1,10]
arr2 = [2,4]
np1 = np.array(arr1)
np2 = np.array(arr2)
print("이거됨?",np1/np2)
