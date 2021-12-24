# Ejercicio 1

Desarrollar un módulo de aumentado de datos para redes de convolución en
Python.

## Goals

- Blur, para un radio de kernel mínimo de 2 y máximo de 10
- Resize, para un factor de escala mínimo de 0.25 y máximo de 2.5
- rotate/transpsose (Flip + Transpose + Rotate)

## Requirements

* Python 3.7+

* Pillow == 8.4.0

How to install all the requirements :
```bash
$ pip install -r requirements.txt
```

## Usage

```bash
$ python3 data_augmentation.py --input_dataset=./tiny_imagenet --factor=20 --output_dataset=./augmented_tiny_imagenet
```

## Authors

* **Luis Rosario** - *Initial work* - [Luisrosario2604](https://github.com/Luisrosario2604)