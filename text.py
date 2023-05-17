import requests
from randommer import Randommer


class Text(Randommer):
    def generate_LoremIpsum(self, api_key: str, loremType: str, type: str, number: int) -> str:
        '''Generate lorem ipsum

        Args:
            api_key (str): api key
            loremType (str): loremType (normal or bussines)
            type (str): type (words or paragraphs)
            number (int): number

        Returns:
            str: Lorem text
        '''
        endpoint = 'Text/LoremIpsum'
        url = self.get_url()+endpoint
        header = {
                'X-Api-Key':api_key
        }
        payload = {
            'loremType':loremType,
            'type':type,
            'number':number
        }
        res = requests.get(url=url,headers=header,params=payload)
        if res.status_code == 200:
            return res.json()
        else:
            return None

    def generate_password(self, api_key: str, length: int, hasDigits: bool, hasUppercase: bool, hasSpecial: bool) -> str:
        '''Generate lorem ipsum

        Args:
            api_key (str): api key
            length (int): lenth of password
            hasDigits (bool): hasDigits
            hasUppercase (bool): hasUppercase
            hasSpecial (bool): hasSpecial

        Returns:
            str: pasword
        '''
        endpoint = 'Text/Password'
        url = self.get_url()+endpoint
        header = {
            'X-Api-Key':api_key
        }
        payload = {
            'length':length,
            'hasDigits':hasDigits,
            'hasUppercase':hasUppercase,
            'hasSpecial':hasSpecial
        }
        res = requests.get(url=url,headers=header,params=payload)
        if res.status_code == 200:
            return res.json()
        else:
            return None

txt = Text()
print(txt.generate_password('8a2128f0e8254c4c8bbe8561b12f88c0',16,True,True,True))