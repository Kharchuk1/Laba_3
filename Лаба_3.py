import numpy as np
import cv2
import argparse
from PIL import Image, ImageDraw

with open('DS4.txt') as f:
    lines = f.readlines()

coor = []
for line in lines:
    formatted_line = line[:-1].split(' ')
    single_coordinate = (int(formatted_line[0]), int(formatted_line[1]))
    coor.append(single_coordinate)

img = Image.new("RGB", (540, 960), (255, 255, 255))
draw = ImageDraw.Draw(img)
draw.point(coor, fill='red')
img.show("result.jpg")
img.save("result.jpg")


img_1 = cv2.imread("C:\\Users\\user\\Laba_2\\result.jpg")
row,col,d = img_1.shape
center = (480, 480)
M = cv2.getRotationMatrix2D(center, 50, 1.0)
new_image = cv2.warpAffine(img_1, M, (row, col))
cv2.imwrite("C:\\Users\\user\\Laba_2\\result_1.jpg", new_image)