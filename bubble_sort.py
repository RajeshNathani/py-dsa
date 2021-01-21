def bubble(elements):
    size = len(elements)
    for i in range(size-1):
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]


if __name__ == "__main__":
    elements = [3, 5, 1, 2, 7, 9]
    bubble(elements)
    print(elements)
