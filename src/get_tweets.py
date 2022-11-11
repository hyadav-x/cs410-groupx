import configparser
import pandas as pd
import tweepy
from datetime import datetime


# read config
# todo: parameterize the config.ini
config = configparser.ConfigParser(interpolation=None)
config.read('config.ini')

access_key = config['twitter']['access_key']
access_key_secret = config['twitter']['access_key_secret']
consumer_key = config['twitter']['consumer_key']
consumer_key_secret = config['twitter']['consumer_key_secret']


# parameters for search
date_since = datetime.today().strftime('%Y-%m-%d')


df = pd.DataFrame(columns=['username',
                            'description',
                            'location',
                            'following',
                            'followers',
                            'totaltweets',
                            'retweetcount',
                            'text',
                            'hashtags'])


auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_key, access_key_secret)

api = tweepy.API(auth)

hashtag="ElectionDay"

tweets = tweepy.Cursor(api.search_tweets,
                               hashtag, lang="en",
                               since_id=date_since,
                               tweet_mode='extended').items(10)

list_tweets = [tweet for tweet in tweets]

i = 1

for tweet in list_tweets:
    username = tweet.user.screen_name
    description = tweet.user.description
    location = tweet.user.location
    following = tweet.user.friends_count
    followers = tweet.user.followers_count
    totaltweets = tweet.user.statuses_count
    retweetcount = tweet.retweet_count
    hashtags = tweet.entities['hashtags']

    try:
        text = tweet.retweeted_status.full_text
    except AttributeError:
        text = tweet.full_text
    hashtext = list()
    for j in range(0, len(hashtags)):
        hashtext.append(hashtags[j]['text'])

    ith_tweet = [username, description,
                location, following,
                followers, totaltweets,
                retweetcount, text, hashtext]

    df.loc[len(df)] = ith_tweet

    i = i+1

filename = hashtag + '_tweets.csv'

df.to_csv(filename, index=False)