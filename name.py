import requests
from randommer import Randommer
from pprint import pprint


class Name(Randommer):
    def get_name(self, api_key: str, nameType: str, quantity: int) -> list:
        '''get name

        Args:
            api_key (str): api key
            nameType (str): nameType
            quantity (str): number of names

        Returns:
            list: list of names
        '''
        endpoint = 'Name'
        url = self.get_url() + endpoint
        header = {
            'X-Api-Key':api_key
        }
        payload = {
            'nameType':nameType,
            'quantity':quantity
        }
        res = requests.get(url=url,headers=header,params=payload)
        if res.status_code == 200:
            return res.json()
        else:
            return False
    
    def get_name_suggestions(self, api_key: str, startingWords: str) -> list:
        '''get name suggestions

        Args:
            api_key (str): api key
            startingWords (str): startingWords

        Returns:
            list: list of name suggestions
        '''
        endpoint = 'Name/Suggestions'
        url = self.get_url() + endpoint
        header = {
            'X-Api-Key':api_key
        }
        payload = {
            'startingWords':startingWords
        }
        res = requests.get(url=url,headers=header,params=payload)
        if res.status_code == 200:
            return res.json()
        else:
            return False
    
    def get_name_cultures(self, api_key: str) -> list:
        '''get available cultures

        Args:
            api_key (str): api key

        Returns:
            list: list of names
        '''
        endpoint = 'Name/Cultures'
        url = self.get_url() + endpoint
        header = {
             'X-Api-Key':api_key
        }
        res = requests.get(url=url,headers=header)
        if res.status_code == 200:
            return res.json()
        else:
            return None

nm = Name()

pprint(nm.get_name_cultures('8a2128f0e8254c4c8bbe8561b12f88c0'))