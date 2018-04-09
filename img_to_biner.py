import cv2
import csv
from glob import glob

img_path = 'resources/data/*.jpg'
img_dir = 'resources/data/'
img_names = glob(img_path)
img = []
list = []
data = []
xmin = []
xmax = []
xnorm = []

for i in img_names:
    img.append(cv2.imread(i, 0))
count = img.__len__()

for x in range(count):
    data.append(img[x])
    xmin.append(data[x].min())
    xmax.append(data[x].max())
    xnorm.append((data[x] - xmin[x]) * 255 / (xmax[x] - xmin[x]))

    list.append(xnorm[x].flatten().tolist())

    # pixel_str_list = map(str, pixel_img)
    # img_str = ','.join(pixel_str_list)
    # list.append(img_str)

directory = 'dataset/img_normalization.csv'
csvfile = open(directory, "ab")
writer = csv.writer(csvfile)
for x in list:
    x.insert(len(x), 1)
    writer.writerow(x)
    print x
    print "Write Success"
