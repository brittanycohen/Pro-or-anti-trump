
from textblob import TextBlob
class merging_all_twitter_data():
    """creates a dictionary of that contains every screen name with the polarities attained from interpreting their bio
    who they follow, and sentiment anlysis of the tweet they made"""
    def __init__(self,polarity_from_followers_and_bio,sentiment_analysis_on_tweets_dict):

        self.polarity_from_followers_and_bio=polarity_from_followers_and_bio
        self.sentiment_analysis_on_tweets_dict=sentiment_analysis_on_tweets_dict

        self.dict_anti_trump_screen_names={}
        self.dict_pro_trump_screen_names={}
        self.dict_neutral_supporter_screen_names={}

    def merging_polarity_from_sentiment(self):
        """assigning polarity to the screen names based on the sentiment anlysis of their tweet from class sentiment_analysis
        then combinging this polarity with the poliarties accumulated in the sorting_by_follower to
        create one dictionary that contains the polarites based on all the data collected

        returns one single dictionary that contains the polarities from all the data collected from twitter """

        #going through the anit trump screen_names on their sentiment anlysis and assiging them polarity
        for screen_name in self.sentiment_analysis_on_tweets_dict["anti trump"]:
            self.dict_anti_trump_screen_names[screen_name]=-.1
        #going through the pro trump screen_names on their sentiment anlysis and assiging them polarity
        for screen_name in self.sentiment_analysis_on_tweets_dict["pro trump"]:
            self.dict_pro_trump_screen_names[screen_name]=.1
        #going through the neutral screen names and giving them a a zero polartiy
        for screen_name in self.sentiment_analysis_on_tweets_dict["neutral"]:
            self.dict_neutral_supporter_screen_names[screen_name]=0

        #merging all of the three dictionaries that contain the polarity of the pro anit and nutral accounts from their tweets
        merged_dictionarys_with_polarity={**self.dict_anti_trump_screen_names,**self.dict_pro_trump_screen_names,**self.dict_neutral_supporter_screen_names}

        #looping through this merged dictionary
        # if the screen_name in this merged dictionary is in the dictionary that contains the polarities from evaluting the screen_names bio
        # and the accounts they follow then add the polarity from the sentiment anlysis of the tweet to that screen name as well in that dictinoary
        for screen_name in merged_dictionarys_with_polarity:
            if screen_name in self.polarity_from_followers_and_bio:
                    #adding the polarity from merged_dictionarys_with_polarity to the polarity_from_followers_and_bio
                self.polarity_from_followers_and_bio[screen_name].append(merged_dictionarys_with_polarity[screen_name])

        return(self.polarity_from_followers_and_bio) # returns one single dictionary that contains the polarities from all the data collected from twitter
