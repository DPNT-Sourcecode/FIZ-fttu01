# noinspection PyUnusedLocal
def fizz_buzz(number):
    '''
    :param number: Integer
    :return: string

    >>> fizz_buzz (3) --> 'fizz'
    >>> fizz_buzz (5) --> 'buzz'
    >>> fizz_buzz (15) --> 'fizz buzz'
    >>> fizz_buzz (333) --> 'fizz deluxe'
    >>> fizz_buzz (555) --> 'fizz buzz deluxe'
    >>> fizz_buzz (5555) --> 'buzz deluxe'
    '''

    both = 'fizz buzz'
    one = 'fizz'
    butNotTheOther = 'buzz'
    poshFrocks = ' deluxe'
    msg = ''
    theFinalFrontier ' '

    ''' Test for divisible by 3 or contains 3 '''
    if (not (number % 3)) or ('3' in str(number)):
        msg = one

    ''' Test for divisible by 5 or contains 5 '''
    if (not (number % 5)) or ('5' in str(number)):
        if msg == '':
            msg = butNotTheOther
        else:
            msg = msg + theFinalFrontier + butNotTheOther

    ''' Test for bigger than ten and number made
    up of the same character repeated '''
    if number > 10 and singleNum(number):
        if len(msg) == 0:
            msg = poshFrocks
        else:
            msg = msg + theFinalFrontier + poshFrocks

    if len(msg) > 0:
        return msg
    else:
        return str(number)

    '''raise NotImplementedError()'''


def singleNum(number):
    '''
    :param number: Integer
    :return: boolean

    >>> singleNum(111) --> 1
    >>> singleNum(112) --> 0
    '''

    ''' Get the first charcter in the number '''
    num = str(number)[0]

    '''If all the digits in number are the same
    as the first character return TRUE (1)'''

    return len(str(number).strip(num)) == 0

    '''raise NotImplementedError()'''

