import tweepy
from textblob import TextBlob

consumer_key = 'PASTE_CUSTOMER_KEY_HERE'
consumer_secret = 'PASTE_CONSUMER_SECRET_HERE'

access_token = 'PASTE_ACCESS_TOKEN_HERE'
access_token_secret = 'PASTE_ACCESS_TOKEN_SECRET_HERE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

userstring=input('Enter the Keyword\n')
tweet_count=int(input('Enter no. of Tweets to check\n'))
public_tweets = api.search(userstring,count=tweet_count)

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    if analysis.polarity > 0:
        print('\nPositive Statement\n')
    elif analysis.polarity < 0:
        print('\nNegative Statement\n')
    else:
        print('\nNeutral Statement\n')
    print("")
