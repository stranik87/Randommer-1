import requests
from randommer import Randommer

class Finance(Randommer):
    def get_crypto_address_types(self, api_key: str) -> list:
        '''get available crypto types

        Args:
            api_key (str): api key

        Returns:
            list: list of types
        '''
        endpoint = 'Finance/CryptoAddress/Types'
        url = self.get_url() + endpoint
        headers = {
            'X-Api-Key': api_key
        }
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_crypto_address(self, crypto_type: str, api_key: str) -> dict:
        '''get available crypto address

        Args:
            crypto_type (str): crypto type
            api_key (str): api key

        Returns:
            dict: crypto address
        '''
        endpoint = 'Finance/CryptoAddress'
        url = self.get_url() + endpoint
        payload = {
            'cryptoType': crypto_type
        }
        headers = {
            'X-Api-Key': api_key
        }
        res = requests.get(url=url,params=payload,headers=headers)

        if res.status_code == 200:
            return res.json()
        else:
            return None

    def get_countries(self, api_key: str) -> list:
        '''get available countries

        Args:
            api_key (str): api key

        Returns:
            list: crypto address
        '''
        endpoint = 'Finance/Countries'
        url = self.get_url() + endpoint
        headers = {
            'X-Api-Key': api_key
                
        }
        res = requests.get(url=url,headers=headers)
        if res.status_code == 200:
            return res.json()
        else:
            return False

    def get_iban_by_country_code(self, country_code: str, api_key: str) -> dict:
        '''get available countries

        Args:
            country_code (str): country code
            api_key (str): api key

        Returns:
            dict: idan data
        '''
        endpoint = 'Finance/Iban/ad'
        url = self.get_url() + endpoint
        payload = {
            'countryCode':country_code
        }
        headers = {
            'X-Api-Key': api_key
                
        }
        res = requests.get(url=url,params=payload, headers=headers)
        if res.status_code == 200:
            return res.json()
        else:
            return False
       

fin = Finance()

print(fin.get_iban_by_country_code('AE','8a2128f0e8254c4c8bbe8561b12f88c0'))