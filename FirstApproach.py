import time, os, csv, tweepy, json, datetime
from tweepy import Stream
from tweepy import OAuthHandler, API
from tweepy.streaming import StreamListener

consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token_key = 'your_access_toke_key'
access_token_secret = 'your_access_token_secret'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

def getFOLLOWERS(screen_name):

    now = datetime.datetime.now()
    now_tag = now.strftime('%Y') + now.strftime('%m') + now.strftime('%d') + '_' + now.strftime('%H') + now.strftime('%M') + now.strftime('%S')

    auth = OAuthHandler(consumer_key, consumer_secret) #OAuth object
    auth.set_access_token(access_token_key, access_token_secret)

    api = tweepy.API(auth)

    ids = []
    fw = open('data/' + screen_name + '_' + now_tag + '.followers','w')
    for page in tweepy.Cursor(api.followers_ids, screen_name=screen_name).pages():
        ids.extend(page)
        time.sleep(60)
        for item in page:
            fw.write(str(item) + '\n')

    print len(ids)

getFOLLOWERS('RealAliceCooper')
