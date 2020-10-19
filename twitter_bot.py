import tweepy
import requests
from bs4 import BeautifulSoup

from bot_keys import *

theURL = "https://www.commodity.com/debt-clock/us/"


def main():
    
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    
    
    print("Getting Data...")
    
    response = requests.get(theURL)
    
    if response.status_code != 200:
        print("Error fetching page")
        exit()
        
    content = response.content
    theHTML = BeautifulSoup(response.content, 'html.parser')
    
    theDebt = theHTML.find(id="debtDisplay").text
    
    print("Today\'s Debt: " + str(theDebt))
            
    api.update_status(f"Today\'s National Debt is ${theDebt}")

    print("Tweet Sent!")


if __name__ == "__main__":
    main()