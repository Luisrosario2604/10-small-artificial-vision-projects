#!/usr/bin/python3

# Importing python3 from local, just use "python3 <binary>" if is not the same location

# Imports
import sys
from PIL import Image
import numpy

# Global variables

# Class declarations

# Function declarations


# 29 < H < 88, 43 < S < 255, 126 < V 255

def main():

    for num in range(1, 239):
        img = Image.open("./lapiz-frames/frames/frame" + str(num) + ".jpg")
        img = img.convert('HSV')

        y = numpy.asarray(img).copy()

        y.setflags(write=1)

        H = y[:, :, 0]
        S = y[:, :, 1]
        V = y[:, :, 2]
        mask = (29 < H) & (43 < S) & (126 < V)
        mask2 = (H > 88) & (S > 255) & (V > 255)
        y[mask] = 0
        y[mask2] = 0

        shadow = Image.fromarray(y, 'HSV')

        #shadow.show()

        blended = Image.blend(img, shadow, alpha=0.5)
        #blended.show()
        result = blended.convert(mode='RGB')
        result.save("./results/frame" + str(num) + ".jpg", "JPEG")


# Main body
if __name__ == '__main__':
    main()
