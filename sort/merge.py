def merge_sort(data):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return merge(left, right)

def merge(left, right):
    ans = []
    i = 0
    j = 0
    while (i < len(left)) and (j < len(right)):
        if left[i] <= right[j]:
            ans.append(left[i])
            i += 1
        else:
            ans.append(right[j])
            j += 1
    if i < len(left):
        ans.extend(left[i:])
    if j < len(right):
        ans.extend(right[j:])
    return ans

if __name__ == '__main__':
    data = [1, 4, 0, 6, 7]
    print(merge_sort(data))
