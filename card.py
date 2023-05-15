import requests
from randommer import Randommer


class Card(Randommer):
    def get_card(self, api_key: str, type=None) -> dict:
        '''get card from randommer
        
        Args:
            api_key (str): api key
            type (str): card type

        Returns:
            dict: card data
        '''
        endpoint = 'Card'
        url = self.get_url() + endpoint

        payload = {
            'type': type,
        }
        headers = {
            'X-Api-Key': api_key,
        }

        response = requests.get(url, params=payload, headers=headers)

        if response.status_code == 200:
            return response.json()
        
        return None

    def get_card_types(self, api_key: str) -> list:
        '''get cars types from randommer

        Args:
            api_key (str): api key
            
        Returns:
            list: list of types
        '''
        endpoint = 'Card/Types'
        url = self.get_url() + endpoint
        headers = {
            'X-Api-Key': api_key,
        }
        res = requests.get(url=url,headers=headers)
        if res.status_code == 200:
            return res.json()
        else:
            return None

        

card = Card()

print(card.get_card_types('2d794c6f46094ceb96bd719c1c26c984'))