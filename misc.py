import requests
from randommer import Randommer


class Misc(Randommer):
    def get_cultures(self, api_key: str) -> list:
        '''get available misc cultures

        Args:
            api_key (str): api key

        Returns:
            list: list of cultures
        '''
        endpoint = 'Misc/Cultures'
        url = self.get_url() + endpoint
        header = {
            'X-Api-Key':api_key
        }
        res = requests.get(url=url,headers=header)
        if res.status_code == 200:
            return res.json()
        else:
            return None
    
    def get_random_address(self, api_key: str, number: int, culture='en') -> list:
        '''get available misc cultures

        Args:
            api_key (str): api key
            number (str): number
            culture (str): culture

        Returns:
            list: random address
        '''
        endpoint = 'Misc/Random-Address'
        url = self.get_url() + endpoint
        headers = {
            'X-Api-Key':api_key
        }
        payload = {
            'number':number
        }
        res = requests.get(url=url,headers=headers,params=payload)
        if res.status_code == 200:
            return res.json()
        else:
            return False

ms = Misc()

print(ms.get_random_address('8a2128f0e8254c4c8bbe8561b12f88c0',2))