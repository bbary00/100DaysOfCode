import requests
from collections import namedtuple
from typing import List

MAIN_URL = 'https://search.talkpython.fm/api/search?q='
Podcast = namedtuple('Podcast', 'category, id, url, title, description')


def ends_for__plural_words(word_to_return, _list):
    special_letters = ['a', 'o', 'u', 'i', 'e']
    plural_ends = dict.fromkeys(special_letters, 'es')
    special_letters.append('y')
    plural_ends['y'] = 'ies'
    if len(_list) > 1:
        if word_to_return[-1] in special_letters:
            word_to_return += plural_ends[word_to_return[-1]]
        else:
            word_to_return += 's'
        return word_to_return
    return word_to_return


def find_info_by_keywords(*args) -> (str, List[Podcast]):
    request_string = MAIN_URL + '-'.join(*args)
    response = requests.get(request_string).json()
    if not response['results']:
        serching_info = f'There is no result by "' + ', '.join(*args) + ends_for__plural_words('" keyword', *args)
        return serching_info, None
    else:
        serching_info = 'Found {0} results for {1:.2f} ms. by "{2}'\
                            .format(len(response['results']),
                                    response['elapsed_ms'],
                                    ', '.join(*args)) + ends_for__plural_words('" keyword', *args)
        podcasts = [Podcast(*podcast.values()) for podcast in response['results']]
        return serching_info, podcasts