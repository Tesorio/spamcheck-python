import requests

API_URL = 'http://spamcheck.postmarkapp.com/filter'


def _parse_response(response):
    content = response.json()

    if response.status_code != 200 or not content.get('success'):
        error_msg = content.get('message', 'API Error')
        raise Exception(error_msg)

    return content


def check(email, report=False):
    options = '"long"' if report else '"short"'
    headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
    }

    data = '{"email":"'+ email + '", "options":' + options + '}'

    response = requests.post(API_URL, headers=headers, data=data)

    return _parse_response(response)

