def linear_search(a, b):
    for index, element in enumerate(a):
        if element == b:
            return index
    return -1


l = [2, 4, 5, 9, 0, 1, 7]
linear_search(l, 9)
