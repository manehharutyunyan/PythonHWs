import cv2 as cv
import numpy as np

img = cv.imread("C:\\Users\\maneh_onrsjft\\Downloads\\Python\\L3\\L3\\practical_homework3\\pic1.jpg") 
cv.imshow('pic1', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv) 

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab) 

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb) 

cv.waitKey()