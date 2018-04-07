import requests
import pytz
from datetime import datetime


def load_attempts():
    devman_url = 'https://devman.org/api/challenges/solution_attempts/'
    page = 1
    while True:
        devman_response = requests.get(
            devman_url,
            params={'page':'{}'.format(page)}
        ).json()
        for attempt in devman_response['records']:
            yield attempt
        page += 1
        if page > devman_response['number_of_pages']:
            break


def get_midnighters(attempts):
    midnighters = []
    for attempt in attempts:
        attempt_date = datetime.fromtimestamp(
            attempt['timestamp'],
            pytz.timezone(attempt['timezone'])
        )
        midnighter = attempt['username']

        midnite_hour = 0
        morning_hour = 6
        if midnite_hour <= attempt_date.hour < morning_hour:
            if midnighter not in midnighters:
                midnighters.append(midnighter)
    return midnighters


if __name__ == '__main__':
    attempts = load_attempts()
    midnighters = get_midnighters(attempts)
    print('\n'.join(midnighters))
