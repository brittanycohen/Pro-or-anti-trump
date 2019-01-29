
#streams all the information attached to the hashtag trump , ie the tweet, and information from the persons account and writes this information to a json file 
import tweepy
from tweepy.auth import OAuthHandler# autheticat out app

consumer_key = 'Ld96b5kqjdm0KEaRxlhvE7Ri8'
consumer_secret = '60oVWWRx2AFpbcqDuh86GqSNOE3Mki0F4F01VQvRxOlatm5yqt'
access_token = '912785857127514114-bOTdKc5BHnHJvghEM0H7X3jrKz1i2I4'
access_secret = 'ZdaTztZSoe2Sj2x9whDS58orFDTeAXzbkUHR7C3Sy2ZKn'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


from tweepy import Stream
from tweepy.streaming import StreamListener

class MyListener(StreamListener):
# on_data method of a stream listener receives all messages and calls functions according to the message type.
    def on_data(self, data):
        try:
            # storing a the tweet information in json file called ellen
            with open('trump10.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

twitter_stream = Stream(auth, MyListener())

twitter_stream.filter(track=['#trump'])
