#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 14:09:28 2020

@author: matthewreisdorf
"""

#Python Reddit API Wrapper
import praw

#Translate API (Not really Google Affiliated)
from google_trans_new import google_translator



#Translator Object
translator = google_translator()



#Reddit Access for Bot
r_access = praw.Reddit(user_agent = "Test Bot",
                  client_id = "7CW6Ub5SgU1KQg",
                  client_secret = 	"gNXdNihNF4i-yj54HOm5AKb3bg9I7A",
                  username = "MReisdorf_Bot",
                  password = "img0462jpg")




#Define Subreddit (Default to r/France, can be used for any non-English sub)
sub = r_access.subreddit("France")


for submission in sub.top("hour" , limit=3):
    
    #Post Title Translation (Gives original and English Translation)
    title = str(submission.title)
    print(title)
    print(translator.translate(title))
    print("\n")
    
    