import tweepy
from textblob import TextBlob


def startapp():
    try:
        consumer_key = 'PASTE CONSUMER KEY HERE'
        consumer_secret = 'PASTE CONSUMER SERET HERE'
        access_token = 'PASTE ACCESS TOKEN HERE'
        access_token_secret = 'PASTE ACCESS TOKEN SECRET HERE'
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        userstring = input('\n\nEnter the Keyword\n\n')
        tweet_count = int(input('\n\nEnter no. of Tweets to check (MAX=100)\n\n'))
        public_tweets = api.search(userstring, count=tweet_count)
    except:
        print("\nINVALID INPUT!! or AUTHENTICATION FAILED\n")
        input("\n\nPress Any Key To Exit\n\n")
        exit
    positive_tweets = 0
    neutral_tweets = 0
    try:
        for tweet in public_tweets:
                print("-------------------------------------------------------------------------")
                print("USERNAME\t@", tweet.user.screen_name)
                print("\n")
                print("TWEET TEXT -- ", tweet.text)
                print("\n")
                analysis = TextBlob(tweet.text)
                if analysis.polarity > 0:
                    print("\nPositive Statement\n")
                    positive_tweets = positive_tweets + 1
                elif analysis.polarity < 0:
                    print("\nNegative Statement\n")
                    negative_tweets = negative_tweets + 1
                else:
                    print("\nNeutral Statement\n")
                    neutral_tweets = neutral_tweets + 1
                print("-------------------------------------------------------------------------")
        print("\nNegative Count::")
        print(negative_tweets)
        print("\nPositive Count::")
        print(positive_tweets)
        print("\nNeutral Count::")
        print(neutral_tweets)
        input("\n\nPress Any Key To Exit\n\n")
    except:
        print("\n\nTWEET NOT FOUND OR NO INTERNET ACCESS\n\n")
        input("\n\nPress Any Key To Exit\n\n")
        exit
try:
    startapp()
except:
    print("\n\nERROR\n\n")
    print("\n\nNO INTERNET ACCESS\n\n")
    input("\n\nPress Any Key To Exit\n\n")
    exit
