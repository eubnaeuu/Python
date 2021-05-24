import numpy as np

a = np.zeros((4,4))
b = np.ones((5,5))*4

print(a.shape)
print(b.shape)
print(a.reshape(2,8))
print(a.reshape(8,2))
print(a.reshape(16))

arr = [2,0,0,3,0, 0,0,1,0,5]

# numpy의 최댓값 index 가져오기
# 방법1
max=-1
for i in arr:
    if max < i:
        max = i
print(max)

for idx, i in enumerate(arr):
    if max == i:
        print(idx)
        break
    
# 방법2
index = np.argmax(arr)
np_max = np.max(arr)
print(index)
print(np_max)

# 방법3
# print(max(arr))
# index = arr.index(max(arr))
