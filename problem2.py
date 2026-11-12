import csv
import numpy as np
import pandas as pd

def read_file(path):
    """Read comma-separated numbers from a file and print each row's sum.

    >>> read_file("test_numbers.csv")
    6
    15
    24
    """
    with open(path, 'r') as f:
        reader = csv.reader(f)

        for line in reader:
            data = np.array(line, dtype=int)
            print(data.sum())

   