# Ejercicio 2

Desarrollar un sistema de visión artificial que permita hacer seguimiento visual por
color de un objeto. El sistema debe ser capaz de detectar el objeto (en el caso de
que se encuentre presente) en cada fotograma.

## Goals

- Blur, para un radio de kernel mínimo de 2 y máximo de 10
- Resize, para un factor de escala mínimo de 0.25 y máximo de 2.5
- rotate/transpsose (Flip + Transpose + Rotate)

## Requirements

* Python 3.7+

* Pillow == 0.0.0

How to install all the requirements :
```bash
$ pip install -r requirements.txt
```

## Usage

```bash
$ python3 visual_tracking.py --video=./media/lapiz.avi --min_values 29 43126 --max_values 88 255 255
```

## Authors

* **Luis Rosario** - *Initial work* - [Luisrosario2604](https://github.com/Luisrosario2604)