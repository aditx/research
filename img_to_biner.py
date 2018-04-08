import cv2
import csv
from glob import glob
import numpy as np

img_path = 'resources/data/*.jpg'
img_dir = 'resources/data/'
img_names = glob(img_path)
img = []
list = []

for i in img_names:
    img.append(cv2.imread(i, 0))
count = img.__len__()
for x in range(count):
    list.append(img[x].flatten().tolist())
    # pixel_str_list = map(str, pixel_img)
    # img_str = ','.join(pixel_str_list)
    # list.append(img_str)

directory = 'dataset/img.csv'
csvfile = open(directory, "ab")
writer = csv.writer(csvfile)
for x in list:
    x.insert(len(x), 1)
    writer.writerow(x)
    print x
    print "Write Success"
