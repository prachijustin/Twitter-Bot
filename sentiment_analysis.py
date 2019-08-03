from credentials import *
import re 
from tweepy import OAuthHandler 
from textblob import TextBlob 

#function to remove links/special characters from the tweet
def cleanTweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split()) 


#analysis tweet sentiment
def getTweetSentiment(tweet):
    analysis = TextBlob(cleanTweet(tweet))
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'


query = input('Enter person/place/or anything: ')

fetched_tweets = api.search(q = query, count = 200)

tweets = []
for tweet in fetched_tweets:
    parsed_tweets = {}

    parsed_tweets['text'] = tweet.text
    parsed_tweets['sentiment'] = getTweetSentiment(tweet.text)

    if tweet.retweet_count > 0:
        if parsed_tweets not in tweets:
            tweets.append(parsed_tweets)
    else:
        tweets.append(parsed_tweets)


positive_tweets = []
negative_tweets = []
neutral_tweets = []
for tweet in tweets:
    if tweet['sentiment'] == 'Positive':
        positive_tweets.append(tweet)
    elif tweet['sentiment'] == 'Negative':
        negative_tweets.append(tweet)
    else:
        neutral_tweets.append(tweet)


print('Positive tweets percentage: {} %'.format((len(positive_tweets)/len(tweets))*100))
print('Negative tweets percentage: {} %'.format((len(negative_tweets)/len(tweets))*100))
print('Neutral tweets percentage: {} %'.format((len(neutral_tweets)/len(tweets))*100))

print('*'*30)
print("Positive tweets:") 
for tweet in positive_tweets[:10]: 
    print(tweet['text']) 
  
print('*'*30)
print("Negative tweets:") 
for tweet in negative_tweets[:10]: 
    print(tweet['text']) 

print('*'*30)
print("Neutral tweets:") 
for tweet in neutral_tweets[:10]: 
    print(tweet['text']) 