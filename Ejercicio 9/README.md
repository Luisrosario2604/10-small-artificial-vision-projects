# Ejercicio 9

Desarrollar un método para Open3D que permita filtrar outliers en una nube de
puntos 3D. Existen diferentes tipos de filtrado de outliers en la literatura, en este
ejercicio centraremos nuestra atención en el filtrado de outliers por radio (explicado
en clase, módulo Python++).

## Requirements

* Python 3.7+

* open3d == 0.15.2
* open3d_python == 0.3.0.0



How to install all the requirements :
```bash
$ pip install -r requirements.txt
```

## Usage

Usage of main algorithm
```bash
$ python outlier_removal.py --ipc=data/2.pcd --points=16 --radius=0.05 --opc=resulting_could.pcd
```

Bonus : If you want to visualize a 3D file
```bash
$ python visualization.py --file=data/2.pcd
```

## Authors

* **Luis Rosario** - *Initial work* - [Luisrosario2604](https://github.com/Luisrosario2604)