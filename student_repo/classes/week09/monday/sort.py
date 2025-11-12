def combine(left, right):
    array = []
    i = j = 0  # pointers for each list

    # merge until one list runs out
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array.append(left[i])
            i += 1
        else:
            array.append(right[j])
            j += 1

    # add remaining elements (if any)
    array.extend(left[i:])
    array.extend(right[j:])

    return array


l_cur = [1, 7, 27, 36]
r_cur = [3, 6, 15, 39]

combined = combine(l_cur, r_cur)
print(combined)
