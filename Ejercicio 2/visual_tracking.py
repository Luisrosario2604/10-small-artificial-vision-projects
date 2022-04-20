#!/usr/bin/python3
# Importing python3 from local, just use "python3 <binary>" if is not the same location

# /
# ** Luis ROSARIO, 2021
# ** Exercise 2 Software
# ** File description:
# ** visual tracking
# ** https://github.com/Luisrosario2604
# */


# Imports
import cv2
import numpy as np
import os
import argparse


# Global variables
path = []
is_showing_path = True
is_showing_object_detection = True
is_showing_full_path = False

# 29 < H < 88, 43 < S < 255, 126 < V 255


def show_path(frame):
    global path
    a = 0

    if not is_showing_full_path:
        path = path[-7:]

    for i in path:
        center = (i[0] + i[2] // 2, i[1] + i[3] // 2)
        if a == 0:
            a = 1
        else:
            cv2.line(frame, center, last_center, (255, 0, 0), thickness=2, lineType=8)
        last_center = center

    center = (path[-1][0] + path[-1][2] // 2, path[-1][1] + path[-1][3] // 2)
    cv2.circle(frame, center, radius=10, color=(0, 102, 0), thickness=-1)
    return frame


def detect_shape(gray, frame):
    global path
    edged = cv2.Canny(gray, 30, 200)

    contours, hierarchy = cv2.findContours(edged,
                                       cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    if len(contours) != 0:
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        frame_rectangle = [x, y, w, h]
        path.append(frame_rectangle)

        if is_showing_object_detection:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 153), 2)

    if is_showing_path:
        frame = show_path(frame)

    return frame


def visual_tracking(video, out, min, max):

    cap = cv2.VideoCapture(video)

    if out:
        _, extension = os.path.splitext(out)
        if extension == ".avi":
            fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
        else:
            fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        out = cv2.VideoWriter(out, fourcc, 10, (1280, 1024))

    while cap.isOpened():

        flag, frame = cap.read()

        kernel = np.ones((5, 5), np.float32)/25

        try:
            blur = cv2.filter2D(frame, -1, kernel)
        except:
            break

        img_hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

        lower_red = np.array([min[0], min[1], min[2]])
        upper_red = np.array([max[0], max[1], max[2]])
        mask = cv2.inRange(img_hsv, lower_red, upper_red)

        # set my output img to zero everywhere except my mask
        output_img = frame.copy()
        output_img[np.where(mask == 0)] = 0

        # or your HSV image, which I *believe* is what you want
        output_hsv = img_hsv.copy()
        output_hsv[np.where(mask == 0)] = 0

        output_hsv = cv2.cvtColor(output_hsv, cv2.COLOR_BGR2GRAY)

        kernel = np.ones((5, 5), np.uint8)
        img_erosion = cv2.erode(output_hsv, kernel, iterations=1)
        img_erosion = cv2.erode(img_erosion, kernel, iterations=1)
        img_dilation = cv2.dilate(img_erosion, kernel, iterations=1)
        img_dilation = cv2.dilate(img_dilation, kernel, iterations=1)

        img = detect_shape(img_dilation, frame)

        if out:
            out.write(img)

        cv2.imshow('frame', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    if out:
        out.release()
    cv2.destroyAllWindows()


def get_arguments():
    ap = argparse.ArgumentParser()

    ap.add_argument("-v", "--video", required=True, help="path to where the video file resides")
    ap.add_argument("-o", "--output", required=False, help="path to where the result will be save")
    ap.add_argument("-i", "--min_values", type=int, nargs="+", required=True, help="Minimum values of hsv detection (suggested : 29 49 126)")
    ap.add_argument("-a", "--max_values", type=int, nargs="+", required=True, help="Maximum values of hsv detection (suggested : 88 255 255)")

    args = vars(ap.parse_args())

    video = args['video']
    out = args['output']
    max = args['max_values']
    min = args['min_values']

    if not os.path.exists(video):
        print("[ERROR] Video parameter should be an existing file (avi or mp4)")
        exit(84)

    _, extension = os.path.splitext(video)
    if extension not in [".avi", ".mp4"]:
        print("[ERROR] Video parameter should be an existing file (avi or mp4)")
        exit(84)

    if out:
        _, extension = os.path.splitext(out)
        if extension not in [".avi", ".mp4"]:
            print("[ERROR] Out parameter should be a file with avi or mp4 extension")
            exit(84)

    if len(min) != 3:
        print("[ERROR] Minimum values parameter should be 3 ints")
        exit(84)

    if len(max) != 3:
        print("[ERROR] Maximum values parameter should be 3 ints")
        exit(84)

    for i in min:
        if i < 0 or i > 255:
            print("[ERROR] Values for Minimum values parameter should be between 0 and 255")
            exit(84)

    for i in max:
        if i < 0 or i > 255:
            print("[ERROR] Values for Maximum values parameter should be between 0 and 255")
            exit(84)

    return video, out, min, max


def main():
    video, out, min, max = get_arguments()
    visual_tracking(video, out, min, max)


# Main body
if __name__ == '__main__':
    main()
