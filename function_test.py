import decorators


@decorators.logger
def flat_generator(list_of_list):
    if isinstance(list_of_list, list):
        for elem in list_of_list:
            for sub_elem in flat_generator(elem):
                yield sub_elem
    else:
        yield list_of_list


if __name__ == "__main__":

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]
    print(list(flat_generator(list_of_lists_2)))