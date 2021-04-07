import tweepy
from datetime import datetime, timedelta, timezone
import os
from dotenv import load_dotenv
from discord_webhook import DiscordWebhook
import time

load_dotenv()
# Fill the X's with the credentials obtained by  
# following the above mentioned procedure. 
consumer_key = os.getenv('tweeter_consumer_key')
consumer_secret =  os.getenv('tweeter_consumer_secret')
access_key = os.getenv('tweeter_access_key')
access_secret = os.getenv('tweeter_access_secret')
discord = os.getenv('discord_url')

# Create your dictionary class  
class my_dictionary(dict):  
    
            # __init__ function  
            def __init__(self):  
                self = dict()  
                
            # Function to add key:value  
            def add(self, key, value):  
                self[key] = value

def get_tweets(username): 
        
        load_dotenv()
        # Authorization to consumer key and consumer secret 
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
        # Access to user's access key and access secret 
        auth.set_access_token(access_key, access_secret) 
        # Calling api 
        api = tweepy.API(auth) 
        # 200 tweets to be extracted 
        ##get all the tweets
        tweets = []
        for i in [1,2,3]:
            tweets+= api.user_timeline(screen_name=username, page = i)

        ##set the date to last 24hours
        date=datetime.utcnow()- timedelta(minutes=2)
       
        for tweet in tweets:
        # if the tweet was created in last 24hours and contains $ sign for ticker
            if tweet.created_at > date:
                tweet_date= tweet.created_at
                data = str(tweet_date.replace(tzinfo=timezone.utc).astimezone(tz=None).time())+" "+'User: '+tweet.user.screen_name+ " " + tweet.text
                webhook = DiscordWebhook(url=discord, content=data)
                response = webhook.execute()
                print(response)
                time.sleep(4)
        
# Driver code 
if __name__ == '__main__': 
  
    # Here goes the twitter handle for the user 
    # whose tweets are to be extracted. 
    get_tweets("johnscharts")
    get_tweets("theclamshanks")
    get_tweets("OptionsHawk")
    get_tweets("traderstewie")
    get_tweets("danzanger")
    get_tweets("RedDogT3")
    get_tweets("IvanhoffTrades")

