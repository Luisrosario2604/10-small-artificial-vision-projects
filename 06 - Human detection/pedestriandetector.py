#!/usr/bin/python3
# Importing python3 from local, just use "python3 <binary>" if is not the same location

# /
# ** Luis ROSARIO, 2021
# ** Exercise 6 Software
# ** File description:
# ** Pedestrian detector
# ** https://github.com/Luisrosario2604
# */

# Imports
import argparse
import cv2
import os


# Function declarations
def detect_people(img, hog):
    rects, weights = hog.detectMultiScale(img,
                                          winStride=(8, 8),
                                          padding=(32, 32),
                                          scale=1.05)

    for (x, y, w, h) in rects:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return img


def pedestriandetector(images, out):
    fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    out = cv2.VideoWriter(out, fourcc, 33.0, (640, 480))

    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    nb_images = len([name for name in os.listdir(images) if os.path.isfile(os.path.join(images, name))])
    print(nb_images)
    for i in range(nb_images):
        nb_zeros = "00000000"
        nb_zeros = nb_zeros[:-len(str(i))]

        filename = images + "/" + "image_" + str(nb_zeros) + str(i) + "_0.png"
        print(filename)
        frame = cv2.imread(filename)
        frame = detect_people(frame, hog)
        out.write(frame)
        cv2.imshow('Pedestrian', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    out.release()
    cv2.destroyAllWindows()


def get_args():
    ap = argparse.ArgumentParser()

    ap.add_argument("-i", "--images", required=True, help="path to where the image file resides")
    ap.add_argument("-o", "--out", required=True, help="path to where the result will be save")

    args = vars(ap.parse_args())

    return args['images'], args['out']


def main():
    images, out = get_args()
    pedestriandetector(images, out)


# Main body
if __name__ == '__main__':
    main()
