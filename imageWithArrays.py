import numpy as np 
import openCV2
black = np.zeros([600, 600])
cv2.imshow('Black',black)
cv2.waitkey(0)
black[200:400,200:400]=203
print(black) 