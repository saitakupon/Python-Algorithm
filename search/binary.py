def binary_search(data, value):
    min = 0
    max = len(data) - 1
    while min <= max:
        mid = (min + max) // 2
        if data[mid] == value:
            return mid
        elif data[mid] < value:
            min = mid + 1
        else:
            max = mid - 1
    return -1

if __name__ == '__main__':
    data = [i for i in range(10)]
    print(binary_search(data, 2))
