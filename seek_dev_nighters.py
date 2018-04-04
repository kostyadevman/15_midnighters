import requests
import pytz


def load_attempts():
    devman_response = requests.get(
        'https://devman.org/api/challenges/solution_attempts/?page=1',
        params = {'page': '1'}
    )
    page_count = devman_response.json()['number_of_pages']
    for page in range(1,page_count+1):
        devman_response = requests.get(
            'https://devman.org/api/challenges/solution_attempts/',
            params={'page': '{}'.format(page)}
        )
        for attempt in devman_response.json()['records']:
            yield attempt



def get_midnighters():
    pass


if __name__ == '__main__':
    attempts = load_attempts()
    for attempt in attempts:
        print(attempt)
