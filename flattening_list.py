# -*- coding: utf-8 -*-
"""flattening_list.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eFg2J-l-eyi0QExpY7gwG5vBQZ6IUTOX
"""

j=[[[ 23, 47, 77, "intelligence"],[ 33, 28, "artificial", 20],[ 32, 45, 17, "strawberry"]],[[ 12, 37, 6],[ 1, 34, 25, "pear", "apple"],[ 2, 53, 51, "water"]]]

flatten_j = [i for l in j for e in l for i in e]

print(flatten_j)