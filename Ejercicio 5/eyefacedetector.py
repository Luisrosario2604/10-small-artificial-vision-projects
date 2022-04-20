#!/usr/bin/python3
# Importing python3 from local, just use "python3 <binary>" if is not the same location

# /
# ** Luis ROSARIO, 2021
# ** Exercise 5 Software
# ** File description:
# ** Eyes and Face detection
# ** https://github.com/Luisrosario2604
# */

# Imports
import argparse
import cv2
import os

# Global variables

# Class declarations

# Function declarations


def detect_eyes_and_faces(img, face_cascade, eye_cascade):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,
                                          scaleFactor=1.1,
                                          minNeighbors=5,
                                          minSize=(30, 30),
                                          flags=cv2.CASCADE_SCALE_IMAGE)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y: y + h, x: x + w]
        roi_color = img[y: y + h, x: x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    return img


def eyefacedetector(video, out):
    face_cascade = cv2.CascadeClassifier("./haarcascade/haarcascade_frontalface_default.xml")
    eye_cascade = cv2.CascadeClassifier("./haarcascade/haarcascade_eye.xml")

    cap = cv2.VideoCapture(video)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH )
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT )
    fps = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    out = cv2.VideoWriter(out, fourcc, int(fps), (int(width), int(height)))

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            frame = detect_eyes_and_faces(frame, face_cascade, eye_cascade)
            cv2.imshow('frame', frame)
            out.write(frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()


def get_arguments():
    ap = argparse.ArgumentParser()

    ap.add_argument("-v", "--video", required=True, help="path to where the video file resides")
    ap.add_argument("-o", "--out", required=True, help="path to where the result will be save")

    args = vars(ap.parse_args())

    print(args['video'])
    print(args['out'])

    video = args['video']
    out = args['out']

    if not os.path.exists(video):
        print("[ERROR] Video parameter should be an existing file (avi or mp4)")
        exit(84)

    _, extension = os.path.splitext(video)
    if extension not in [".avi", ".mp4"]:
        print("[ERROR] Video parameter should be an existing file (avi or mp4)")
        exit(84)

    _, extension = os.path.splitext(out)
    if extension not in [".avi", ".mp4"]:
        print("[ERROR] Out parameter should be a file with avi or mp4 extension")
        exit(84)

    return video, out


def main():
    video, out = get_arguments()
    eyefacedetector(video, out)


# Main body
if __name__ == '__main__':
    main()
