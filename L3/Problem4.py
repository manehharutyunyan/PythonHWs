import cv2 as cv
import numpy as np

img = cv.imread("C:\\Users\\maneh_onrsjft\\Downloads\\Python\\L3\\L3\\practical_homework3\\pic2.jpg") 
cv.imshow('pic2', img)

blank = np.zeros(img.shape[:2], dtype = 'uint8')
circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 70, (255, 0, 0), -1)
cv.imshow('circle', circle) 

bitwise_and = cv.bitwise_and(img, img, mask=circle)
cv.imshow('bitwise_and', bitwise_and) 

cv.waitKey()