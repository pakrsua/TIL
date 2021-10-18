def merge(left, right):
    result = []
    while len(left) > 0 or len(right):
        if len(left) > 0 and len(right):
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        if len(left) > 0:
            result.extend(left)
        if len(right) > 0:
            result.extend(right)
        return result

def merge_sort(m):

    if len(m) <= 1:
        return m

    left = m[:len(m)//2]
    right = m[len(m)//2:]
    print(left, right)
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

m = [1, 3, 5, 7, 9, 8, 4, 6, 2, 0]
print(merge_sort(m))