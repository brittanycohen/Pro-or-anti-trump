import json
class interpreting_tweet(object):
    """interprets a tweet in json  and prints out useful information related to that tweet"""

    def __init__(self,jsonfilename):

        self.jsonfilename=jsonfilename
        self.data=[] # creating an emptry list
        #note we don't need to add this to the initlization because making this an empty list so there is nothing to initilize


        # the whole_file is comprised of many json files or dictionarys the with as statemnt goes through each dictionary element below
        with open(self.jsonfilename,"r") as whole_file:
            for seperate_json_file in whole_file:
                #note! need to use json.loads with an s to read the seperate dictionaries!!
                #making a dictionary of the json document so I can call values
                #note: a json file looks like a dictionary so we can treat it as such when we upload it as a json file
                self.data.append(json.loads(seperate_json_file))# adding each of the json files to the list

    def tweet_info(self):
        """prints the tweet with the person  name, user name , and number of followers they have """
        for json_file in self.data: # going through the list and picking out the json_file
            # now that we have the json file we can treat it like a dictionary by calling a part in the file
            print("\nthe tweet is ------- {}\n\nit was created by ------- {} whoes user name is {} with {} followers\n\n"
            .format(json_file["text"],json_file["user"]["name"],json_file["user"]["screen_name"],json_file["user"]["followers_count"]))
    def tweets(self):
        """returns a list of tweets"""
        tweet=[] # creating a list to add all of the tweets text to
        for json_file in self.data:
            tweet.append(json_file["text"])# adding the text of the tweets to the list
        return tweet # returning the list of tweets so that I can use this function tweets and apply it
    def dictionary_of_screen_name_with_tweet(self):
        """creating a dictionary of the tweet associating with the screen_name"""
        screen_name_with_tweet={}
        for json_file in self.data: # going through the list and picking out the json_file
            screen_name_with_tweet[json_file["user"]["screen_name"]]=json_file["text"]
        return screen_name_with_tweet # returns a dictionary with the screen name and tweet
    def screen_name_with_bio(self):
        """creats a dictionary of the screen name with their bio"""
        accounts_for_pro_or_anti_followers={}
        for json_file in self.data:  # going through the list and picking out the json_file
                #adding the desciption of the bio with the screen name to the dictionary screen_name_with_desciption
                accounts_for_pro_or_anti_followers[json_file["user"]["screen_name"]]=json_file["user"]["description"]
        return(accounts_for_pro_or_anti_followers)# returns dictionary with screen name and bio
