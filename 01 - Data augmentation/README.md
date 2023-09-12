# Exercise 1

#### 👨‍🎓 This project was carried out during my master's degree in computer vision at URJC - Madrid 

Develop a data augmentation module for convolutional networks in Python.

## Goals

- Blur, for a minimum kernel radius of 2 and a maximum kernel radius of 10
- Resize, for a minimum scale factor of 0.25 and a maximum of 2.5
- rotate/transpose (Flip + Transpose + Rotate)

## Requirements

* Python 3.7+

* Pillow ~= 9.1.0

How to install all the requirements :

```bash
pip3 install -r requirements.txt
```

## Usage

```bash
python data_augmentation.py --input_dataset=./tiny_imagenet --factor=20 --output_dataset=./augmented_tiny_imagenet
```

## Results

<p align="center">
  <img src="./imgs/result.jpg">
</p>
<p align="center">
  <i>Example of 4 images generated from the data augmentation</i>
</p>

## Authors

* **Luis Rosario** - *Member 1* - [Luisrosario2604](https://github.com/Luisrosario2604)