import random
import itertools


NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

to_title = [name.title() for name in NAMES]
print(to_title)


def team_maker():
    names = [name.split()[0] for name in to_title]
    while True:
        first, second = random.sample(names, 2)
        if first == second:
            next(team_maker())
        yield f'{first} teams up with {second}'


def dedup_and_title_case_names(names):
    names = set([name.title() for name in names])
    return names


def change_order(name):
    first, second = name.split()
    return f"{second} {first}"


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    names = [change_order(name) for name in names]
    names.sort(reverse=True)
    return [change_order(name) for name in names]


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    names = [name.split()[0] for name in names]
    lengths = [len(name) for name in names]
    return names[lengths.index(min(lengths))]


bites = {6: 'PyBites Die Hard',
         7: 'Parsing dates from logs',
         9: 'Palindromes',
         10: 'Practice exceptions',
         11: 'Enrich a class with dunder methods',
         12: 'Write a user validation function',
         13: 'Convert dict in namedtuple/json',
         14: 'Generate a table of n sequences',
         15: 'Enumerate 2 sequences',
         16: 'Special PyBites date generator',
         17: 'Form teams from a group of friends',
         18: 'Find the most common word',
         19: 'Write a simple property',
         20: 'Write a context manager',
         21: 'Query a nested data structure'}
exclude_bites = {6, 10, 16, 18, 21}


def filter_bites(bites=bites, bites_done=exclude_bites):
    """return the bites dict with the exclude_bites filtered out"""
    return {k: v for k, v in bites.items() if k not in bites_done}


if __name__ == '__main__':
    pairs = team_maker()
    for _ in range(1000):
        print(next(pairs))
    slice_pairs = itertools.islice(pairs, 10)
    print(list(slice_pairs))
    print(dedup_and_title_case_names(NAMES))
    print(sort_by_surname_desc(NAMES))
    print(shortest_first_name(NAMES))
