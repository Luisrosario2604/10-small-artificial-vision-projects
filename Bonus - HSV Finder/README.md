# Bonus

#### 👨‍🎓 This project was carried out during my master's degree in computer vision at URJC - Madrid

Implementation of a programme to assist in the determination of HSV parameters

## Keys

- 'S' save values hsv in np array file
- 'Q' to exit

## Requirements

* Python 3.7+

* Numpy == 1.21.3
* Opencv_python == 4.5.3.56


How to install all the requirements :
```bash
$ pip install -r requirements.txt
```

## Usage

```bash
$ python find_hsv.py --min_values 49 43 126 --max_values 88 255 255 -f=./imgs/picklerick.jpeg
```

## Results

<p align="center">
  <img src="./imgs/result.png">
</p>
<p align="center">
  <i>Result of the hsv finder</i>
</p>

## Authors

* **Luis Rosario** - *Initial work* - [Luisrosario2604](https://github.com/Luisrosario2604)