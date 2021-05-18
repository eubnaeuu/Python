import cv2
import numpy as np
print("Hello OpenCV", cv2.__version__)

img = np.full(shape=(512,512,3),fill_value=255,dtype=np.uint8) 
text="Hello OpenCV!(한글)" 
org=(50,100) 
font=cv2.FONT_HERSHEY_SIMPLEX 
cv2.putText(img,text,org,font,1,(255,0,0),2)
 
size, BaseLine=cv2.getTextSize(text,font,1,2) 
cv2.rectangle(img,org,(org[0]+size[0],org[1]-size[1]),(0,0,255)) 
cv2.circle(img,org,3,(255,0,255),2) 

cv2.imshow("A",img) 
cv2.waitKey() 
cv2.destroyAllWindows()

