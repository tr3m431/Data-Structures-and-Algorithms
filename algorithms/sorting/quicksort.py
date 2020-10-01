def quicksort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quicksort(less)+equal+quicksort(greater)
    else:
        return array
if __name__ == "__main__":
    
    test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    print quicksort(test)
