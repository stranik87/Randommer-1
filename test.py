import requests

base_url = 'https://randommer.io/'

def get_card():
    '''get card'''
    endpoint = 'api/Card'
    
    url = base_url + endpoint # 'https://randommer.io/api/Card'

    payload = {
        'type': 'Visa',
    }
    headers = {
        'X-Api-Key': '2d794c6f46094ceb96bd719c1c26c984',
    }

    response = requests.get(url, params=payload, headers=headers)

    if response.status_code == 200:
        return response.json()


print(get_card())
