from ast import keyword
from curses import keyname
from distutils.command.config import config
from time import process_time_ns
import tweepy
import configparser
import pandas as pd


#read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

#authenticate
auth = tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)


#public_tweets = api.home_timeline()

#for tweet in public_tweets:
   #print(tweet.user.screen_name)


#User Tweets
user = "Equiideas09"
limit = 200

tweets = api.user_timeline(screen_name = user, count = limit, tweet_mode='extended', exclude_replies=True)


columns = ['User', 'Tweets']
data = []

for tweet in tweets:
    #print(tweet.full_text)
    data.append([tweet.user.screen_name,tweet.full_text])

df = pd.DataFrame(data,columns=columns)
#df.to_csv('file1.csv')
#print(df)



data2 = []
keyword = "hikal"
tweets2 = api.search_tweets(q = keyword, count = limit, tweet_mode='extended')
for tweet2 in tweets2:
    #print(tweet.full_text)
    data2.append([tweet2.user.screen_name,tweet2.full_text])

df2 = pd.DataFrame(data2,columns=columns)
df2.to_csv('file4.csv')
print(df2)


#cursor = tweepy.Cursor(api.user_timeline, id='darshitpatel84', tweet_mode="extended").items(1)

#for i in cursor:
#    print(i)
