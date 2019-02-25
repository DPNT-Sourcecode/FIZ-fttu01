# noinspection PyUnusedLocal
def fizz_buzz(number):

    '''

    :param number: Integer
    :param Int2: Integer between 0 and 100 inclusive
    :return: string

    >>> fizz_buzz (3) --> 'fizz'
    >>> fizz_buzz (5) --> 'buzz'
    >>> fizz_buzz (15) --> 'fizz buzz'
    '''

    both = 'fizz buzz'
    one = 'fizz'
    butNotTheOther = 'buzz'

    if (number % 3 =0) and (number % 5 =0):
        return both
    elif number % 3 =0:
        return one
    elif number % 3 =0:
        return butNotTheOther
    else:
        return str(number)

    '''raise NotImplementedError()'''





