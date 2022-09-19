# Name:
# Email ID:

from math import inf


def get_max_of_min(list_of_num_tuples):
    if len(list_of_num_tuples) == 0:
        return None

    elif len(list_of_num_tuples) == 1:
        minimum = inf
        for num in list_of_num_tuples[0]:
            if num < minimum:
                minimum = num
        return minimum

    else:
        num_tuples = len(list_of_num_tuples)
        minimums = [inf] * num_tuples

        for idx in range(num_tuples):
            for num in list_of_num_tuples[idx]:
                if num < minimums[idx]:
                    minimums[idx] = num
        
        maximum = -inf
        for num in minimums:
            if num > maximum:
                maximum = num

        return maximum