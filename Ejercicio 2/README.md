# Ejercicio 2

Desarrollar un sistema de visión artificial que permita hacer seguimiento visual por
color de un objeto. El sistema debe ser capaz de detectar el objeto (en el caso de
que se encuentre presente) en cada fotograma.

## Goals

- Aplicar un filtro gaussiano al fotograma para eliminar ruido
- Convertir el fotograma al espacio de color HSV
- Segmentar el fotograma utilizando el rango de color seleccionado
- Eliminar pequeños focos de ruido en la imagen resultante
- Detectar los distintos contornos que aparecen en la imagen y quedarse
con aquel que presente mayor área

## Requirements

* Python 3.7+

* numpy == 1.21.3
* opencv_python == 4.5.3.56
* Pillow == 8.4.0

How to install all the requirements :
```bash
$ pip install -r requirements.txt
```

## Usage

```bash
$ python visual_tracking.py --video=./media/lapiz.avi --min_values 29 49 126 --max_values 88 255 255 --output=result.avi
```

## Authors

* **Luis Rosario** - *Initial work* - [Luisrosario2604](https://github.com/Luisrosario2604)