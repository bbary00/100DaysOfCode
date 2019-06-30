import time
from functools import wraps

def timeit(func):
    """
    Decorator to time a function
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        # before calling the decorated function
        print('== starting timer')
        start = time.time()

        # call the decorated function
        func(*args, **kwargs)

        # after calling the decorated function
        end = time.time()
        print(
            f'== {func.__name__} took {int(end - start)} seconds to complete')

    return wrapper


def print_args(func):
    '''Decorator to print function arguments'''

    @wraps(func)
    def wrapper(*args, **kwargs):

        # before
        print()
        print('*** args:')
        for arg in args:
            print(f'- {arg}')

        print('**** kwargs:')
        for k, v in kwargs.items():
            print(f'- {k}: {v}')
        print()

        # call func
        func(*args, **kwargs)

    return wrapper


@timeit
@print_args
def generate_report(*months, **parameters):
    time.sleep(2)
    print('(actual function) Done, report links ...')


parameters = dict(split_geos=True, include_suborgs=False, tax_rate=33)
generate_report('October', 'November', 'December', **parameters)


"""
Write a decorator called make_html that
 wraps text inside one or more html tags.

As shown in the tests decorating get_text with make_html twice should
 wrap the text in the corresponding html tags, so:

@make_html('p')
@make_html('strong')
def get_text(text='I code with PyBites'):
    return text
- would return: <p><strong>I code with PyBites</strong></p>

Have fun and start to grok decorators!
"""





def make_html(element):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = f'<{element}>' + func(*args, **kwargs) + f'</{element}>'
            return result
        return wrapper
    return decorator


@make_html('p')
@make_html('strong')
def get_text(text='I code with PyBites'):
    return text

print(get_text())
