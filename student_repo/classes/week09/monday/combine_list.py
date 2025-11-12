#create a function that only uses the combine method to sort a list

array_a = [5,4,3,2,1]


def combine(array_to_sort):
    array = []
    for i in range(len(array_to_sort)):
        if array_to_sort[i] < array_to_sort[i]:
            array.append(array_to_sort[i])
        elif array_to_sort[i] < array_to_sort[i-1]:
            array.combine(array_to_sort[i])
    return array

sorted_array = combine(array_a)
print(sorted_array)