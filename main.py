import tweepy
from textblob import TextBlob

consumer_key = 'PASTE CONSUMER KEY'
consumer_secret = 'PASTE CONSUMER SECRET'
access_token = 'PASTE ACCESS TOKEN'
access_token_secret = 'PASTE TOKEN SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

userstring=input('\n\nEnter the Keyword\n\n')
tweet_count=int(input('\n\nEnter no. of Tweets to check (MAX=100)\n\n'))
public_tweets = api.search(userstring,count=tweet_count)

positive_tweets=0
negative_tweets=0
neutral_tweets=0

for tweet in public_tweets:

        print("-------------------------------------------------------------------------")
        print("USERNAME\t",tweet.user.screen_name)
        print("\n")
        print("TWEET TEXT -- ",tweet.text)
        print("\n")
        analysis = TextBlob(tweet.text)
        if analysis.polarity > 0:
            print("\nPositive Statement\n")
            positive_tweets = positive_tweets + 1
            sentiment = 1
        elif analysis.polarity < 0:
            print("\nNegative Statement\n")
            negative_tweets =  negative_tweets + 1
            sentiment = 2
        else:
            print("\nNeutral Statement\n")
            neutral_tweets = neutral_tweets + 1
            sentiment = 0
        print("-------------------------------------------------------------------------")
print("Negative Count::")
print(negative_tweets)
print("Positive Count::")
print(positive_tweets)
print("Neutral Count::")
print(neutral_tweets)
