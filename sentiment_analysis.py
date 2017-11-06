import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from textblob import TextBlob


consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""


auth = OAuthHandler(consumer_key,consumer_secret)

auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
public_tweets=api.search('samsung')
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
