#!/usr/bin/python3
# Importing python3 from local, just use "python3 <binary>" if is not the same location

# /
# ** Luis ROSARIO, 2021
# ** Exercise 8.2 Software
# ** File description:
# ** Tracking with opencv
# ** https://github.com/Luisrosario2604
# */

# Imports
import argparse
import cv2
import os
import time


# Global variables

# Class declarations

# Function declarations


def tracking(video, tracker):

    cap = cv2.VideoCapture(video)
    roi = None

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if roi is None:
            roi = cv2.selectROI("frame", frame, fromCenter=False, showCrosshair=True)
            tracker.init(frame, roi)
        else:
            success, box = tracker.update(frame)
            if success:
                (x, y, w, h) = [int(v) for v in box]
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 130, 38), 2)
            else:
                print("We lost the object")
            cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        time.sleep(0.01)
    cap.release()
    cv2.destroyAllWindows()


def get_arguments():
    ap = argparse.ArgumentParser()

    ap.add_argument("-i", "--image", required=True, help="path to where the video file resides")
    ap.add_argument("-t", "--tracker", required=False, default="kcf", help="OpenCV object tracker type")

    args = vars(ap.parse_args())

    video = args['image']

    if not os.path.exists(video):
        print("[ERROR] Video parameter should be an existing file (avi or mp4)")
        exit(84)

    _, extension = os.path.splitext(video)
    if extension not in [".avi", ".mp4"]:
        print("[ERROR] Video parameter should be an existing file (avi or mp4)")
        exit(84)

    if args["tracker"] not in ["csrt", "kcf", "boosting", "mil", "tld", "medianflow", "mosse"]:
        print("[ERROR] tracker parameter is not correct, should be equal to : "
              "csrt, kcf, boosting, mil, tld, medianflow or mosse")
        exit(84)

    trackers_function = {
        "csrt": cv2.TrackerCSRT_create,
        "kcf": cv2.TrackerKCF_create,
        "boosting": cv2.TrackerBoosting_create,
        "mil": cv2.TrackerMIL_create,
        "tld": cv2.TrackerTLD_create,
        "medianflow": cv2.TrackerMedianFlow_create,
        "mosse": cv2.TrackerMOSSE_create
    }

    tracker = trackers_function[args["tracker"]]()

    return video, tracker


def main():
    print("OpenCV version should be 3.4.11, you have : " + str(cv2.__version__))
    video, tracker = get_arguments()
    tracking(video, tracker)


# Main body
if __name__ == '__main__':
    main()
