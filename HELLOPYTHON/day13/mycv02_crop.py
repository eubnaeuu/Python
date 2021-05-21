import cv2
 
img = cv2.imread('test.PNG', cv2.IMREAD_GRAYSCALE)

print(len(img)) # x축 길이
print(len(img[0])) # y축 길이

cropped_img = img[45:90 , 140:205]
cv2.imwrite('test_crop.png', cropped_img)

cv2.imshow('test image',cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
