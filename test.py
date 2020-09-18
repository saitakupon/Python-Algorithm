from search.linear import linear_search
from search.binary import binary_search
from sort.select import select_sort
from sort.insert import insert_sort
from sort.bubble import bubble_sort
from sort.merge import merge_sort
from sort.quick import quick_sort

data1 = [i for i in range(10)]
print(linear_search(data1, 4))
print(binary_search(data1, 4))

data2 = [1, 4, 0, 6, 7]
print(select_sort(data2))
print(insert_sort(data2))
print(bubble_sort(data2))
print(merge_sort(data2))
print(quick_sort(data2))
