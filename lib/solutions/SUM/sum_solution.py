# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    '''

     :param Int1: Integer between 0 and 100 inclusive
     :param Int2: Integer between 0 and 100 inclusive
     :return: Sum of Int1 and Int2

     >>> sumR1 (3, 57) --> 60
     >>> sumR1 (0, 100) --> 60
     '''

    if x in range(0,101) and y in range(0, 101):
        return x + y
    else:
        print 'Input out of range'


    '''raise NotImplementedError() '''