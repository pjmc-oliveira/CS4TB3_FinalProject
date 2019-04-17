'''
Some example usages for new language features
'''

# def running_avg():
#     'Ask user for input and keep running avg'
#     count = 0
#     summ = 0
#     print('Enter numbers to avg, press \'q\' to exit.')
#     do:
#         c = input('Enter a number: ')
#     while c != 'q':
#         try:
#             summ += int(c)
#             count++
#         except ValueError:
#             print('Invalid input!')
#             break
#     else:
#         print(f'The avg is {summ/count}')

class DescriptiveInt(int):
    'An int that can describe itself'
    '''
    Usage:
        str(DescriptiveInt(57)) -> 'A number'
        str(DescriptiveInt(44)) -> 'An even number'
        ...
    '''
    def __str__(self):
        switch self:
            case < 0:
                return 'A negative number'
            case 0:
                return 'zero'
            case 1:
                return 'one'
            case in range(0, self + 1, 2):
                return 'An even number'
            case < 10:
                return 'A small number'
            case >= 100:
                return 'A large number'
            else:
                return 'A number'

def drop(iterable, item):
    'Drop the beginning of an iterable until item'
    'Usage: drop(range(10), 5) -> range(5, 10)'
    i = 0
    until iterable[i] == item:
        i++
    return iterable[i:]

def fib(n: int) -> int:
    'Gets the n\'th fibonacci number'
    'Usage: [fib(i) for i in range(10)] -> [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]'
    unless n < 2:
        return fib(n - 1) + fib(n - 2)
    else:
        return n



class NilType(type):
    def __eq__(self, other):
        'Return true if can\'t access 0th element'
        try:
            other[0]
            return False
        except IndexError:
            return True

class ConsType(type):
    def __eq__(self, other):
        'Return true if can access 0th element'
        try:
            other[0]
            return True
        except IndexError:
            return False

class Nil(metaclass=NilType): pass
class Cons(metaclass=ConsType): pass

'''Overload operators for pseudo pattern-matching'''
def length(xs):
    'Gets the length of a sequence recursively'
    'Usage: length(range(44, 77, 3) -> 11'
    switch xs:
        case Nil: return 0
        case Cons: return 1 + length(xs[1:])