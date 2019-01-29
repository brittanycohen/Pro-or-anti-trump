
import tweepy # twitters api
from tweepy.auth import OAuthHandler# autheticat out app
#_________________________________________________________________________________________
#autehtication of twitter account
consumer_key = 'Ld96b5kqjdm0KEaRxlhvE7Ri8'
consumer_secret = '60oVWWRx2AFpbcqDuh86GqSNOE3Mki0F4F01VQvRxOlatm5yqt'
access_token = '912785857127514114-bOTdKc5BHnHJvghEM0H7X3jrKz1i2I4'
access_secret = 'ZdaTztZSoe2Sj2x9whDS58orFDTeAXzbkUHR7C3Sy2ZKn'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
#____________________________________________________________________________________________
from textblob import TextBlob
from json_Tweet_interpreter import interpreting_tweet
f=interpreting_tweet("trump10.json")
dictionary_of_screen_name_with_tweet=f.dictionary_of_screen_name_with_tweet()

from condensed_sentiment import sentiment_analysis
# using the dictionary_of_screen_name_with_tweet from the json_tweet interpreter to imput into the sentiment anylisis class to anylisis
c=sentiment_analysis(dictionary_of_screen_name_with_tweet)
screen_names_dictioanry=c.sentiment_analysis_on_tweets()
#____________________________________________________________________________________________
#using the screen_names_dictioanry above to go through and collect data from twitter
# the data collected is finding all the accounts that each neutral, pro, and anti trump account follows, putting this into dictionarys
#that contains the name of the neutral, pro ,and anti account with who they follow then storing this information in a .p file to use later



#collecting data of all the followers that each neutral account has
import time # time is used to make sure that i don't exceed the rate limit which only allows me to take 15 pieces of data every 15 mintues

# creating an empty dictionary to put all the followers that the neutral accounts follow and the neutral accounts name
neutral_tweet_followers={}
anti_tweet_followers={}
pro_tweet_followers={}


#looping through the neutral screen names until they are finished
#looping from 0:15 every 15 minutes so we don't exceed the ratelimit
a=0
b=15
arbitary_number=50
for number_of_loops in range(0,arbitary_number):

    neutral_peeps=screen_names_dictioanry["neutral"][a:b]

    for screen_name in neutral_peeps:
        #adding neutral_tweet_followers to dictionary
        neutral_tweet_followers[screen_name]=api.friends_ids(id=screen_name)  # this returns the interger value of the user id a sepcifc user is following(i.e. who the anti trump users follow)

    # continuing in the list by incrementing through the list by 15 again so we don't exceed the ratelimit of twitter
    a=b
    b=b+15
    #if we come to the end of the pro_trumpies where there is nothing left in the list then break the for loop
    if neutral_peeps==[]:
        break
    time.sleep(900)# delay code by 900 seconds ie every 15 minute

#writing the dictionary of anti_trump followers with the count to a json file
import pickle
pickle.dump(neutral_tweet_followers, open( "neutral-trump9.p", "wb" ) )

#collecting data of all the followers that each anti account has
e=0
f=15
arbitary_number2=50
for number_of_loops in range(0,arbitary_number2):
    anti_peeps=screen_names_dictioanry["anti trump"][e:f]

    for screen_name in anti_peeps:
        #adding to anti_tweet_followers dictionary
        anti_tweet_followers[screen_name]=api.friends_ids(id=screen_name) # this returns the interger value of the user id a sepcifc user is following(i.e. who the anti trump users follow)

    # continuing in the list by incrementing through the list by 15 again so we don't exceed the ratelimit of twitter
    e=f
    f=f+15
    #if we come to the end of the anti_trumpies where there is nothing left in the list then break the for loop
    if anti_peeps==[]:
        break
    time.sleep(900)# delay code by 900 seconds ie every 15 minute

#writing the dictionary of anti_trump followers with the count to a json file
pickle.dump(anti_tweet_followers, open( "anti-collect_like_neutral9.p", "wb" ) )

#collecting data of all the followers that each pro account has
c=0
d=15
arbitary_number1=50
for number_of_loops in range(0,arbitary_number1):
    pro_peeps=screen_names_dictioanry["pro trump"][c:d]

    for screen_name in pro_peeps:
        #adding to pro_tweet_followers dictionary
        pro_tweet_followers[screen_name]=api.friends_ids(id=screen_name) # this returns the interger value of the user id a sepcifc user is following(i.e. who the anti trump users follow)

    # continuing in the list by incrementing through the list by 15 again so we don't exceed the ratelimit of twitter
    c=d
    d=d+15
    #if we come to the end of the pro_trumpies where there is nothing left in the list then break the for loop
    if pro_peeps==[]:
        break
    time.sleep(900)# delay code by 900 seconds ie every 15 minute

#writing the dictionary of anti_trump followers with the count to a json file
pickle.dump(pro_tweet_followers, open( "pro-collect_like_neutral9.p", "wb" ) )
