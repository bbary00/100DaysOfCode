from collections import defaultdict, namedtuple, Counter, deque
import csv
import random
from urllib.request import urlretrieve
import timeit, functools

# user = ('bob', 'coder')
# print("{0} is a {1}".format(user[0], user[1]))
#
# User = namedtuple('User', 'name role')
# user = User(name='Amy', role='admin')
# print(f"{user.name} is a {user.role}")
#
# users = {'bob': 'coder'}
# print(users['bob'])
# # print(users['julien']) #ERROR
# print(users.get('bob'))
# print(users.get('julien')) #None
#
# challenges_done = [('mike', 10), ('julian', 7), ('bob', 5),
#                    ('mike', 11), ('julian', 8), ('bob', 6)]
# print(challenges_done)
# challenges = {}
# # for k, v in challenges_done:
# #     challenges[k].append          # Can't append
# challenges = defaultdict(list)
# for k, v in challenges_done:
#     challenges[k].append(v)
# print(challenges)
#
#
# words = "Lorem Ipsum is simply dummy text of the printing and " \
#         "typesetting industry. Lorem Ipsum has been\
#     the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and \
#     scrambled it to make a type specimen book. It has survived not only \
#     five centuries, but also the leap into \
#     electronic typesetting, remaining essentially unchanged. It was \
#     popularised in the 1960s with the release of \
#     Letraset sheets containing Lorem Ipsum passages, and more recently with\
#     desktop publishing software like Aldus \
#     PageMaker including versions of Lorem Ipsum".split()
# print(words[:5])
# common_words = {}
# for i in words:
#     if i not in common_words:
#         common_words[i] = 1
#     else:
#         common_words[i] += 1
#
# for k, v in sorted(common_words.items(),
#                    key=lambda x: x[1],
#                    reverse=True)[:5]:
#     print(k, v)
#
# common_words = Counter(words)
# print(common_words.most_common(5))
#
#
#
# lst = list(range(1000000))
# deq = deque(range(1000000))
# def insert_delete(ds):
#     for _ in range(10):
#         index = random.choice(range(100))
#         ds.remove(index)
#         ds.insert(index, index)
# t = timeit.Timer(functools.partial(insert_delete, lst))
# t2 = timeit.Timer(functools.partial(insert_delete, deq))
# # print(t.timeit(100))
# # print(t2.timeit(100))



print()
movie_data = 'https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv'
movies_csv = 'movies.csv'
print(urlretrieve(movie_data, movies_csv))
Movie = namedtuple('Movie', 'title year score')
def get_movies_by_director(data=movies_csv):
    """Extracts all movies from csv and stores them in a dictionary
       where keys are directors, and values is a list of movies (named tuples)"""
    directors = defaultdict(list)
    with open(data, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue

            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)

    return directors


directors = get_movies_by_director()
# print(type(directors))
# print(directors['Christopher Nolan'])
# cnt = Counter()
# for k, v in directors.items():
#     cnt[k] = len(v)
# print(cnt.most_common(5))

rates = defaultdict(list)
for k, v in directors.items():
    rates[k] = sorted(v, key=lambda x: x.score, reverse=True)[0]
rates = dict(sorted(rates.items(), key=lambda x: x[1][2], reverse=True))
for k, v in rates.items():
    print(k, v)










