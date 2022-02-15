# PMGCodingTest

## Problem Statement
Write a command line program that takes several CSV files as arguments. Each CSV file (found in the fixtures directory of this repo) will have the same columns. Your script should output a new CSV file to stdout that contains the rows from each of the inputs along with an additional column that has the filename from which the row came (only the file's basename, not the entire path). Use filename as the header for the additional column.

## Language and Third-Party Library
- Python 3.6.5
- Pandas

## Input Command Line
```python
$ python ./csv-combiner.py ./fixtures/accessories.csv ./fixtures/clothing.csv > combined.csv
```
OR
```python
$ python ./csv-combiner.py ./fixtures/accessories.csv ./fixtures/clothing.csv ./fixtures/household_cleaners.csv > combined.csv
```


