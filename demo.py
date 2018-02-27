import tweepy
from textblob import TextBlob

consumer_key = input('\n\nPASTE_CUSTOMER_KEY_HERE\n')
consumer_secret = input('\n\nPASTE_CONSUMER_SECRET_HERE\n')

access_token = input('\n\nPASTE_ACCESS_TOKEN_HERE\n')
access_token_secret = input('\n\nPASTE_ACCESS_TOKEN_SECRET_HERE\n')

print('\n\n')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

userstring=input('\n\nEnter the Keyword\n')
tweet_count=int(input('\n\nEnter no. of Tweets to check\n'))
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
