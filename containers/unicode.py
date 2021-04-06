import unicodedata


class NormalizedStr:
    '''
<<<<<<< HEAD
    By default Python's str type stores any valid unicode string.
=======
    By default, Python's str type stores any valid unicode string.
>>>>>>> b2d46c4950c56835211bb5d5d606c2feb8883262
    This can result in unintuitive behavior.
    For example:

    >>> 'César' in 'César Chávez'
    True
    >>> 'César' in 'César Chávez'
    False

<<<<<<< HEAD
<<<<<<< HEAD
    The two strings to the right of the in keyword above are
    equal *semantically*,
    but they are not equal *representationally*.
    In particular, the first is in NFC form, and the second is
    in NFD form.
    The purpose of this class is to automatically normalize our
    strings for us,
=======
=======
>>>>>>> b2d46c4950c56835211bb5d5d606c2feb8883262
    The two strings to the right of the in keyword above are equal *semantically*,
    but not equal *representationally*.
    In particular, the first is in NFC form, and the second is in NFD form.
    The purpose of this class is to automatically normalize our strings for us,
<<<<<<< HEAD
>>>>>>> b2d46c4950c56835211bb5d5d606c2feb8883262
=======
>>>>>>> b2d46c4950c56835211bb5d5d606c2feb8883262
    making foreign languages "just work" a little bit easier.
    '''

    def __init__(self, text, normal_form='NFC'):
<<<<<<< HEAD
<<<<<<< HEAD
        self.text = unicodedata.normalize(normal_form, text)
        self.form = normal_form

    def __repr__(self):
        '''
        The string returned by the __repr__ function should be
        valid python code
        that can be substituted directly into the python
        interpreter to reproduce an equivalent object.
        '''
        return "NormalizedStr('" + str(self.text) + "', '" + str(self.form) + "')"

    def __str__(self):
        '''
        This functions converts the NormalizedStr into a
        regular string object.
        The output is similar, but not exactly the same,
        as the __repr__ function.
        '''
        return str(self.text)
=======
=======
>>>>>>> b2d46c4950c56835211bb5d5d606c2feb8883262
        pass

    def __repr__(self):
        '''
        The string returned by the __repr__ function should be valid python code
        that can be substituted directly into the python interpreter to reproduce an equivalent object.
        '''

    def __str__(self):
        '''
        This functions converts the NormalizedStr into a regular string object.
        The output is similar, but not exactly the same, as the __repr__ function.
        '''
<<<<<<< HEAD
>>>>>>> b2d46c4950c56835211bb5d5d606c2feb8883262
=======
>>>>>>> b2d46c4950c56835211bb5d5d606c2feb8883262

    def __len__(self):
        '''
        Returns the length of the string.
        The expression `len(a)` desugars to a.__len__().
        '''
<<<<<<< HEAD
<<<<<<< HEAD
        return len(self.text)

    def __contains__(self, substr):
        '''
        Returns true if the `substr` variable is contained
        within `self`.
        The expression `a in b` desugars to `b.__contains__(a)`.

        HINT:
        You should normalize the `substr` variable to ensure that
        the comparison is done semantically and not syntactically.
        '''
        return unicodedata.normalize(self.form, substr) in self.text
=======
=======
>>>>>>> b2d46c4950c56835211bb5d5d606c2feb8883262

    def __contains__(self, substr):
        '''
        Returns true if the `substr` variable is contained within `self`.
        The expression `a in b` desugars to `b.__contains__(a)`.

        HINT:
        You should normalize the `substr` variable to ensure that the comparison is done semantically and not syntactically.
        '''
<<<<<<< HEAD
>>>>>>> b2d46c4950c56835211bb5d5d606c2feb8883262
=======
>>>>>>> b2d46c4950c56835211bb5d5d606c2feb8883262

    def __getitem__(self, index):
        '''
        Returns the character at position `index`.
        The expression `a[b]` desugars to `a.__getitem__(b)`.
        '''
<<<<<<< HEAD
<<<<<<< HEAD
        return self.text[index]
=======
>>>>>>> b2d46c4950c56835211bb5d5d606c2feb8883262
=======
>>>>>>> b2d46c4950c56835211bb5d5d606c2feb8883262

    def lower(self):
        '''
        Returns a copy in the same normalized form, but lower case.
        '''
<<<<<<< HEAD
<<<<<<< HEAD
        return self.text.lower()
=======
>>>>>>> b2d46c4950c56835211bb5d5d606c2feb8883262
=======
>>>>>>> b2d46c4950c56835211bb5d5d606c2feb8883262

    def upper(self):
        '''
        Returns a copy in the same normalized form, but upper case.
        '''
<<<<<<< HEAD
<<<<<<< HEAD
        return self.text.upper()
=======
>>>>>>> b2d46c4950c56835211bb5d5d606c2feb8883262
=======
>>>>>>> b2d46c4950c56835211bb5d5d606c2feb8883262

    def __add__(self, b):
        '''
        Returns a copy of `self` with `b` appended to the end.
        The expression `a + b` gets desugared into `a.__add__(b)`.

        HINT:
<<<<<<< HEAD
<<<<<<< HEAD
        The addition of two normalized strings is not guaranteed
        to stay normalized.
        Therefore, you must renormalize the strings after
        adding them together.
        '''
        return NormalizedStr(unicodedata.normalize(self.form,
                                                   str(self.text) + str(b)))
=======
        The addition of two normalized strings is not guaranteed to stay normalized.
        Therefore, you must renormalize the strings after adding them together.
        '''
>>>>>>> b2d46c4950c56835211bb5d5d606c2feb8883262
=======
        The addition of two normalized strings is not guaranteed to stay normalized.
        Therefore, you must renormalize the strings after adding them together.
        '''
>>>>>>> b2d46c4950c56835211bb5d5d606c2feb8883262

    def __iter__(self):
        '''
        HINT:
<<<<<<< HEAD
<<<<<<< HEAD
        Recall that the __iter__ method returns a class, which is
        the iterator object.
        You'll need to define your own iterator class with
        the appropriate magic methods,
        and return an instance of that class here.
        '''
        return NormalizedStrIter(self.text)


class NormalizedStrIter:
    def __init__(self, text):
        self.text = text
        self.i = 0

    def __next__(self):
        if len(self.text) <= self.i:
            raise StopIteration
        else:
            x = self.text[self.i]
            self.i += 1
            return x
=======
=======
>>>>>>> b2d46c4950c56835211bb5d5d606c2feb8883262
        Recall that the __iter__ method returns a class, which is the iterator object.
        You'll need to define your own iterator class with the appropriate magic methods,
        and return an instance of that class here.
        '''
<<<<<<< HEAD
>>>>>>> b2d46c4950c56835211bb5d5d606c2feb8883262
=======
>>>>>>> b2d46c4950c56835211bb5d5d606c2feb8883262
