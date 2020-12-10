from itertools import combinations


def elements_that_sum_to(list_, sum_result, number_of_elements_to_sum):
    result = []
    for items in combinations(list_, number_of_elements_to_sum):
        if sum(items) == sum_result:
            result = items
            break
    return result


def contiguous_elements_that_sum_to(
        list_, sum_result, number_of_elements_to_sum):
    result = []
    for i in range(len(list_)-number_of_elements_to_sum):
        if sum(list_[i:i+number_of_elements_to_sum]) == sum_result:
            result = list_[i:i+number_of_elements_to_sum]
            break
    return result


def multiple_list_elements(list_):
    result = 1
    for element in list_:
        result *= element

    return result
