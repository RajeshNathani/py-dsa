def binary_search(num_list, number):
    num_list.sort()
    left_index = 0
    right_index = len(num_list)-1
    while left_index <= right_index:
        mid_index = (left_index+right_index)//2
        mid_num = num_list[mid_index]
        if mid_num == number:
            return mid_index
        if number < mid_num:
            right_index = mid_num-1
        else:
            left_index = mid_num+1
    return -1


print(binary_search([1, 4, 5, 9, 2, 3], 5))
