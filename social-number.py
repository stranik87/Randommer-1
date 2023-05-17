import requests
from randommer import Randommer


class SocialNumber(Randommer):
    def get_SocialNumber(self, api_key: str) -> str:
        '''get SocialNumber

        Args:
            api_key (str): api key

        Returns:
            str: number as str
        '''
        endpoint = 'SocialNumber'
        url = self.get_url()+endpoint
        header = {
            'X-Api-Key':api_key
        }
        res = requests.get(url=url,headers=header)
        if res.status_code == 200:
            return res.json()
        else:
            return None
        
num = SocialNumber()
print(num.get_SocialNumber('8a2128f0e8254c4c8bbe8561b12f88c0'))
