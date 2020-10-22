from PIL import Image
import matplotlib.pyplot as p
import numpy as np
import numpy
im = Image.open('D:/THONY Programs/output_srtm.tif')
#im.show()

imarray = numpy.array(im)
p.plot(imarray)
p.show()
print(imarray)

import cv2

from matplotlib.image import imread

img = imread("D:/THONY Programs/output_srtm.tif")

print(img)

import matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
z=1
plt.scatter(imarray[0],imarray[1])
plt.show()