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
    msg =''

    if not (number % 3):
        msg = one
    elif '3' in str(number):
        msg = one

    if not (number % 5):
        msg = msg + butNotTheOther
    elif '5' in str(number):
        msg = msg + butNotTheOther

    if len(msg) > 4:
        return both
    elif len(msg) = 4:
        return msg
    else:
        return str(number)

    '''raise NotImplementedError()'''



