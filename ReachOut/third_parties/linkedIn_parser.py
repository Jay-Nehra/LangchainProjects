import os 
import requests
from loguru import logger
from dotenv import load_dotenv
from typing import Dict

load_dotenv()

def linkedIn_scrap(profile_url: str, mock: bool = True) -> Dict:
    """
        Scrapes information from the LinkedIn Profile
        Manually scrap information from the LinkedIn profile.
    """
    if mock:
        linkedIn_profile_gist_url = "https://gist.githubusercontent.com/rcapdepaula/43b320e5f9ed1656ab047258f428cbc2/raw/51070719fb0b201a718e1819b580d38ac8f37dfb/ricardo.json"
        
        try:
            response = requests.get(
                url=linkedIn_profile_gist_url,
                timeout=15
            )
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
    else:
        # I am not attempting to directly connect to the LinkedIn API at the moment. `Proxycurl` can be used to do this bu the alloted tokens are quite less and I do not want to create an account at the moment for this POC. 
        return "We do not support the LinkedIn API Connections and scraping at the moment. You can set the `mock` flag to access the precollected linkedIn profile data in a publically available gist or supply your own."
    
    data = response.json()    
    return data


if __name__=='__main__':
    profile_data = linkedIn_scrap('url')
    print(profile_data)