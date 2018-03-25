from os import sys

import tweepy
from google.cloud import language, translate
from google.cloud.language import enums, types


def translated_text(text):
    translate_client = translate.Client()
    translation = translate_client.translate(text,target_language='en')
    return (format(translation['translatedText']))

def entity_sentiment_text(text):
    client = language.LanguageServiceClient()
    document = types.Document(content=text.encode('utf-8'), type=enums.Document.Type.PLAIN_TEXT)
    encoding = enums.EncodingType.UTF32
    if sys.maxunicode == 65535:
        encoding = enums.EncodingType.UTF16
    result = client.analyze_sentiment(document, encoding).document_sentiment
    sentiment = format(result.score)
    return(sentiment)

class App(object):
    def get_tweet_sentiment(self,userstring,tweet_count):
        consumer_key = 'DvsIlWzzMRTotWwvXFjGsWTOF'
        consumer_secret = '0uUOA5FqWcJMqDrCiFT2GoXNi3IyiWqcEuTwqvvv6qlKhnzups'
        access_token = '751940867242549248-POjtMipdB2kYC5EctSz7QOIfLCa30KL'
        access_token_secret = 'M5YybNemnJIIAfznpcghoX47F5Udtwi7g9Ly2LvobvGpX'
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        public_tweets = api.search(userstring, count=tweet_count)
        positive_tweets = 0
        negative_tweets = 0
        neutral_tweets = 0
        tweet_text_with_sentiment = []
        for tweet in public_tweets:
            tweets= {}
            user_name = tweet.user.screen_name
            tweets['user_name'] = user_name
            tweet_text = tweet.text
            tweet_text = str(translated_text(tweet_text))
            analysis = float(entity_sentiment_text(tweet_text))
            tweets['sentiment'] = float(analysis)
            tweets['tweet_text'] = tweet_text
            if analysis > 0:
                positive_tweets = positive_tweets + 1
            elif analysis < 0:
                negative_tweets = negative_tweets + 1
            else:
                neutral_tweets = neutral_tweets + 1
            tweet_text_with_sentiment.append(tweets)
        return(tweet_text_with_sentiment)