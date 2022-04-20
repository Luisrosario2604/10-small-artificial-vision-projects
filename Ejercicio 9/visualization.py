#!/usr/bin/python3
# Importing python3 from local, just use "python3 <binary>" if is not the same location

# /
# ** Luis ROSARIO, 2021
# ** Exercise 9 Software Bonus
# ** File description:
# ** Visualization of cloud of points
# ** https://github.com/Luisrosario2604
# */

# Imports
import argparse
import open3d as o3d
import os


# Function declarations
def open_3d_file(file):
	pcd = o3d.io.read_point_cloud(file)
	o3d.visualization.draw_geometries([pcd])


def get_arguments():
	ap = argparse.ArgumentParser()

	ap.add_argument("-f", "--file", required=False, help="file path .pcd")

	args = vars(ap.parse_args())

	file = args["file"]

	if not os.path.exists(file):
		print("[ERROR] File not existing")
		exit(84)
	type = file.split('.')[-1]

	if type not in ['pcd']:
		print("[ERROR] File should be a .pcd")
		exit(84)

	return file


def main():

	file = get_arguments()
	open_3d_file(file)


# Main body
if __name__ == '__main__':
	main()
