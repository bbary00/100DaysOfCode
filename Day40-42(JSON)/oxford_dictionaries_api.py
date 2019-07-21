import requests
import json


def read_creds():

    with open('credentials.txt', 'r') as file:
        credentials = file.read()
    return json.loads(credentials)


credential = read_creds()
language = 'en'
word = 'Ace'

url = f'https://od-api.oxforddictionaries.com:443/' \
    f'api/v2/entries/{language}/{word}'

r = requests.get(url,
                 headers={'app_id': credential['app_id'],
                          'app_key': credential['app_key']})

response = json.loads(r.text)
for result in response['results']:
    for lexicalEntrie in result['lexicalEntries']:
        for entrie in lexicalEntrie['entries']:
            for sense in entrie['senses']:
                print(f"Definition: {' '.join(sense['definitions'])}")
