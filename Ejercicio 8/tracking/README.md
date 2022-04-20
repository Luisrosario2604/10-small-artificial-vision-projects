# Ejercicio 8.2

Hacer uso del módulo de seguimiento visual de OpenCV (tracking) para
hacer seguimiento de un objeto o región de interés en una secuencia de
video

## Keys

- 'Q' para salir

## Virtual env

####You need to start the virtual env to get the specific OpenCV version (3.4.11.45)

Create virtual env
```bash
$ pip install virtualenv
$ python -m venv .
```

Start virtual env
```bash
$ source bin/activate
```

Exit virtual env
```bash
$ deactivate
```

## Requirements

* Python 3.9.2

* numpy == 1.22.3
* opencv-contrib-python == 3.4.11.45


How to install all the requirements (You need to be in the virtual env !) :
```bash
$ pip install -r requirements.txt
```

## Usage

Start tracking with default tracker (default kcf)
```bash
$ python visual_tracking_cv.py --image=media/road1.mp4
```

Start tracking with specific tracker
```bash
$ python visual_tracking_cv.py --image=media/road1.mp4 --tracker=mose
```

Tracker available :
* csrt
* kcf
* boosting
* mil
* tld
* medianflow
* mosse

## Authors

* **Luis Rosario** - *Initial work* - [Luisrosario2604](https://github.com/Luisrosario2604)