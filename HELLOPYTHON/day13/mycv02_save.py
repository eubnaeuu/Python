import cv2
 
img = cv2.imread('test.PNG', cv2.IMREAD_GRAYSCALE)
cv2.imwrite('test_save.jpg', img)

print(img)

cv2.imshow('test image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# paste.jpg