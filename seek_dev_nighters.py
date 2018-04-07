import requests
import pytz
from datetime import datetime


def load_attempts():
    devman_url = 'https://devman.org/api/challenges/solution_attempts/'
    devman_response = requests.get(
        devman_url,
        params = {'page': '1'}
    )
    page_count = devman_response.json()['number_of_pages']
    for page in range(1,page_count+1):
        devman_response = requests.get(
            devman_url,
            params={'page': '{}'.format(page)}
        )
        for attempt in devman_response.json()['records']:
            yield attempt


def get_midnighters(attempts):
    midnighters = []
    for attempt in attempts:
        attempt_date = datetime.fromtimestamp(attempt['timestamp'])
        timezone = pytz.timezone(attempt['timezone'])
        midnighter = attempt['username']

        attempt_date_local = timezone.localize(attempt_date)
        midnite_hour = 0
        morning_hour = 6
        if midnite_hour <= attempt_date_local.hour < morning_hour:
            if midnighter not in midnighters:
                midnighters.append(midnighter)
    return midnighters


if __name__ == '__main__':
    attempts = load_attempts()
    midnighters = get_midnighters(attempts)
    print('\n'.join(midnighters))
