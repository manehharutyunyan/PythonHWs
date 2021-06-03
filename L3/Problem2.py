import cv2 as cv
import numpy as np

img = cv.imread("C:\\Users\\maneh_onrsjft\\Downloads\\Python\\L3\\L3\\practical_homework3\\pic1.jpg") 
cv.imshow('pic1', img)

b, g, r = cv.split(img)

cv.imshow('blue', b)
cv.imshow('green', g)
cv.imshow('red', r)

cv.waitKey()