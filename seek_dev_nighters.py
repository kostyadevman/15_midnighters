import requests
import pytz
from datetime import datetime


def load_attempts():
    devman_url = 'https://devman.org/api/challenges/solution_attempts/'
    page = 1
    while True:
        devman_json = requests.get(
            devman_url,
            params={'page': page}
        ).json()
        for attempt in devman_json['records']:
            yield attempt
        page += 1
        if page > devman_json['number_of_pages']:
            break


def get_midnighters(attempts):
    midnighters = []
    for attempt in attempts:
        attempt_date = datetime.fromtimestamp(
            attempt['timestamp'],
            pytz.timezone(attempt['timezone'])
        )
        midnite_hour = 0
        morning_hour = 6
        if midnite_hour <= attempt_date.hour < morning_hour:
            if attempt['username'] not in midnighters:
                midnighters.append(attempt['username'])
    return midnighters


if __name__ == '__main__':
    attempts = load_attempts()
    midnighters = get_midnighters(attempts)
    print('\n'.join(midnighters))
