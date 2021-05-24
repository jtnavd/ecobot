import tweepy as twitter
import secrets
import time, datetime

auth = twitter.OAuthHandler(secrets.API_KEY, secrets.API_SECRET_KEY)
auth.set_access_token(secrets.ACCESS_TOKEN, secrets.SECRET_ACCESS_TOKEN)

api = twitter.API(auth)
def bothash(hashtags):
    hashtags = ['ecology', 'environment']
    while True:
        print(datetime.datetime.now())

        for hashtag in hashtags:
            for tweet in twitter.Cursor(api.search, q=hashtag, rpp=15).items(5):
                try:
                    id = dict(tweet._json)['id']
                    text = dict(tweet._json)['text']

                    api.retweet(id)
                    api.create_favorite(id)

                    print("Tweet ID: ", id)
                    print("Tweet Text: ", text)
                except twitter.TweepError as e:
                    print(e.reason)
        time.sleep(10)
def botlike(search, n_tweets = 200):
    for tweet in twitter.Cursor(api.search, search).items(n_tweets):
        try:
            print('Tweet liked')
            time.sleep(10)

        except twitter.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

bothash(['ecology', 'environment'])