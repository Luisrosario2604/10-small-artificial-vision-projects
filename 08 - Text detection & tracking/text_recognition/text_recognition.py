#!/usr/bin/python3
# Importing python3 from local, just use "python3 <binary>" if is not the same location

# /
# ** Luis ROSARIO, 2021
# ** Exercise 8.1 Software
# ** File description:
# ** Text recognition for cars
# ** https://github.com/Luisrosario2604
# */

# Imports
import argparse
import os
import imghdr
from skimage.segmentation import clear_border
import pytesseract
import numpy as np
import imutils
import cv2


# Global values
minAR = 4
maxAR = 5
debug = False


# Function declarations
def build_tesseract_options(psm=7):
	alphanumeric = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
	options = "-c tessedit_char_whitelist={}".format(alphanumeric)
	options += " --psm {}".format(psm)
	return options


def get_blackhat(gray):
	rectKern = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))
	blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rectKern)
	return blackhat, rectKern


def get_light(gray):
	squareKern = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
	light = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, squareKern)
	light = cv2.threshold(light, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
	return light


def get_gradx(blackhat):
	gradX = cv2.Sobel(blackhat, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
	gradX = np.absolute(gradX)
	(minVal, maxVal) = (np.min(gradX), np.max(gradX))
	gradX = 255 * ((gradX - minVal) / (maxVal - minVal))
	gradX = gradX.astype("uint8")
	return gradX


def get_thresh(gradX, rectKern, light):
	gradX = cv2.GaussianBlur(gradX, (5, 5), 0)
	gradX = cv2.morphologyEx(gradX, cv2.MORPH_CLOSE, rectKern)
	thresh = cv2.threshold(gradX, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
	thresh = cv2.erode(thresh, None, iterations=2)
	thresh = cv2.dilate(thresh, None, iterations=2)
	thresh = cv2.bitwise_and(thresh, thresh, mask=light)
	thresh = cv2.dilate(thresh, None, iterations=2)
	thresh = cv2.erode(thresh, None, iterations=1)
	return thresh


def get_cnt(thresh, keep=5):
	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:keep]
	return cnts


def locate_license_plate(gray, candidates, clearBorder=False):
	plate_countour = None
	roi = None
	for c in candidates:
		(x, y, w, h) = cv2.boundingRect(c)
		ar = w / float(h)
		if minAR <= ar <= maxAR:
			plate_countour = c
			licensePlate = gray[y:y + h, x:x + w]
			roi = cv2.threshold(licensePlate, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
			if clearBorder:
				roi = clear_border(roi)
			break
	return roi, plate_countour


def locate_candidates(gray):
	blackhat, rectKern = get_blackhat(gray)
	light = get_light(gray)
	gradX = get_gradx(blackhat)
	thresh = get_thresh(gradX, rectKern, light)

	cv2.imshow("Blackhat", blackhat)
	cv2.imshow("Light", light)
	cv2.imshow("Gradient X", gradX)
	cv2.imshow("Blur", thresh)
	return thresh, blackhat, light, gradX


def smooth_image(image):
	blur = cv2.medianBlur(image, 1)
	thresh = cv2.threshold(blur, 125, 255, cv2.THRESH_BINARY_INV)[1]

	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
	close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=1)

	# kernel = np.ones((3, 3), np.uint8)
	# denoised = cv2.morphologyEx(close, cv2.MORPH_CLOSE, kernel)
	# erosion = cv2.erode(close, kernel, iterations=1)
	return 255 - image


def find_and_ocr(image, psm=7, clearBorder=False):
	plate_number = None
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	thresh, blackhat, light, gradX = locate_candidates(gray)
	candidates = get_cnt(thresh)
	(lp, plate_countour) = locate_license_plate(gray, candidates, clearBorder=clearBorder)
	if lp is None:
		candidates = get_cnt(blackhat)
		(lp, plate_countour) = locate_license_plate(gray, candidates, clearBorder=clearBorder)
	if lp is None:
		candidates = get_cnt(light)
		(lp, plate_countour) = locate_license_plate(gray, candidates, clearBorder=clearBorder)
	if lp is None:
		candidates = get_cnt(gradX)
		(lp, plate_countour) = locate_license_plate(gray, candidates, clearBorder=clearBorder)
	if lp is not None:
		options = build_tesseract_options(psm=psm)
		cv2.imshow("Before smooth", lp)
		lp = smooth_image(lp)
		cv2.imshow("After smooth", lp)
		plate_number = pytesseract.image_to_string(lp, config=options)
	return plate_number, plate_countour


def cleanup_text(text):
	return "".join([c if ord(c) < 128 else "" for c in text]).strip()


def recognition_image(file):
	image = cv2.imread(file)
	image = imutils.resize(image, width=600)
	(plate_number, plate_countour) = find_and_ocr(image)

	if plate_number is not None and plate_countour is not None:
		box = cv2.boxPoints(cv2.minAreaRect(plate_countour))
		box = box.astype("int")
		cv2.drawContours(image, [box], -1, (0, 255, 0), 2)
		(x, y, w, h) = cv2.boundingRect(plate_countour)
		cv2.putText(image, cleanup_text(plate_number), (x, y - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
		print("PLATE {}".format(plate_number))
		cv2.imshow("Final result", image)
		cv2.waitKey(0)
	else:
		print("Nothing found")

	cv2.destroyAllWindows()
	return


def text_recognition(file, file_type):

	if file_type == "image":
		recognition_image(file)


def get_arguments():
	ap = argparse.ArgumentParser()

	ap.add_argument("-i", "--image", required=False, help="image")
	ap.add_argument("-v", "--video", required=False, help="video")

	args = vars(ap.parse_args())

	image = args["image"]
	video = args["video"]

	if image is None and video is None:
		print("[ERROR] You should give a video or an image")
		exit(84)

	if image is not None and video is not None:
		print("[ERROR] You should give ONLY a video or an image")
		exit(84)

	if video is not None:
		if not os.path.exists(video):
			print("[ERROR] Video not existing")
			exit(84)

		type = imghdr.what(video)

		if type not in ['avi', 'mp4']:
			print("[ERROR] Only avi and mp4 accepted for videos")
			exit(84)

		file = video
		file_type = 'video'

	if image is not None:
		if not os.path.exists(image):
			print("[ERROR] Image not existing")
			exit(84)
		type = imghdr.what(image)

		if type not in ['gif', 'jpeg', 'png', 'tiff', 'bmp']:
			print("[ERROR] Image should be an image")
			exit(84)

		file = image
		file_type = 'image'

	return file, file_type


def main():

	file, file_type = get_arguments()
	text_recognition(file, file_type)


# Main body
if __name__ == '__main__':
	main()
