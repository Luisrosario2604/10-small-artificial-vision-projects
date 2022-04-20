#!/usr/bin/python3
# Importing python3 from local, just use "python3 <binary>" if is not the same location

# /
# ** Luis ROSARIO, 2021
# ** Exercise 3 Software
# ** File description:
# ** CSV reader
# ** https://github.com/Luisrosario2604
# */


# Imports
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import argparse
import os


# Function declarations
def area2d(detection, groundtruth, output_graphs):
    area_2d_detection = detection[:, 1]
    area_2d_groundtruth = groundtruth[:, 1]

    nan_values_area_2d = np.where(np.isnan(area_2d_detection) == True)[0].size
    area_total = [
        abs(area_2d_detection[i] - area_2d_groundtruth[i])
        for i in range(area_2d_detection.size)
        if not np.isnan(area_2d_detection[i])
        and not np.isnan(area_2d_groundtruth[i])
    ]

    area_numbers = ['[0-50)', '[50-100)', '[100-150)', '[150-200)', '[200-250)', '[>250)']
    area_2d_accuracy = []

    area_total = np.array(area_total)

    accuracy_50 = np.where(area_total < 50)[0].size
    accuracy_100 = np.where(area_total < 100)[0].size - accuracy_50
    accuracy_150 = np.where(area_total < 150)[0].size - accuracy_100 - accuracy_50
    accuracy_200 = np.where(area_total < 200)[0].size - accuracy_150 - accuracy_100 - accuracy_50
    accuracy_250 = np.where(area_total < 250)[0].size - accuracy_200 - accuracy_150 - accuracy_100 - accuracy_50
    accuracy_300 = np.where(area_total >= 250)[0].size

    area_2d_accuracy.append(accuracy_50  / (area_total.size + nan_values_area_2d) * 100)
    area_2d_accuracy.append(accuracy_100 / (area_total.size + nan_values_area_2d) * 100)
    area_2d_accuracy.append(accuracy_150 / (area_total.size + nan_values_area_2d) * 100)
    area_2d_accuracy.append(accuracy_200 / (area_total.size + nan_values_area_2d) * 100)
    area_2d_accuracy.append(accuracy_250 / (area_total.size + nan_values_area_2d) * 100)
    area_2d_accuracy.append(accuracy_300 / (area_total.size + nan_values_area_2d) * 100)

    print("Nan 2D : " + str(nan_values_area_2d / (area_total.size + nan_values_area_2d) * 100) + "%")
    print("area2d accuracy : " + str(area_2d_accuracy))
    print(str(sum(area_2d_accuracy) + nan_values_area_2d / (area_total.size + nan_values_area_2d) * 100) + "%")

    plt.bar('errors', nan_values_area_2d / (area_total.size + nan_values_area_2d) * 100, align='center', color='k')
    plt.bar(area_numbers, area_2d_accuracy, align='center', color='r', edgecolor='k')
    plt.title('Area2D')
    plt.xlabel('Squared feet error')
    plt.ylabel('Percentage of blueprints')
    plt.ylim([0, 100])

    plt.savefig(output_graphs + 'area2D.png', bbox_inches='tight')
    plt.show()


def area3d(detection, groundtruth, output_graphs):
    area_3d_detection = detection[:, 2]
    area_3d_groundtruth = groundtruth[:, 2]

    nan_values_area_3d = np.where(np.isnan(area_3d_detection) == True)[0].size
    area_total = [
        abs(area_3d_detection[i] - area_3d_groundtruth[i])
        for i in range(area_3d_detection.size)
        if not np.isnan(area_3d_detection[i])
        and not np.isnan(area_3d_groundtruth[i])
    ]

    area_numbers = ['[0-50)', '[50-100)', '[100-150)', '[150-200)', '[200-250)', '[>250)']
    area_3d_accuracy = []

    area_total = np.array(area_total)

    accuracy_50 = np.where(area_total < 50)[0].size
    accuracy_100 = np.where(area_total < 100)[0].size - accuracy_50
    accuracy_150 = np.where(area_total < 150)[0].size - accuracy_100 - accuracy_50
    accuracy_200 = np.where(area_total < 200)[0].size - accuracy_150 - accuracy_100 - accuracy_50
    accuracy_250 = np.where(area_total < 250)[0].size - accuracy_200 - accuracy_150 - accuracy_100 - accuracy_50
    accuracy_300 = np.where(area_total >= 250)[0].size

    area_3d_accuracy.append(accuracy_50  / (area_total.size + nan_values_area_3d) * 100)
    area_3d_accuracy.append(accuracy_100 / (area_total.size + nan_values_area_3d) * 100)
    area_3d_accuracy.append(accuracy_150 / (area_total.size + nan_values_area_3d) * 100)
    area_3d_accuracy.append(accuracy_200 / (area_total.size + nan_values_area_3d) * 100)
    area_3d_accuracy.append(accuracy_250 / (area_total.size + nan_values_area_3d) * 100)
    area_3d_accuracy.append(accuracy_300 / (area_total.size + nan_values_area_3d) * 100)

    print("Nan 3D : " + str(nan_values_area_3d / (area_total.size + nan_values_area_3d) * 100) + "%")
    print("area 3d accuracy : " + str(area_3d_accuracy))
    print(str(sum(area_3d_accuracy) + nan_values_area_3d / (area_total.size + nan_values_area_3d) * 100) + "%")

    plt.bar('errors', nan_values_area_3d / (area_total.size + nan_values_area_3d) * 100, align='center', color='k')
    plt.bar(area_numbers, area_3d_accuracy, align='center', color='r', edgecolor='k')
    plt.title('Area3D')
    plt.xlabel('Squared feet error')
    plt.ylabel('Percentage of blueprints')
    plt.ylim([0, 100])

    plt.savefig(output_graphs + 'area3D.png', bbox_inches='tight')
    plt.show()


def complexity(detection, groundtruth, output_graphs):
    complexity_detection = detection[:, 3]
    complexity_groundtruth = groundtruth[:, 3]

    nan_values_complexity = np.where(np.isnan(complexity_detection) == True)[0].size
    complexity_total = [
        abs(complexity_detection[i] - complexity_groundtruth[i])
        for i in range(complexity_detection.size)
        if not np.isnan(complexity_detection[i])
        and not np.isnan(complexity_groundtruth[i])
    ]

    complexity_numbers = ['0', '1', '2', '3', '>=4']
    complexity_accuracy = []

    complexity_total = np.array(complexity_total)

    complexity_accuracy.append(np.where(complexity_total == 0)[0].size / (complexity_total.size + nan_values_complexity) * 100)
    complexity_accuracy.append(np.where(complexity_total == 1)[0].size / (complexity_total.size + nan_values_complexity) * 100)
    complexity_accuracy.append(np.where(complexity_total == 2)[0].size / (complexity_total.size + nan_values_complexity) * 100)
    complexity_accuracy.append(np.where(complexity_total == 3)[0].size / (complexity_total.size + nan_values_complexity) * 100)
    complexity_accuracy.append(np.where(complexity_total >= 4)[0].size / (complexity_total.size + nan_values_complexity) * 100)

    print("Nan complexity : " + str(nan_values_complexity / (complexity_total.size + nan_values_complexity) * 100) + "%")
    print("complexity accuracy : " + str(complexity_accuracy))
    print(str(sum(complexity_accuracy) + nan_values_complexity / (complexity_total.size + nan_values_complexity) * 100) + "%")

    plt.bar('errors', nan_values_complexity / (complexity_total.size + nan_values_complexity) * 100, align='center', color='k')
    plt.bar(complexity_numbers, complexity_accuracy, align='center', color='r', edgecolor='k')
    plt.title('Complexity')
    plt.xlabel('Inches per foot')
    plt.ylabel('Percentage of blueprints')
    plt.ylim([0, 100])

    plt.savefig(output_graphs + 'complexity.png', bbox_inches='tight')
    plt.show()


def compute_stats(inference_original, groundtruth_original, output_graphs):
    df = pd.read_csv(inference_original)
    df = df.replace('-', -1)
    df.to_csv("./datasets/modified_detection.csv", index=False)

    df = pd.read_csv(groundtruth_original)
    df = df.replace('-', -1)
    df.to_csv("./datasets/modified_groundtruth.csv", index=False)

    detection = np.loadtxt("./datasets/modified_detection.csv", delimiter=',', skiprows=1)
    groundtruth = np.loadtxt("./datasets/modified_groundtruth.csv", delimiter=',', skiprows=1)

    detection = np.where(detection == -1, np.nan, detection)
    groundtruth = np.where(groundtruth == -1, np.nan, groundtruth)

    area2d(detection, groundtruth, output_graphs)
    area3d(detection, groundtruth, output_graphs)
    complexity(detection, groundtruth, output_graphs)


def get_arguments():
    ap = argparse.ArgumentParser()

    ap.add_argument("-i", "--inference", required=True, help="Inference")
    ap.add_argument("-g", "--groundtruth", required=True, help="Groundtruth")
    ap.add_argument("-o", "--output_graphs", required=True, help="Output directory (created if doesn't exist)")

    args = vars(ap.parse_args())

    inference_original = args["inference"]
    groundtruth_original = args["groundtruth"]
    output_graphs = args["output_graphs"]

    if not os.path.exists(inference_original):
        print("[ERROR] Inference should be an existing file (csv)")
        exit(84)

    if not os.path.exists(groundtruth_original):
        print("[ERROR] Groundtruth should be an existing file (csv)")
        exit(84)

    _, extension = os.path.splitext(inference_original)
    if extension != ".csv":
        print("[ERROR] Inference should be an existing file (csv)")
        exit(84)

    _, extension = os.path.splitext(groundtruth_original)
    if extension != ".csv":
        print("[ERROR] Groundtruth should be an existing file (csv)")
        exit(84)

    if not os.path.isdir(output_graphs):
        output_graphs = os.getcwd() + "/" + output_graphs
        os.mkdir(output_graphs)
    if output_graphs[-1] != "/":
        output_graphs += "/"

    return inference_original, groundtruth_original, output_graphs


def main():
    inference_original, groundtruth_original, output_graphs = get_arguments()
    compute_stats(inference_original, groundtruth_original, output_graphs)


# Main body
if __name__ == '__main__':
    main()
