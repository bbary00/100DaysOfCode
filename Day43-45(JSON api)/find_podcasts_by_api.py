from api_worker import find_info_by_keywords
import webbrowser
import re


def print_info(podcast_object):
    print(f'Podcast title: {podcast_object.title}')
    print(f'Podcast category: {podcast_object.category}')
    print(f'Podcast id: {podcast_object.id}')
    print(f'Podcast description: {podcast_object.description}')
    webbrowser.open('https://talkpython.fm' + podcast_object.url, new=2)


def get_keywords():
    input_string = input('Enter keywords to search: ')
    keywords = re.split(r'[\s,]\s*', input_string)
    response_line, podcasts = find_info_by_keywords(keywords)
    if not podcasts:
        print(response_line)
        return 0
    else:
        print(response_line)
        for i, podcast in enumerate(podcasts, start=1):
            print(f'{i}. ', podcast.title)
        print('\n\n')
        see_info_number = int(input('See info about podcast with number: ')) - 1
        print_info(podcasts[see_info_number])


get_keywords()
