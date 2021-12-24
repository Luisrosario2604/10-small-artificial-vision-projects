#!/usr/bin/python3

# Importing python3 from local, just use "python3 <binary>" if is not the same location

# Imports
import numpy as np
from PIL import Image, ImageDraw
import cv2

# Global variables

# Class declarations

# Function declarations


# 29 < H < 88, 43 < S < 255, 126 < V 255

def main():

    videodims = (100, 100)
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    video = cv2.VideoWriter("test.mp4", fourcc, 60, videodims)
    img = Image.new('RGB', videodims, color='darkred')
    # draw stuff that goes on every frame here
    for i in range(0, 60 * 60):
        imtemp = img.copy()
        # draw frame specific stuff here.
        video.write(cv2.cvtColor(np.array(imtemp), cv2.COLOR_RGB2BGR))
    video.release()


# Main body
if __name__ == '__main__':
    main()
