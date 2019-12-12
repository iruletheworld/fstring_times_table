# -*- coding: utf-8 -*-

'''
Using Python 3 f-string to make a times table string. A bit of fun.

This module uses the "pytablewriter" to convert the time table into a
markdown table string.

It also uses "pyperclip" to copy the markdown table string into the clipboard.

Author : 高斯羽 博士 (Dr. Gāo, Sī Yǔ)
'''

import pytablewriter
import pyperclip

__author__ = u'高斯羽 博士 (Dr. Gāo, Sī Yǔ)'
__version__ = '1.0.0'
__date__ = '2019-12-12'


def times_table(int_start=1, int_end=9):
    '''
    Using Python 3.6+ f-string to make a times table.

    Parameters
    -----------
    int_start : int
        The start of the times table.

        Default = 1.

    int_end : int
        The end of the times table.

        Default = 9.

    Returns
    --------
    zip : zip object
        The times table as a zip object.
    '''

    int_end = int_end + 1

    list_tbl = [
        [f'{x} × {y} = {x * y}' for y in range(int_start, int_end)]
        for x in range(int_start, int_end)
    ]

    return zip(*list_tbl)


# on windows, you must place the pytablewriter code inside this
if __name__ == '__main__':

    int_start = 1

    int_end = 9

    # make a times table from 1 to 9
    list_tbl = list(times_table(int_start, int_end))

    list_header = list(range(int_start, int_end + 1))

    # use pytablewriter to make a markdown table
    writer = pytablewriter.MarkdownTableWriter()

    writer.headers = list_header

    writer.value_matrix = list_tbl

    # copy table string to clipboard
    pyperclip.copy(writer.dumps())

    writer.write_table()
