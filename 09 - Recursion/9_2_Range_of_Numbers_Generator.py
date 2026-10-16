def range_of_numbers(start_num, end_num):
    if end_num < start_num:
        return []
    count_list = range_of_numbers(start_num, end_num -1)
    count_list.append(end_num)
    return count_list