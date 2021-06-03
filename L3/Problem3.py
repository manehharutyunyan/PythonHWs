import cv2 as cv
import numpy as np

img = cv.imread("C:\\Users\\maneh_onrsjft\\Downloads\\Python\\L3\\L3\\practical_homework3\\pic2.jpg") 
cv.imshow('pic2', img)

average = cv.blur(img, (7,7)) #more blur
cv.imshow('average blur', average)
cv.imshow('bilateral blur', average)

#img, diameter, sigmacolor (larger value means more colors in the neighbourhood will be considered when the blur is computed), sigmaSpace (larger values means that pixels further out of the center pixel will influence the bluring calculation)
bilateral1 = cv.bilateralFilter(img, 5, 5, 5)
bilateral2 = cv.bilateralFilter(img,250, 5, 5)
bilateral3 = cv.bilateralFilter(img,5, 250, 5)
bilateral4 = cv.bilateralFilter(img,5, 5, 250)

cv.imshow('bilateral1', bilateral1)
cv.imshow('bilateral2', bilateral2)
cv.imshow('bilateral3', bilateral3)
cv.imshow('bilateral4', bilateral4)

cv.waitKey()

# when we compare average bluring and bilaterial bluring, bilaterial blurings have preserved edges