import cv2

# https://076923.github.io/posts/Python-opencv-6/
 
img = cv2.imread('test.PNG', cv2.IMREAD_GRAYSCALE)

# 정형화된 회전각도(90, 180, 270)

# img90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) # 시계방향으로 90도 회전
# img180 = cv2.rotate(img, cv2.ROTATE_180) # 180도 회전
# img270 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE) # 반시계방향으로 90도 회전

# cv2.imshow('original', img)
# cv2.imshow('rotate90', img90)
# cv2.imshow('rotate180', img180)
# cv2.imshow('rotate270', img270)

height, width = img.shape # channel -> 필터, 채널
matrix = cv2.getRotationMatrix2D((width/2, height/2), 10, 1)
dst = cv2.warpAffine(img, matrix, (width, height))

cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()



