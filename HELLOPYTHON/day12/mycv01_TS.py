import cv2
from cv2.cv2 import cvtColor
 
# 이미지 읽기
img = cv2.imread('test.PNG', 1) # 3x2 픽셀

img_rb = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # to 흑백
 
print(img_rb)
 
# 이미지 화면에 표시
cv2.imshow('Test Image1', img)
cv2.imshow('Test Image2', img_rb)
cv2.waitKey(0)

# 이미지 윈도우 삭제
cv2.destroyAllWindows()
 
