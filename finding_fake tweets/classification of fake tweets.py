# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 21:14:15 2017

@author: akank
"""

from nltk.metrics.distance import edit_distance
import csv

#  transposition flag allows transpositions edits (e.g., “ab” -> “ba”),

# =============================================================================
Tweets = ["Happy Diwali 2017 #Diwali",
          "No one is born hating another person because of the color of his skin or his background or his religion....",
          "My warmest condolences and sympathies to the victims and families of the terrible Las Vegas shooting",
          "Kylie Jenner Has Reportedly Spent 70000 on Baby Clothes and Accessories",
          "When life hands you rain change your sport from soccer to swimming."
          ]
 

 #=============================================================================
SpamTweets = ["BREAKING: FBI says Las Vegas shooter had no connection to international terrorist group.",
             "I'm gonna go out on a limb and say las Vegas shooting was a botched false flag operation. None of it makes sense to me or anybody I know.",
            "Cause the Las Vegas shooting is being covered up!" ,
              "Between the Russia / Clinton Foundation revelations and lack of motive in the Las Vegas shooting I've determined something is seriously off!",
              "Tbh they completely swept the Las Vegas shooting under the rug like nothing",
              "Camera's are everywhere yet still no answers on shooting. Sec.",
              "Did you hear that? That’s the sound of people forgetting about the Las Vegas shooting and main stream media and government winning.",
              "Weeks after the Las Vegas shooting and we still know very little, besides the fact that the story of what happened keeps changing.",
              "Las Vegas shooting narrative is crumbling down",
              "Reminder: More people died in the Las Vegas shooting than in UK terror attacks this decade.",
             "I questioned the #LasVegas shooting narrative.",
              "I questioned the #LasVegas shooting narrative. #lasVegasshooting",
              "I questioned the #LasVegas shooting narrative. #peaceneeded",
              "I questioned the #LasVegas shooting narrative.#trumpeffect",
              "I questioned the #LasVegas shooting narrative. #peoplescared",
              "I questioned the #LasVegas shooting narrative. #immigrantsunsafe",
              "I questioned the #LasVegas shooting narrative. #Americaindanger",
              "I questioned the #LasVegas shooting narrative. #terrorsponsored",
             "@trump I questioned the #LasVegas shooting narrative.",
              " @fbi I questioned the #LasVegas shooting narrative."
             ]


rows = []
csvfile = open('TweetData_comparison.csv', 'w')
fieldnames = ['NormalTweet','SpamTweet','EditDistance']
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()
for tweet in Tweets:
    for spamTweet in SpamTweets:
        print('Tweet' + (str(Tweets.index(tweet) + 1)) + '->' 
              + 'SpamTweet' + (str(SpamTweets.index(spamTweet) + 1)) + 
              ' = ' + str(edit_distance(tweet, spamTweet)))
        
        writer.writerow({'NormalTweet':'Tweet' + (str(Tweets.index(tweet) + 1)), 
               'SpamTweet':'SpamTweet' + (str(SpamTweets.index(spamTweet) + 1)),
               'EditDistance': str(edit_distance(tweet, spamTweet))})
       
csvfile.close()