import re


"""
text = 'Awesome, I am doing the #100DaysOfCode challenge'

re.search(r'I am', text)
<_sre.SRE_Match at 0x7f18b0b0c100>

re.match(r'I am', text)
nothing because from start to end

re.match(r'Awesome.*challenge', text)
<_sre.SRE_Match at 0x7f18b0b0c098>

hundred = 'Awesome, I am doing the #100DaysOfCode challenge'
two_hundred = 'Awesome, I am doing the #200DaysOfCode challenge'

m = re.match(r'.*(#\d+DaysOfCode).*', hundred)
m.groups()[0]
"""

# Trainings

text = """It weighed about 10,000 tons, entered the atmosphere at a
    speed of 64,000km/h and exploded over a city with a blast of 500
    kilotons. But on 15 February 2013, we were-lucky. The meteorite
    that showered pieces of rock over Chelyabinsk, Russia, was relatively
    small, at only about 17 metres wide. Although 458 many people
    were injured by falling glass, the damage was nothing compared
    to what had happened in Siberia nearly one hundred years ago.
    Another relatively small object (approximately 50 metres in diameter)
    exploded in mid-air over a forest region, flattening about 80 
    million trees. If 256 it had exploded over a city such as Moscow
    or London, millions of people would have been killed.
    
    By a strange coincidence, the same day that the meteorite 
    terrified the people of Chelyabinsk, another 50m-wide asteroid passed 
    relatively close to Earth. Scientists were expecting that visit and know
    that the asteroid will return to fly close by us in 2046, but
    the Russian meteorite earlier in the day had been too
    small for anyone to spot."""

print(re.findall(r"\w+\s\d{4}.\s\w+", text))  # Year with word before and after
print(re.sub(r'\w+ed\s', '', text))  # Remove all words with -ed
print(re.findall(r"[A-Z]\w+", text))  # All uppercase words
print(re.findall(r"\w+-\w+", text))  # Words with a slash


import re


def extract_course_times():
    """Write a regular expression that returns a list of timestamps:
        ['01:47', '32:03', '41:51', '27:48', '05:02']"""
    flask_course = ('Introduction 1 Lecture 01:47'
                    'The Basics 4 Lectures 32:03'
                    'Getting Technical!  4 Lectures 41:51'
                    'Challenge 2 Lectures 27:48'
                    'Afterword 1 Lecture 05:02')
    print(re.findall(r"\d{2}:\d{2}", flask_course))


def get_all_hashtags_and_links():
    """Write a regular expression that returns this list:
       ['http://pybit.es/requests-cache.html', '#python', '#APIs']"""
    tweet = ('New PyBites article: Module of the Week - Requests-cache '
             'for Repeated API Calls - http://pybit.es/requests-cache.html '
             '#python #APIs')
    print(re.findall(r"(http\S+|#\w+)", tweet))


extract_course_times()
get_all_hashtags_and_links()
