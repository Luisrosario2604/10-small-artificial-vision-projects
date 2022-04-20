#!/usr/bin/python3
# Importing python3 from local, just use "python3 <binary>" if is not the same location

# /
# ** Luis ROSARIO, 2021
# ** Exercise 1 Software
# ** File description:
# ** Generating new images from one
# ** https://github.com/Luisrosario2604
# */

# Imports
import argparse
import os
from PIL import Image
from PIL import ImageFilter
from random import randint

# Global variables
valid_images = [".jpg", ".gif", ".png", ".tga", ".jpeg"]

# Function declarations


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

	ap.add_argument("-i", "--input_dataset", required=True, help="Input directory")
	ap.add_argument("-o", "--output_dataset", required=True, help="Output directory (created if doesn't exist")
	ap.add_argument("-f", "--factor", required=True, help="Number of images generated from one")

	args = vars(ap.parse_args())

	input_dir = args["input_dataset"]
	output_dir = args["output_dataset"]

	if not args["factor"].isdigit():
		print("[ERROR] The first agument should be an integer <= 50")
		exit(84)

	factor = int(args["factor"])

	if factor <= 0 or factor > 50:
		print("[ERROR] The first argument should be an integer between 1 and 50")
		exit(84)

	if not os.path.isdir(input_dir):
		print("[ERROR] Input dataset argument should be an existing directory")
		exit(84)

	if not os.path.isdir(output_dir):
		end_dir = os.getcwd() + "/" + args["output_dataset"]
		os.mkdir(end_dir)

	if input_dir[-1] != "/":
		input_dir += "/"

	if output_dir[-1] != "/":
		output_dir += "/"

	return factor, input_dir, output_dir


def generate_images(factor, images, output_dir):

	for image in images:
		img_default = Image.open(image[0])

		for i in range(factor):
			new_img = img_default

			if randint(0, 1) == 0:
				new_img = new_img.filter(ImageFilter.GaussianBlur(radius=randint(2, 10)))
			if randint(0, 1) == 0:
				param_resize = (float(randint(25, 250)) / 100)
				width, height = (new_img.width * param_resize, new_img.height * param_resize)
				new_img = new_img.resize((int(width), int(height)))

			if randint(0, 1) == 0:
				rdm_tmp = randint(1, 6)

				if rdm_tmp == 1:
					new_img = new_img.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)
				elif rdm_tmp == 2:
					new_img = new_img.transpose(method=Image.Transpose.FLIP_TOP_BOTTOM)
				elif rdm_tmp == 3:
					new_img = new_img.transpose(method=Image.Transpose.ROTATE_90)
				elif rdm_tmp == 4:
					new_img = new_img.transpose(method=Image.Transpose.ROTATE_180)
				elif rdm_tmp == 5:
					new_img = new_img.transpose(method=Image.Transpose.ROTATE_270)
				else:
					new_img = new_img.transpose(method=Image.Transpose.TRANSPOSE)

			new_img.save(output_dir + image[1] + "-" + str(i + 1) + image[2])


def main():

	factor, input_dir, output_dir = get_arguments()
	images = get_images(input_dir)
	generate_images(factor, images, output_dir)

	print("Done !")


# Main body
if __name__ == '__main__':
	main()
