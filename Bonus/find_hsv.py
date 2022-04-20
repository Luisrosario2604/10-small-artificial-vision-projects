#!/usr/bin/python3
# Importing python3 from local, just use "python3 <binary>" if is not the same location

# /
# ** Luis ROSARIO, 2021
# ** Exercise Bonus Software
# ** File description:
# ** Finding good hsv from image
# ** https://github.com/Luisrosario2604
# */

# Imports
import cv2
import numpy as np
import argparse
import os

# Global variables

# Function declarations


# A required callback method that goes into the trackbar function.
def nothing(x):
    pass


def get_arguments():
    ap = argparse.ArgumentParser()

    ap.add_argument("-f", "--file", required=True, help="File location (webcam for webcam)")
    ap.add_argument("-n", "--min_values", required=False, help="Min HSV values", nargs='+')
    ap.add_argument("-x", "--max_values", required=False, help="Max HSV values", nargs='+')

    args = vars(ap.parse_args())

    file = args["file"]
    min_values = args["min_values"]
    max_values = args["max_values"]

    return file, min_values, max_values


def main():

    file, min_values, max_values = get_arguments()

    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)

    cv2.namedWindow("Trackbars")

    cv2.createTrackbar("L - H", "Trackbars", 0, 179, nothing)
    cv2.createTrackbar("L - S", "Trackbars", 0, 255, nothing)
    cv2.createTrackbar("L - V", "Trackbars", 0, 255, nothing)
    cv2.createTrackbar("U - H", "Trackbars", 179, 179, nothing)
    cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
    cv2.createTrackbar("U - V", "Trackbars", 255, 255, nothing)

    while True:
        if file != 'webcam':
            frame = cv2.imread(file)
        else:
            ret, frame = cap.read()
            if not ret:
                break
            # Flip the frame horizontally (Not required)
            frame = cv2.flip(frame, 1)

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        l_h = cv2.getTrackbarPos("L - H", "Trackbars")
        l_s = cv2.getTrackbarPos("L - S", "Trackbars")
        l_v = cv2.getTrackbarPos("L - V", "Trackbars")
        u_h = cv2.getTrackbarPos("U - H", "Trackbars")
        u_s = cv2.getTrackbarPos("U - S", "Trackbars")
        u_v = cv2.getTrackbarPos("U - V", "Trackbars")

        lower_range = np.array([l_h, l_s, l_v])
        upper_range = np.array([u_h, u_s, u_v])

        # Filter the image and get the binary mask, where white represents your target color
        mask = cv2.inRange(hsv, lower_range, upper_range)

        # You can also visualize the real part of the target color
        res = cv2.bitwise_and(frame, frame, mask=mask)

        # Converting the binary mask to 3 channel image, this is just so we can stack it with the others
        mask_3 = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

        # stack the mask, orginal frame and the filtered result
        stacked = np.hstack((mask_3, frame, res))

        # Show this stacked frame at 40% of the size.
        cv2.imshow('Trackbars', cv2.resize(stacked, None, fx=0.4, fy=0.4))

        # If the user presses ESC then exit the program
        key = cv2.waitKey(1)
        if key == 27:
            break

        # If the user presses `s` then print this array.
        if key == ord('s'):

            thearray = [[l_h, l_s, l_v], [u_h, u_s, u_v]]
            print(thearray)

            # Also save this array as penval.npy
            np.save('hsv_value', thearray)
            break

        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


# Main body
if __name__ == '__main__':
    main()
