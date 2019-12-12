# -*- coding: utf-8 -*-

'''
Using Python 3 f-string to make a times table string.
'''

import itertools
import pytablewriter
import pyperclip


def times_table(int_start=1, int_end=9):
    '''
    '''

    int_end = int_end + 1

    list_tbl = [
        [f'{x} × {y} = {x * y}' for y in range(int_start, int_end)]
        for x in range(int_start, int_end)
    ]

    # # get max str length
    # chain = itertools.chain.from_iterable(list_tbl)

    # list_temp = list(chain)

    # list_temp = [len(i) for i in list_temp]

    # int_len = max(list_temp)

    # # set every string to max length, left justified
    # for i, j in enumerate(list_tbl):

    #     for k, v in enumerate(j):

    #         j[k] = v.ljust(int_len)

    #     list_tbl[i] = j

    return zip(*list_tbl)


# on windows, you must place the pytablewriter code inside this
if __name__ == '__main__':

    int_start = 1

    int_end = 9

    # make a times table from 1 to 9
    list_tbl = list(times_table(int_start, int_end))

    list_header = list(range(int_start, int_end + 1))

    writer = pytablewriter.RstGridTableWriter()

    writer.headers = list_header

    writer.value_matrix = list_tbl

    # copy table string to clipboard
    pyperclip.copy(writer.dumps())

    writer.write_table()
