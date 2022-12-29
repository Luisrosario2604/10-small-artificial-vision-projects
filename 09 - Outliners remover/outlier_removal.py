#!/usr/bin/python3
# Importing python3 from local, just use "python3 <binary>" if is not the same location

# /
# ** Luis ROSARIO, 2021
# ** Exercise 9 Software
# ** File description:
# ** Cloud of points, radio outliers
# ** https://github.com/Luisrosario2604
# */

# Imports
import argparse
import open3d as o3d
import os


# Function declarations
def radius_outlier_removal(pcd, points, radius):
	# Function to downsample input pointcloud into output pointcloud with a voxel
	voxel_pcd = pcd.voxel_down_sample(voxel_size=0.05)
	tree_pcd = o3d.geometry.KDTreeFlann(voxel_pcd)

	result = []
	for index, point in enumerate(voxel_pcd.points):
		k, _, _ = tree_pcd.search_radius_vector_3d(point, radius)
		if k >= points:
			result.append(index)

	result_cloud = voxel_pcd.select_by_index(result, invert=True)

	# paints all the points to a uniform color. The color is in RGB space, [0, 1] range.
	return result_cloud.paint_uniform_color([51 / 255, 51 / 255, 255 / 255])


def open_3d_file(file, points, radius, output):
	pcd = o3d.io.read_point_cloud(file)

	filtered_point_cloud = radius_outlier_removal(pcd, points, radius)
	
	o3d.visualization.draw_geometries([filtered_point_cloud])
	o3d.io.write_point_cloud("results/" + output, filtered_point_cloud)
	print("Result saved in : results/" + output)


def get_arguments():
	ap = argparse.ArgumentParser()

	ap.add_argument("-i", "--ipc", required=True, help="file path .pcd")
	ap.add_argument("-p", "--points", required=True, help="minimum of number points used", type=int)
	ap.add_argument("-r", "--radius", required=True, help="radius", type=float)
	ap.add_argument("-o", "--opc", required=True, help="output path .pcd")

	args = vars(ap.parse_args())

	file = args["ipc"]
	points = int(args["points"])
	radius = float(args["radius"])
	output = args["opc"]

	if not os.path.exists(file):
		print("[ERROR] File not existing")
		exit(84)
	type = file.split('.')[-1]

	if type not in ['pcd']:
		print("[ERROR] Ipc should be a .pcd")
		exit(84)

	type = file.split('.')[-1]

	return file, points, radius, output


def main():

	file, points, radius, output = get_arguments()
	open_3d_file(file, points, radius, output)


# Main body
if __name__ == '__main__':
	main()
