def quick_sort(data):
    if len(data) <= 1:
        return data
    pivot = data[0]
    small = [i for i in data[1:] if i <= pivot]
    large = [i for i in data[1:] if i > pivot]
    small = quick_sort(small)
    large = quick_sort(large)
    return small + [pivot] + large

if __name__ == '__main__':
    data = [1, 4, 0, 6, 7]
    print(quick_sort(data))
