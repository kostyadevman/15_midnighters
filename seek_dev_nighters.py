import requests
import pytz
from datetime import datetime

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



def get_midnighters(attempts):
    for attempt in attempts:
        attempt_date = datetime.fromtimestamp(attempt['timestamp'])
        timezone = pytz.timezone(attempt['timezone'])
        username = attempt['username']

        attempt_date_local = timezone.localize(attempt_date)
        midnite_hour = 0
        morning_hour = 6
        if midnite_hour <= attempt_date_local.hour < morning_hour:
            yield username

def print_midnighters(midnighters):
    pass

if __name__ == '__main__':
    attempts = load_attempts()
    midnighters = get_midnighters(attempts)
    print_midnighters(midnighters)

