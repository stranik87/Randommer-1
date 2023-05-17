import requests
from randommer import Randommer


class Phone(Randommer):
    def generate(self, api_key: str, CountryCode: str, Quantity: int) -> list:
        '''get bulk telephone numbers for a country

        Args:
            api_key (str): api key
            CountryCode (str): CountryCode ex: 'uz'
            Quantity (str): Quantity

        Returns:
            list: list of phone numbers
        '''
        endpoint = 'Phone/Generate'
        url = self.get_url() + endpoint
        header = {
            'X-Api-Key':api_key
        }
        payload = {
            'CountryCode':CountryCode,
            'Quantity':Quantity
        }
        res = requests.get(url=url,headers=header,params=payload)
        if res.status_code == 200:
            return res.json()
        else:
            return None
    
    def get_IMEI(self, api_key: str, Quantity: int) -> list:
        '''get bulk imei

        Args:
            api_key (str): api key
            Quantity (str): Quantity

        Returns:
            list: list of phone numbers
        '''
        endpoint = 'Phone/IMEI'
        url = self.get_url() + endpoint
        header = {
            'X-Api-Key':api_key
        }
        payload = {
            'Quantity':Quantity
        }
        res = requests.get(url=url,headers=header,params=payload)
        if res.status_code == 200:
            return res.json()
        else:
            return None
    
    def is_valid(self, api_key: str, telephone: str, CountryCode: str) -> bool:
        '''get bulk imei

        Args:
            api_key (str): api key
            telephone (str): phone number
            CountryCode (str): CountryCode ex: 'uz'

        Returns:
            bool: is valid
        '''
        endpoint = 'Phone/Validate'
        url = self.get_url() + endpoint
        header = {
            'X-Api-Key':api_key
        }
        payload = {
            'telephone':telephone,
            'CountryCode':CountryCode
        }
        res = requests.get(url=url,headers=header,params=payload)

        if res.status_code == 200:
            return True

        else:
            return False
    
    def get_countries(self, api_key: str) -> list:
        '''get countries

        Args:
            api_key (str): api key

        Returns:
            list: lsit of countries
        '''
        endpoint = 'Phone/Countries'
        url = self.get_url()+endpoint
        header = {
            'X-Api-Key':api_key
        }
        res = requests.get(url=url,headers=header)
        if res.status_code == 200:
            return res.json()
        else:
            return None

numb = Phone()
print(numb.get_countries('8a2128f0e8254c4c8bbe8561b12f88c0'))