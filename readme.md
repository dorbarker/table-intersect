# Table Intersect

Takes delimited files and writes a copy of each containing the intersect of the leftmost column of all the files.

## Install

### Python

```sh
python -m pip install git+https://github.com/dorbarker/table-intersect.git`
```
### Conda

```sh
conda install -c dorbarker table-intersect
```

## Usage

```sh
$ table-intersect --help
usage: table-intersect [-h] [--delimiter CHAR] PATH [PATH ...]

Takes delimited files and writes a copy of each 
containing the intersect of the leftmost column of all the files.

positional arguments:
  PATH                  Input files

optional arguments:
  -h, --help            show this help message and exit
  --delimiter CHAR, -d CHAR
                        Table delimiter; the same for all files [TAB]
```

## Example

```sh
table-intersect -d , ex1.csv ex2.csv
# creates ex1.csv.matched ex2.csv.matched
```

```sh
# ex1.csv

name,item
matthias,sword
martin,sword
cluny,tail
asmodeus,fangs
```

```sh
# ex2.csv

matthias,mouse
cluny,rat
mortimer,mouse
```

```sh
# ex1.csv.matched

matthias,sword
cluny,tail
```

```sh
# ex2.csv.matched

matthias,mouse
cluny,rat
```

