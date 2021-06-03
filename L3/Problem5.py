import cv2 as cv
import numpy as np


blank = np.zeros((200, 200), dtype = 'uint8')
rectangle = cv.rectangle(blank.copy(), (20, 20), (180, 180), (178,178,178), -1)
circle = cv.circle(blank.copy(), (100, 100), 100, (178,178,178), -1)

pic1 = cv.bitwise_xor(rectangle, circle)
pic2 = cv.bitwise_or(rectangle, circle)

cv.imshow('pic1', pic1)
cv.imshow('pic2', pic2)

blank3 = np.zeros(shape=(200,200, 3))
rectangle3 = cv.rectangle(blank3.copy(), (20, 20), (180, 180), (255,0,208), -1)
circle3 = cv.circle(blank3.copy(), (100, 100), 100, (255,0,208), -1)
pic3 = cv.bitwise_xor(rectangle3, circle3)
cv.imshow('pic3', pic3)


cv.waitKey(0)
