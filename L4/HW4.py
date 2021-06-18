import cv2 as cv
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

img = cv.imread("C:\\Users\\maneh_onrsjft\\Downloads\\Python\\L4\\L4\\practical_homework4\\pic1.jpg") 
#cv.imshow('pic1', img)

#problem 1
"""
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('grayscale', gray) 

gray_hist = cv.calcHist([gray], [0], None, [256], [0,256]) 
gray_hist = [i[0] for i in gray_hist]


mpl.use('tkagg')
x = np.arange(256)
plt.plot(x,gray_hist)
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')

#plt.show()
"""

#problem 2
"""
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256]) 
    mpl.use('tkagg') #backend for using matplotlib with any shell
    x = np.arange(256)
    plt.plot(x,hist, color=col)
    plt.title('Color Histogram')
    plt.xlabel('Bins')
    plt.ylabel('# of pixels')


plt.show()
"""

#problem 3
"""
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

threshold, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY) #less white
cv.imshow('simple threshold', thresh)  

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 0)
cv.imshow('adaptive threshold', adaptive_thresh) 

adaptive_thresh_gaussian = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 9)
cv.imshow('adaptive threshold gaussian', adaptive_thresh_gaussian) 
"""

#problem 4
"""
img = cv.imread("C:\\Users\\maneh_onrsjft\\Downloads\\Python\\L4\\L4\\practical_homework4\\pic2.jpg") 

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY) #less white

cv.imshow('simple threshold', thresh) 

threshold_inv, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV) #black parts are changed to white and vice versa
cv.imshow('simple threshold inversed', thresh) 
"""

cv.waitKey(0)
























cv.waitKey()
