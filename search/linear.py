def linear_search(data, value):
    for i in range(len(data)):
        if data[i] == value:
            return i
    return -1

if __name__ == '__main__':
    data = [i for i in range(10)]
    print(linear_search(data, 2))
