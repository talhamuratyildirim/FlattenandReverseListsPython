# -*- coding: utf-8 -*-
"""reversing_lists.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rH3dH_Il114xbH8teWQiivwujU-sjaQy
"""

l = [[1, 2], [3, 4], [5, 6, 7]]

l_reversed = []

for e in range(len(l)):         # This for loop reverses the lists in the list "l"
  l_reversed.append(l[-(e+1)])

print(l_reversed)

l_reversed2 = [e[::-1] for e in l_reversed]     # This for loop reverses the each list's inside

print(l_reversed2)