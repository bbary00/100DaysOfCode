from itertools import zip_longest
from itertools import permutations, combinations


"""
What?! Mike, Kim, and Andre are missing!
You heard somebody mention itertools the other day for its
power to work with iterators. Maybe it has a convenient way
to solve this problem? Check out the module and patch the
get_attendees function for Bert so it returns all names
again. For missing data use dashes (-).
"""

names = 'Tim Bob Julian Carmen Sofia Mike Kim Andre'.split()
locations = 'DE ES AUS NL BR US'.split()
confirmed = [False, True, True, False, True]


def get_attendees():
    for participant in zip_longest(names, locations, confirmed, fillvalue='-'):
        print(participant)


def friends_teams(friends, size=2, order_does_matter=False):
    if order_does_matter:
        print(list(permutations(friends, size)))
    else:
        print(list(combinations(friends, size)))


if __name__ == '__main__':
    get_attendees()
    friends_teams(names, 3)
