import json
import requests

API_URL = 'https://spamcheck.postmarkapp.com/filter'


def _parse_response(response):
    try:
        content = response.json()
    except Exception:
        raise Exception('API Error. Spamcheck may be down.')

    if response.status_code != 200 or not content.get('success'):
        error_msg = content.get('message', 'API Error')
        raise Exception(error_msg)

    return content


def check(email, report=False):
    data = {
        'email': email,
        'options': 'long' if report else 'short'
    }
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    response = requests.post(API_URL, json.dumps(data), headers=headers)

    return _parse_response(response)
