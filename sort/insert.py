def insert_sort(data):
    for i in range(len(data)):
        buf = data[i]
        j = i - 1
        while (j >= 0) and (data[j] > buf):
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = buf
    return data

if __name__ == '__main__':
    data = [1, 4, 0, 6, 7]
    print(insert_sort(data))
