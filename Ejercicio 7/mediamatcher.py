#!/usr/bin/python3
# Importing python3 from local, just use "python3 <binary>" if is not the same location

# /
# ** Luis ROSARIO, 2021
# ** Exercise 7 Software
# ** File description:
# ** Media matcher (moovies)
# ** https://github.com/Luisrosario2604
# */

# Imports
import argparse
import os
import imghdr
import cv2


# Global variables
valid_images = [".jpg", ".gif", ".png", ".tga", ".jpeg"]

# Function declarations


def sift_detection(query, image):
	img1 = cv2.imread(query, cv2.IMREAD_GRAYSCALE)  # queryImage
	img2 = cv2.imread(image, cv2.IMREAD_GRAYSCALE)  # trainImage
	# Initiate SIFT detector
	sift = cv2.SIFT_create()
	# find the keypoints and descriptors with SIFT
	kp1, des1 = sift.detectAndCompute(img1, None)
	kp2, des2 = sift.detectAndCompute(img2, None)
	# BFMatcher with default params
	bf = cv2.BFMatcher()
	matches = bf.knnMatch(des1, des2, k=2)
	# Apply ratio test
	good = []
	for m, n in matches:
		if m.distance < 0.75 * n.distance:
			good.append([m])
	# cv22.drawMatchesKnn expects list of lists as matches.
	img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

	return len(good), img3


def mediamatcher(query, images_covers):

	minimum_score = 40
	best_match = None
	best_score = 0

	for image in images_covers:
		score, img = sift_detection(query, image[0])
		if score >= best_score and score >= minimum_score:
			best_match = img
			best_score = score
		print(str(query) + "   -   " + str(image[0]) + "   -   Score matches : " + str(score))

	if best_score == 0:
		print("None of the covers found ! Should have more than 40 matches !")
		return

	cv2.imshow('Number of matches : ' + str(best_score), best_match)

	while True:
		key = cv2.waitKey(1)
		if key == ord('q'):
			break

	cv2.destroyAllWindows()
	return


def get_images(input_dir):
	images = []

	for path in os.listdir(input_dir):
		ext = os.path.splitext(path)[1]
		if ext.lower() not in valid_images:
			continue

		filename = os.path.basename(path)
		filename = filename[::-1]
		filename = filename[filename.find('.') + 1:]
		filename = filename[::-1]

		images.append([os.path.join(input_dir, path), filename, ext])

	if not images:
		print("[ERROR] Not even one image found in the input directory")
		exit(84)

	return images


def get_arguments():
	ap = argparse.ArgumentParser()

	ap.add_argument("-q", "--query", required=True, help="Original image")
	ap.add_argument("-c", "--covers", required=True, help="Image collection")

	args = vars(ap.parse_args())

	query = args["query"]
	covers = args["covers"]

	if not os.path.exists(query):
		print("[ERROR] Original image should be an image")
		exit(84)

	type = imghdr.what(query)

	if type not in ['gif', 'jpeg', 'png', 'tiff', 'bmp']:
		print("[ERROR] Original image should be an image")
		exit(84)

	if not os.path.isdir(covers):
		print("[ERROR] Image collection should be an existing directory")
		exit(84)

	return query, covers


def main():

	query, covers = get_arguments()
	images_covers = get_images(covers)
	mediamatcher(query, images_covers)


# Main body
if __name__ == '__main__':
	main()
