# Using Python 3.6+ f-string to make a times table

Python f-string is pretty powerful and playful. This project shows how
to use f-string to make a times table and then convert it into a
Markdown string (but you could actually convert into all kinds of
different table string for different purposes, e.g., Latex, RST, CSV,
etc.).

The code to make the actual times table is very simple. You would get a
zip object from it.

```python
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
```

With the zip object, you can then use `pytablewriter` to convert it into
a Markdown string. Note that, on Windows, the code with `pytablewriter`
needs to be guarded, i.e., you need to put them into the `if __name__ ==
'__main__'` block.

```python
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

```

Then, you would get the following times table.

## Times table from 1 to 9
|    1    |    2     |    3     |    4     |    5     |    6     |    7     |    8     |    9     |
|---------|----------|----------|----------|----------|----------|----------|----------|----------|
|1 × 1 = 1|2 × 1 = 2 |3 × 1 = 3 |4 × 1 = 4 |5 × 1 = 5 |6 × 1 = 6 |7 × 1 = 7 |8 × 1 = 8 |9 × 1 = 9 |
|1 × 2 = 2|2 × 2 = 4 |3 × 2 = 6 |4 × 2 = 8 |5 × 2 = 10|6 × 2 = 12|7 × 2 = 14|8 × 2 = 16|9 × 2 = 18|
|1 × 3 = 3|2 × 3 = 6 |3 × 3 = 9 |4 × 3 = 12|5 × 3 = 15|6 × 3 = 18|7 × 3 = 21|8 × 3 = 24|9 × 3 = 27|
|1 × 4 = 4|2 × 4 = 8 |3 × 4 = 12|4 × 4 = 16|5 × 4 = 20|6 × 4 = 24|7 × 4 = 28|8 × 4 = 32|9 × 4 = 36|
|1 × 5 = 5|2 × 5 = 10|3 × 5 = 15|4 × 5 = 20|5 × 5 = 25|6 × 5 = 30|7 × 5 = 35|8 × 5 = 40|9 × 5 = 45|
|1 × 6 = 6|2 × 6 = 12|3 × 6 = 18|4 × 6 = 24|5 × 6 = 30|6 × 6 = 36|7 × 6 = 42|8 × 6 = 48|9 × 6 = 54|
|1 × 7 = 7|2 × 7 = 14|3 × 7 = 21|4 × 7 = 28|5 × 7 = 35|6 × 7 = 42|7 × 7 = 49|8 × 7 = 56|9 × 7 = 63|
|1 × 8 = 8|2 × 8 = 16|3 × 8 = 24|4 × 8 = 32|5 × 8 = 40|6 × 8 = 48|7 × 8 = 56|8 × 8 = 64|9 × 8 = 72|
|1 × 9 = 9|2 × 9 = 18|3 × 9 = 27|4 × 9 = 36|5 × 9 = 45|6 × 9 = 54|7 × 9 = 63|8 × 9 = 72|9 × 9 = 81|

The string you get is the following.
```markdown
|    1    |    2     |    3     |    4     |    5     |    6     |    7     |    8     |    9     |
|---------|----------|----------|----------|----------|----------|----------|----------|----------|
|1 × 1 = 1|2 × 1 = 2 |3 × 1 = 3 |4 × 1 = 4 |5 × 1 = 5 |6 × 1 = 6 |7 × 1 = 7 |8 × 1 = 8 |9 × 1 = 9 |
|1 × 2 = 2|2 × 2 = 4 |3 × 2 = 6 |4 × 2 = 8 |5 × 2 = 10|6 × 2 = 12|7 × 2 = 14|8 × 2 = 16|9 × 2 = 18|
|1 × 3 = 3|2 × 3 = 6 |3 × 3 = 9 |4 × 3 = 12|5 × 3 = 15|6 × 3 = 18|7 × 3 = 21|8 × 3 = 24|9 × 3 = 27|
|1 × 4 = 4|2 × 4 = 8 |3 × 4 = 12|4 × 4 = 16|5 × 4 = 20|6 × 4 = 24|7 × 4 = 28|8 × 4 = 32|9 × 4 = 36|
|1 × 5 = 5|2 × 5 = 10|3 × 5 = 15|4 × 5 = 20|5 × 5 = 25|6 × 5 = 30|7 × 5 = 35|8 × 5 = 40|9 × 5 = 45|
|1 × 6 = 6|2 × 6 = 12|3 × 6 = 18|4 × 6 = 24|5 × 6 = 30|6 × 6 = 36|7 × 6 = 42|8 × 6 = 48|9 × 6 = 54|
|1 × 7 = 7|2 × 7 = 14|3 × 7 = 21|4 × 7 = 28|5 × 7 = 35|6 × 7 = 42|7 × 7 = 49|8 × 7 = 56|9 × 7 = 63|
|1 × 8 = 8|2 × 8 = 16|3 × 8 = 24|4 × 8 = 32|5 × 8 = 40|6 × 8 = 48|7 × 8 = 56|8 × 8 = 64|9 × 8 = 72|
|1 × 9 = 9|2 × 9 = 18|3 × 9 = 27|4 × 9 = 36|5 × 9 = 45|6 × 9 = 54|7 × 9 = 63|8 × 9 = 72|9 × 9 = 81|

```

You can easily get the string in other formats. All you need to do is
change the writer from Markdown to the desired one. See the [documentation](https://pytablewriter.readthedocs.io/en/latest/index.html)
of `pytablewriter` for more details.

Here is an example for reStructuredText.

```python
writer = pytablewriter.RstGridTableWriter()
```


```rst
.. table::

    +---------+----------+----------+----------+----------+----------+----------+----------+----------+
    |    1    |    2     |    3     |    4     |    5     |    6     |    7     |    8     |    9     |
    +=========+==========+==========+==========+==========+==========+==========+==========+==========+
    |1 × 1 = 1|2 × 1 = 2 |3 × 1 = 3 |4 × 1 = 4 |5 × 1 = 5 |6 × 1 = 6 |7 × 1 = 7 |8 × 1 = 8 |9 × 1 = 9 |
    +---------+----------+----------+----------+----------+----------+----------+----------+----------+
    |1 × 2 = 2|2 × 2 = 4 |3 × 2 = 6 |4 × 2 = 8 |5 × 2 = 10|6 × 2 = 12|7 × 2 = 14|8 × 2 = 16|9 × 2 = 18|
    +---------+----------+----------+----------+----------+----------+----------+----------+----------+
    |1 × 3 = 3|2 × 3 = 6 |3 × 3 = 9 |4 × 3 = 12|5 × 3 = 15|6 × 3 = 18|7 × 3 = 21|8 × 3 = 24|9 × 3 = 27|
    +---------+----------+----------+----------+----------+----------+----------+----------+----------+
    |1 × 4 = 4|2 × 4 = 8 |3 × 4 = 12|4 × 4 = 16|5 × 4 = 20|6 × 4 = 24|7 × 4 = 28|8 × 4 = 32|9 × 4 = 36|
    +---------+----------+----------+----------+----------+----------+----------+----------+----------+
    |1 × 5 = 5|2 × 5 = 10|3 × 5 = 15|4 × 5 = 20|5 × 5 = 25|6 × 5 = 30|7 × 5 = 35|8 × 5 = 40|9 × 5 = 45|
    +---------+----------+----------+----------+----------+----------+----------+----------+----------+
    |1 × 6 = 6|2 × 6 = 12|3 × 6 = 18|4 × 6 = 24|5 × 6 = 30|6 × 6 = 36|7 × 6 = 42|8 × 6 = 48|9 × 6 = 54|
    +---------+----------+----------+----------+----------+----------+----------+----------+----------+
    |1 × 7 = 7|2 × 7 = 14|3 × 7 = 21|4 × 7 = 28|5 × 7 = 35|6 × 7 = 42|7 × 7 = 49|8 × 7 = 56|9 × 7 = 63|
    +---------+----------+----------+----------+----------+----------+----------+----------+----------+
    |1 × 8 = 8|2 × 8 = 16|3 × 8 = 24|4 × 8 = 32|5 × 8 = 40|6 × 8 = 48|7 × 8 = 56|8 × 8 = 64|9 × 8 = 72|
    +---------+----------+----------+----------+----------+----------+----------+----------+----------+
    |1 × 9 = 9|2 × 9 = 18|3 × 9 = 27|4 × 9 = 36|5 × 9 = 45|6 × 9 = 54|7 × 9 = 63|8 × 9 = 72|9 × 9 = 81|
    +---------+----------+----------+----------+----------+----------+----------+----------+----------+
```

# Contributing

高斯羽 博士 (Dr. Gāo, Sī Yǔ)

# Licence

MIT