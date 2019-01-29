#________________________________________________________________________________
#importing all of the classes made to run condensed_merged_sentiment

# to run condensed_bio need to import interpreting_tweet
from json_Tweet_interpreter import interpreting_tweet
f=interpreting_tweet("trump10.json")
screen_name_with_bio_description=f.screen_name_with_bio()
dictionary_of_screen_name_with_tweet=f.dictionary_of_screen_name_with_tweet()

from condensed_sentiment import sentiment_analysis
c=sentiment_analysis(dictionary_of_screen_name_with_tweet)
sentiment_analysis_on_tweets_dict=c.sentiment_analysis_on_tweets()

from condensed_bio import reading_bio
c=reading_bio(screen_name_with_bio_description)
interpreting_bio=c.interpreting_bio()

from condensed_class import comparing_pro_and_anti_followers
f=comparing_pro_and_anti_followers("anti-trump3.p","pro-trump6.p")
top_accounts_for_pro_or_anti_followers=f.accounts_only_pro_or_anti_follow()

# to run sorting_by_follower we need information form reading_bio and comparing_pro_and_anti_followers
from condensed_sorting import sorting_by_follower
y=sorting_by_follower("neutral-trump2.p","anti-collect_like_neutral.p","pro-collect_like_neutral.p",interpreting_bio,top_accounts_for_pro_or_anti_followers)
polarity_from_followers_and_bio=y.followers()

#________________________________________________________________________________

# now that everything above is imported we can now run
from condensed_merged_sentiment import merging_all_twitter_data
c=merging_all_twitter_data(polarity_from_followers_and_bio,sentiment_analysis_on_tweets_dict)
merged_polarities=c.merging_polarity_from_sentiment()

# looping through the screen_names with the list of polarities collected from all the data from twitter
for screen_name in merged_polarities:

    #summing through list of polaritys per screen name and attaching the tweet that person made

    #if they have a negative polarity they are some percentage anti trump
    if sum(merged_polarities[screen_name])<0:
        if screen_name in dictionary_of_screen_name_with_tweet:
            print("-----------\n{} has a correlation coefficient of {} so they are an anti trump supporter, their tweet was: \n\n{}\n".format(screen_name,sum(merged_polarities[screen_name]),dictionary_of_screen_name_with_tweet[screen_name]))

    #if they have a positive polarity they are some percentage pro trump
    elif sum(merged_polarities[screen_name])>0:
        if screen_name in dictionary_of_screen_name_with_tweet:
                print("-----------\n{} has a correlation coefficient of {} so they are a pro trump supporter, their tweet was: \n\n{}\n".format(screen_name,sum(merged_polarities[screen_name]),dictionary_of_screen_name_with_tweet[screen_name]))

    #if they have a zero polarity we still don't know enough about the person
    elif sum(merged_polarities[screen_name])==0:
        if screen_name in dictionary_of_screen_name_with_tweet:
                print("-----------\n{} has a correlation coefficient of {}, this means with the information collected from twitter we are unable to determine if they support trump or not.\ntheir tweet was: \n\n{}\n".format(screen_name,sum(merged_polarities[screen_name]),dictionary_of_screen_name_with_tweet[screen_name]))
