#import json
from json_Tweet_interpreter import interpreting_tweet
f=interpreting_tweet("trump10.json")
screen_name_with_bio_description=f.screen_name_with_bio()

from condensed_bio import reading_bio
c=reading_bio(screen_name_with_bio_description)
interpreting_bio=c.interpreting_bio()

from condensed_class import comparing_pro_and_anti_followers
f=comparing_pro_and_anti_followers("anti-trump3.p","pro-trump6.p")
accounts_for_pro_or_anti_followers=f.accounts_only_pro_or_anti_follow()



class sorting_by_follower(object):
    """gives polarity to the each screen name based on if they follow more pro or anti trump accounts and
    adds this polarity to the already existing polarity calculated in the condensed_bio"""

    def __init__(self,neutral_trump2_pfile,anti_collect_like_neutral_pfile,pro_collect_like_neutral_pfile,interpreting_bio,accounts_for_pro_or_anti_followers):
        self.interpreting_bio=interpreting_bio
        self.accounts_for_pro_or_anti_followers=accounts_for_pro_or_anti_followers

        self.neutral_trump2_pfile=neutral_trump2_pfile
        self.anti_collect_like_neutral_pfile=anti_collect_like_neutral_pfile
        self.pro_collect_like_neutral_pfile=pro_collect_like_neutral_pfile

        import pickle # import pickle to read json file

        self.neutral_accounts_and_people_they_follow= pickle.load( open( self.neutral_trump2_pfile, "rb" ) ) # opening json file
        self.pro_accounts_and_people_they_follow= pickle.load( open( self.anti_collect_like_neutral_pfile, "rb" ) ) # opening json file
        self.anti_accounts_and_people_they_follow= pickle.load( open( self.pro_collect_like_neutral_pfile, "rb" ) ) # opening json file

        #merginging the 3 dictionarys above to get a dictionary of all the screen names with every person they follow
        self.all_accounts_with_followers={**self.neutral_accounts_and_people_they_follow,**self.pro_accounts_and_people_they_follow,**self.anti_accounts_and_people_they_follow}

#looping through the neutral accounts  dictionary to obtain the people they follow and compare with positive and negative followers
    def followers(self):
        """ go through a dictionary of all the screen names with every person they follow then finding
        how many pro and anti trump accounts this person follows and assigning a polarity to them
        based on if they follow more pro trump accounts as appose to anit trump accounts and vise versa then
        adding the polarities from the class reading_bio to the polarities just found based on who the person follows and
        returning the screen names with polarities from interpreting_bio and amount of pro or anti trump accounts followed """

        follower_anlysis_with_screen_name={}

        for screen_name in self.all_accounts_with_followers:

            # finding the common followers these screen names have with the top most followed anti trump accounts and the top most pro trump accounts
            common_followers_with_anti_supports=list(set(self.all_accounts_with_followers[screen_name]) & set(self.accounts_for_pro_or_anti_followers["anti trump"]))# the common elements from each set turned into a list
            common_followers_with_pro_supports=list(set(self.all_accounts_with_followers[screen_name]) & set(self.accounts_for_pro_or_anti_followers["pro trump"]))# the common elements from each set turned into a list

            # if the person followers more anti trump twitter accounts than pro trump they are a anti trump supporter
            # assigning a polarity to them based on if they lean more to following more pro trump accounts vs anti trump accounts and vise versa
            if len(common_followers_with_anti_supports)>=3 and len(common_followers_with_pro_supports)<3:
                follower_anlysis_with_screen_name[screen_name]=-.2

            elif len(common_followers_with_pro_supports)>=3 and len(common_followers_with_anti_supports)<3:
                follower_anlysis_with_screen_name[screen_name]=.2

            #  if the person the same amount of anti and pro trump accounts
            elif len(common_followers_with_anti_supports)==(common_followers_with_pro_supports):
                follower_anlysis_with_screen_name[screen_name]=0

            # if they follower a larger amount of anti trump accounts in comparison to pro trump accoutns
            elif len(common_followers_with_anti_supports)>(4+len(common_followers_with_pro_supports)):
                follower_anlysis_with_screen_name[screen_name]=-.2

            # if they follower a larger amount of pro trump accounts in comparison to anti trump accoutns
            elif len(common_followers_with_pro_supports)>(4+len(common_followers_with_anti_supports)):
                follower_anlysis_with_screen_name[screen_name]=.2

            # if they follow a small amount of either of the accounts still can't determine
            else:
                follower_anlysis_with_screen_name[screen_name]=0

        # adding the polarities from the class reading_bio to the list in the dictionary follower_anlysis_with_screen_name
        for screen_name in follower_anlysis_with_screen_name:
            if screen_name in self.interpreting_bio:
                #adding the polarity from follow_anlysis_Wtih_screen_anme to the intpereting bio
                self.interpreting_bio[screen_name].append(follower_anlysis_with_screen_name[screen_name])
        return(self.interpreting_bio)# returns now the screen names with polarity from bio interpetation and amount of pro or anti trump accounts followed
