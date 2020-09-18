def bubble_sort(data):
    for i in range(len(data)):
        for j in range(len(data) - (i + 1)):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

if __name__ == '__main__':
    data = [1, 4, 0, 6, 7]
    print(bubble_sort(data))
