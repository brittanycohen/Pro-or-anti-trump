
from json_Tweet_interpreter import interpreting_tweet
f=interpreting_tweet("trump10.json")
#dictionary_of_screen_name_with_tweet=f.dictionary_of_screen_name_with_tweet()
screen_name_with_bio_description=f.screen_name_with_bio()

class reading_bio(object):
    """this function reads someones bio to see if they state if they are a pro or anti trump supporter"""

    def __init__(self,screen_name_with_bio_description):
        self.screen_name_with_bio_description=screen_name_with_bio_description
        self.screen_names=[]
        #everything in list lowercase to have issues with matchign later because converted words to lower case
        self.hashtags_dictionary={"Pro trump hashtags":["tcot","potus","buildthewall","foxnews","rightwing","gun","americafirst"
        ,"cnnisfakenews","trump2020","maga","wall","peotus","usa","makeamericagreatagain","draintheswamp","buildthatwall"
        ,"conservative","republican","constitution","constitutions","trumptrain","ccw247","deplorables","wall"],"anti trump hashtags":["trumpIsAMoron",
        "trumpbaitandwwitch","liberals","liberal","moron","impeachtrump","theresistance","democrats","resist","idiotinchief",
        "guncontrol","birthcontrol","fakepresident","impeachtrumpnow","resistance","notmypresident","berniesanders",
        "hillaryclinton","barackobama","obama","hillary","bernie","nowalls","equality","equalityforeveryone","equalityneedsyou",
        "equalityforall","equalityadvocate","equality4all","strengthinnumbers","strongertogether","lovetrumpshate","democrat",
        "freedom","trumpresign","trumprussia"]}
        #self.screen_name_with_desciption={}

    def interpreting_bio(self):
        """going through the bio's of every screen name and seeing if they state anything pro or anti about trump by parsing each word
        from their bio and comparing it to the hashtags_dictionary then assigning polarity to each screen name based on
        if they have something on their bio that is positive negative or a neutral about trump
        this funciton returns a dictionary with the screen name and the polarity assigned based on the evalution from
        their bio """

        #collectes a list of all the screen names that tweeted about trump
        for screen_name in self.screen_name_with_bio_description:
            self.screen_names.append(screen_name)

        bio_anlysis_with_screen_name={}
        pro_trump_based_on_bio=[]
        anti_trump_based_on_bio=[]
        rest_of_users=[]

        # looping through all the screen names of people that tweeted about trump
        for screen_name in self.screen_name_with_bio_description:

            # going through the dictionary of the screen name with the bio descriptions and extracting the descptions as a string
            words_in_bio=str(self.screen_name_with_bio_description[screen_name])

            # splitting the words up in the bio
            words_split_up=words_in_bio.split()

            #looping through one word at a time to see if any of the words in a bio are in either the pro
            #or anti trump hashtag dictinoary
            for word in words_split_up:

                #(uses import string) get rid of any punctuation
                import string
                #getting rid of punctionation attached to a word to match the format is the hashtag dictionary (i.e. no punctionary)
                word_with_no_puncuation_attached=word.translate(str.maketrans('','',string.punctuation))
                # making every word lowercase to match the hashtags_dictionary form
                lower_case_no_puncuation=word_with_no_puncuation_attached.lower()

                # if the word is in the pro trump section for the hashtags_dictionary add this screen name to pro_trump_based_on_bio
                if lower_case_no_puncuation in self.hashtags_dictionary["Pro trump hashtags"]:
                    pro_trump_based_on_bio.append(screen_name)

                # if the word is in the anti trump section for the hashtags_dictionary add this screen name to anti_trump_based_on_bio
                if lower_case_no_puncuation in self.hashtags_dictionary["anti trump hashtags"]:
                    anti_trump_based_on_bio.append(screen_name)

                #word not in the hashtags_dictionary  add screen name to rest_of_userss
                else:
                    rest_of_users.append(screen_name)

            # getting rid of duplicates in pro_trump_based_on_bio and anti_trump_based_on_bio because above we go through each word
            # so even if the screen name had a word from the hashtags_dictionary the rest of the words might not be and would be adding
            # that screen name multiple times to the rest_of_users
            pro_trump_no_duplicates_bio=list(set(pro_trump_based_on_bio))
            anti_trump_no_duplicates_bio=list(set(anti_trump_based_on_bio))

            #finding the commone screen names in the pro_trump_no_duplicates_bio and anti_trump_no_duplicates_bio
            # and then removing that commmon screen name that is in the pro and anit trump list so its just left in the
            #rest of the users list
            common_in_anti_and_pro=list(set(pro_trump_no_duplicates_bio)&set(anti_trump_no_duplicates_bio))
            for screen_name in common_in_anti_and_pro:
                pro_trump_no_duplicates_bio.remove(screen_name)
                anti_trump_no_duplicates_bio.remove(screen_name)

            # finding the common values between anti_trump_no_duplicates_bio and screen names and
            #pro_trump_no_duplicates_bio and screen names
            common_in_anti_and_screen_names=list(set(self.screen_names)&set(anti_trump_no_duplicates_bio))
            common_in_pro_and_screen_names=list(set(self.screen_names)&set(pro_trump_no_duplicates_bio))

            #removing these common screen names from the screen_names list so that I can get a
            #list of screen_names for people that aren't pro or anti (ie. our rest_of_users but ignoring that because
            #that has many duplicates)
            for screen_name in common_in_anti_and_screen_names:
                self.screen_names.remove(screen_name)
            for screen_name in common_in_pro_and_screen_names:
                self.screen_names.remove(screen_name) # now the screen_names has removed the duplicates from the pro and anti trump bios to have it left with still nuetral polarity

            # assigning polarity to the screen names that bios state something about pro or anti trump or neutral
            for screen_name in pro_trump_no_duplicates_bio:
                bio_anlysis_with_screen_name[screen_name]=[.7] # making the polarity a list data type because I will be adding to this list as more twitter information is gathered and then summing the poliarties at the end for a final correlation coeffient

            # assigning polarity to the screen names that bios state something about pro or anti trump or neutral
            for screen_name in anti_trump_no_duplicates_bio:
                bio_anlysis_with_screen_name[screen_name]=[-.7]

            # assigning polarity to the screen names that bios state something about pro or anti trump or neutral
            for screen_name in self.screen_names:
                bio_anlysis_with_screen_name[screen_name]=[0]
        return(bio_anlysis_with_screen_name)
