# Python Line Count

## Task

Write a Python program that takes a directory as a required argument and a filename extension as optional argument that defaults to “.txt”. The program should locate all files with the given extension in the given directory and all its subdirectories to produce a list of all matching files with the numbers of lines within the file. The program should also output the total number of lines and the average number of lines per file.

## Solution

The first step is to collect every files in the directory and all its subdirectories with given extensions. Generally, `glob.glob()`can get the result by one line. But a BFS solution is also presented in the code.

After that, every files in the list will be opened and counted the number of lines. Here, the method I use is 

```python
file_d = open(directory, 'r')
num_lines = sum(1 for _ in file_d)
file_d.close() 
```

## Usage

The result will be printed by executing the following codes:

```python
import FileCollection from file_count
file_collection = FileCollection()
file_collection.count(directory, extension)
```

## Test

There are four unit tests in *file_test.py*, which will test whether the code works properly in different situation. The unit test can be called by

```shell
python -m unittest file_test.py
```

## Pylint Test

The codes also passed Pylint test with a 10.00/10 rating.


