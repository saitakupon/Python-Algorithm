def select_sort(data):
    for i in range(len(data)):
        min = i
        for j in range((i + 1), len(data)):
            if data[min] > data[j]:
                min = j
        data[i], data[min] = data[min], data[i]
    return data

if __name__ == '__main__':
    data = [1, 4, 0, 6, 7]
    print(select_sort(data))
