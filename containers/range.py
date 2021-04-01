def range(a, b=None, c=None):
    '''
    This function should behave exactly like the built-in range function.
    For example:

    >>> list(range(5))
    [0, 1, 2, 3, 4]
    >>> list(range(1, 5))
    [1, 2, 3, 4]
    >>> list(range(1, 5, 2))
    [1, 3]

    HINT:
    If you can figure out how to use the built-in range function
    (without modifying the test cases!),
    then feel free to do so.
    That's fairly difficult to do, however, and it's much easier to
    just implement this function normally using the yield syntax.

    NOTE:
    For efficiency reasons, Python's built-in range object is written in
    the C programming language rather than natively in python.
    You can find the source code online at
    https://hg.python.org/cpython/file/ee7b713fec71/Objects/rangeobject.c
    The link takes you to a file that is 1445 lines long,
    and all it does is implement this simple functionality.
    My easy to read Python implementation of this function is just
    15 lines long.
    (And with some code golf I also wrote a less readable version
    that is only 4 lines.)
    It is very common for C programs to be 100x longer than their
    corresponding python programs.
    C code must manage lots of details about the computer manually that
    python code automates for you.
    Carefully written C code can be faster than the corresponding python
    code because it can remove some of the overhead of this automation process,
    but the resulting code is much longer and harder to read/write.
    '''

    if b and c:
        if c > b and b > 0:
            yield 0
        elif b / c < 0:
            return []
        elif b < 0 and c < 0:
            z1 = 0
            while z1 > b:
                yield z1
                z1 += c
        else:
            z1 = 0
            while z1 < b:
                yield z1
                z1 += c

    elif c is None and b:
        if a >= b:
            return []
        else:
            y1 = a
            while y1 < b:
                yield y1
                y1 += 1

    elif b is None and c is None:
        if a <= 0:
            return []
        else:
            x1 = 0
            while x1 < a:
                yield x1
                x1 += 1
