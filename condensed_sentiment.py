# using sentiment anlysis package from textblob
from textblob import TextBlob

class sentiment_analysis():
    """sentiment anylsis on all of the tweets to help provide insite on if they are pro
    or anti trump """
    def __init__(self,dictionary_of_tweets_with_screen_name):
        self.dictionary_of_tweets_with_screen_name=dictionary_of_tweets_with_screen_name

        self.pro_trump_tweet=0
        self.anti_trump_tweet=0
        self.nuetral_tweets=0

        self.pro_trump_screen_names=[]
        self.anti_trump_screen_names=[]
        self.neutral_supporter_screen_names=[]

        self.all_screen_names={"pro trump":[],"anti trump":[],"neutral":[]}

    def sentiment_analysis_on_tweets(self):
        """this does sentiment anlysis on each of the tweets, counts how many pro_trump tweets, anti_trump tweets and neutral tweets there are
        then seperates the screen names of each of the accounts three categories: pro, anti, or neutral and returns that in a dictioanry"""

        #looping through dictionary
        for screen_name in self.dictionary_of_tweets_with_screen_name:

            #note: to grab the tweets in the dictionary_of_tweets_with_screen_name we do dictionary_of_tweets_with_screen_name[screen_name]

            # going through the tweets to do a sentiment anlysis
            sentiment_analysis=TextBlob(self.dictionary_of_tweets_with_screen_name[screen_name])# creating a handle for TextBlob on the tweets

            # the if statmenst below addressing the polarity of the tweet (ie if its positive or negative)

            # positive polarity means in support of trump (ie saying nice things about the man...)
            if sentiment_analysis.sentiment.polarity > 0 :
                self.pro_trump_tweet+=1# incrementing the positive tweets (counting how many pro_trump tweets we have )
                self.pro_trump_screen_names.append(screen_name)


            # negative polarity opposing trump
            elif sentiment_analysis.sentiment.polarity < 0:
                self.anti_trump_tweet+=1# incrementing the negative tweets
                self.anti_trump_screen_names.append(screen_name)

            # neautral tweets (ie these may not be neutral but textblob can't detect sarcasm)
            else:
                self.nuetral_tweets+=1
                self.neutral_supporter_screen_names.append(screen_name)
                

        #importing collections to append to a dictiaonry
        from collections import defaultdict
        # looping through all the screen names putting them into lists inside a dictionary of what the pro trump screen names are
        #the anti trump screen names and the neutral trump screen names based on the sentiment anlysis
        for screen_name in self.pro_trump_screen_names:
            self.all_screen_names["pro trump"].append(screen_name)
        for screen_name in self.anti_trump_screen_names:
            self.all_screen_names["anti trump"].append(screen_name)
        for screen_name in self.neutral_supporter_screen_names:
            self.all_screen_names["neutral"].append(screen_name)

        return(self.all_screen_names) # dictionary with all the screen names seperated by pro anti or neutral based on sentiment anlsyis
