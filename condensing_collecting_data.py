
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
# the data collected is finding who the users that post anti trump and pro trump tweets follow then
# going through a for loop to find the most popular accounts that are followed
# then storing this information in a .p files to use later

import time # time is used to make sure that I don't exceed the rate limit on twitter which only allows me to take 15 pieces of data every 15 mintues

# creating an empty dictionary to put all the followers that the anti_trump supports follow with their freuqncy
anti_trump_integer_dictionary_of_followers={}

#looping through the anti trump screen names until they are finished
#looping from 0:15 every 15 minutes so we don't exceed the ratelimit
a=0
b=15
arbitary_number=50
for number_of_loops in range(0,arbitary_number):
    anti_trumpies=screen_names_dictioanry["anti trump"][a:b]

    for screen_name in anti_trumpies:
        user_followers=api.friends_ids(id=screen_name)# this returns the interger value of the user id a sepcifc user is following(i.e. who the anti trump users follow)

        # getting the amount of times a user is followed by adding their frequncy to the dictionary
        for follower in user_followers:
            if follower in anti_trump_integer_dictionary_of_followers:
                anti_trump_integer_dictionary_of_followers[follower]+=1
            else:
                anti_trump_integer_dictionary_of_followers[follower]=1


    # continuing in the list by incrementing through the list by 15 again so we don't exceed the ratelimit of twitter
    a=b
    b=b+15

    #if we come to the end of the anti_trumpies where there is nothing left in the list then break the for loop
    if anti_trumpies==[]:
        break
    time.sleep(900)# delay code by 900 seconds ie every 15 minutes

#writing the dictionary of anti_trump followers with the frequency to a json file
import pickle
pickle.dump(anti_trump_integer_dictionary_of_followers, open( "anti-trump3.p", "wb" ) )


pro_trump_integer_dictionary_of_followers={}

#looping through the pro trump screen names until they are finished
#looping from 0:15 every 15 minutes so we don't exceed the ratelimit
c=0
d=15
arbitary_number1=50
for number_of_loops in range(0,arbitary_number1):
    pro_trumpies=screen_names_dictioanry["pro trump"][a:b]

    for screen_name in pro_trumpies:
        user_followers=api.friends_ids(id=screen_name)# this returns the interger value of the user id a sepcifc user is following(i.e. who the pro trump users follow)

        # getting the amount of times a user is followed by adding their frequncy to the dictionary
        for follower in user_followers:
            if follower in pro_trump_integer_dictionary_of_followers:
                pro_trump_integer_dictionary_of_followers[follower]+=1
            else:
                pro_trump_integer_dictionary_of_followers[follower]=1


    # continuing in the list by incrementing through the list by 15 again so we don't exceed the ratelimit of twitter
    c=d
    d=d+15
    #if we come to the end of the pro_trumpies where there is nothing left in the list then break the for loop
    if pro_trumpies==[]:
        break
    time.sleep(900)# delay code by 900 seconds ie every 15 minutes

#writing the dictionary of pro_trump followers with the frequency to a json file
pickle.dump(pro_trump_integer_dictionary_of_followers, open( "pro-trump6.p", "wb" ) )
