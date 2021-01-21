import cv2
import numpy as np
import matplotlib.pyplot as plt
image_array=np.array(cv2.imread("s5.png"))
image_gray = cv2.cvtColor(image_array,cv2.COLOR_BGR2GRAY)
edges =cv2.Canny(image_gray, threshold1=200,threshold2=200)
plt.imshow(edges, cmap='gray')
plt.show()