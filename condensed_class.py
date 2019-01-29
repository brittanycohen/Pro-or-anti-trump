
import pickle # import pickle to read json file
class comparing_pro_and_anti_followers(object):
    """this class takes in two files:
    file 1: for the people that the pro trump screen names follow and the frequency of each of those followsers.
    file 2:for the people that the anti trump screen names follow and the frequency of each of those followsers

     It then sorts two files in order of most frequent followed accounts of the pro and anti trump accounts
     then compares these two lists to find the distinct followers of only pro and only anti trump accounts
     to find a pattern to help asses the rest of the undecided neutral accounts."""

    def __init__(self,anti_trump_pfile,pro_trump_pfile):

        self.anti_trump_pfile=anti_trump_pfile
        self.pro_trump_pfile=pro_trump_pfile

        self.anti_trump_dictionary= pickle.load( open( self.anti_trump_pfile, "rb" ) ) # opening anti_trump json file
        self.pro_trump_dictionary=pickle.load(open(self.pro_trump_pfile,"rb"))# opening pro_trump json file

        self.list_of_order_of_people_followed_most_by_anti_trumpies=[] # empty list that will be added to from the functiosn below
        self.list_of_order_of_people_followed_most_by_pro_trumpies=[]
        self.common_followers=[]

        self.top_followed_pro_and_anti_twitter_accounts={"pro trump":[],"anti trump":[]}

    def accounts_only_pro_or_anti_follow(self):
        """ordering the anti trump and pro trump dictionary by highest freuqnecy of followers
         then extracting the top 30 highest followed accounts for each group, then finding the common followers from the top 30
         anti and pro trump accounts followed and extracting any similiaries that they have then returning a dictionary seperating
         by pro trump and anti trump with the top pro trump accounts followed and the top anit trump accounts followed
         """

         #sorting ferquency by highest value first ( this turns the dictionary into a list)
        order_of_people_followed_most_by_anti_trumpies=(sorted(self.anti_trump_dictionary.items(), key=lambda t: t[1], reverse=True))
        order_of_people_followed_most_by_pro_trumpies=(sorted(self.pro_trump_dictionary.items(), key=lambda t: t[1], reverse=True))


        # going through the ordered lists for the anti and pro screen names and getting rid of the frequencies, only grabbing the top 30 screen names and putting
        #them into a new list
        for name_of_followers_with_frequency in order_of_people_followed_most_by_anti_trumpies[:30]:
            #the [0] grabs the first item in the tuple for the order_of_people_followed_most_by_anti_trumpies which is a list of tuples then adds to the empty list
            self.list_of_order_of_people_followed_most_by_anti_trumpies.append(name_of_followers_with_frequency[0])#this is a list of the top 30 accounts (in integers) followed most by anti trump supports

        for name_of_followers_with_frequency in order_of_people_followed_most_by_pro_trumpies[:30]:
            #the [0] grabs the first item in the tuple for the order_of_people_followed_most_by_pro_trumpies which is a list of tuples then adds to the empty list
            self.list_of_order_of_people_followed_most_by_pro_trumpies.append(name_of_followers_with_frequency[0]) #this is a list of the top 30 accounts (in integers) followed most by pro trump supports


        # finding the common followers between the pro and anti trump lists
        self.common_followers=list(set(self.list_of_order_of_people_followed_most_by_pro_trumpies) & set(self.list_of_order_of_people_followed_most_by_anti_trumpies))# the common elements from each set turned into a list

        # comparing the common_followers ( ie followers that both anti and pro trump supports share)
        # with the top aint trump accounts followed and  the same for the top pro trump accounts followed
        #and creating new lists where  there are no common followers in the top anti trump accounts followed and the
        #top pro trump accounts followed
        screen_names_of_only_anti_trumpies_follow=list(set(self.common_followers)^set(self.list_of_order_of_people_followed_most_by_anti_trumpies))
        screen_names_of_only_pro_trumpies_follow=list(set(self.common_followers)^set(self.list_of_order_of_people_followed_most_by_pro_trumpies))

        #importing collections so that we can append to a dictionary
        from collections import defaultdict

        #looping through screen_names_of_only_anti_trumpies_follow and screen_names_of_only_pro_trumpies_follow and
        #creating a dictionary seperating by pro and anti trump with the top pro trump accounts followed and the top anit trump accounts followed
        for follower_integer in screen_names_of_only_pro_trumpies_follow:
            self.top_followed_pro_and_anti_twitter_accounts["pro trump"].append(follower_integer)
        #print(self.top_followed_pro_and_anti_twitter_accounts)
        for follower_integer in screen_names_of_only_anti_trumpies_follow:
            self.top_followed_pro_and_anti_twitter_accounts["anti trump"].append(follower_integer)

        return(self.top_followed_pro_and_anti_twitter_accounts)
