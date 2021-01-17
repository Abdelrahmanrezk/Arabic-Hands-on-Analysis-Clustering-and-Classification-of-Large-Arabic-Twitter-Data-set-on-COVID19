# unCheck comment for any to_csv, or pickle  function comments if you need to run and save the function

# coding: utf-8

# In[1]:


# # !pip install twarc
# from twarc import Twarc
# import pandas as pd
# import  json
# import csv
# import os
# import multiprocessing
# import pymongo
# from configs import *


# In[2]:


# !git clone https://github.com/SarahAlqurashi/COVID-19-Arabic-Tweets-Dataset


# In[3]:


# T = Twarc(consumer_key, consumer_secret, access_token, access_token_secret)


# In[4]:


# def one_file_tweets(Inputfile):
#     '''Get all tweets text in one file'''
#     ids = []
# #     df = pd.read_csv(Inputfile,lineterminator='\n', error_bad_lines=False, encoding='utf-8')
    
#     with open(Inputfile, "r", encoding='utf-8') as ids_file: #open the input file
#         try:
#             ids=ids_file.read().split() #read and store the ids
# #             print("#"*50)
# #             print("ids le/n: ", len(ids))
#             tweets_text = []
#             print("=-=========")
#             for tweet in T.hydrate(iter(ids)):
#                 print(tweet)
#                 break
#                 tweets_text.append(tweet['full_text'])
                
#             if len(tweets_text) != len(ids):
#                 indx=len(tweets_text) 
#                 for tweet in T.hydrate(iter(ids[indx:])):
#                     tweets_text.append(tweet['full_text'])
#             dict_col = {'full_text': tweets_text}
#             df_file = pd.DataFrame(dict_col)
#             df_file.to_csv('csv_down_files/'+ Inputfile +'.csv', index=False)
#         except Exception as e:
#             file = open("logs/tweets_api_file.log","+a")
#             file.write("This error related to function one_file_tweets of tweets_api file\n" 
#                + str(e) + "\n" + "#" *99 + "\n") # "#" *99 as separated lines
#     return len(ids)


# In[5]:


# def read_direction(direction_path):
#     '''Loop over each direction and path each file in this direction to get all tweets'''
#     tot = 0
#     all_path_files = os.listdir(direction_path)
#     for file_path in all_path_files:
#         file_path = direction_path + file_path
#         ids = one_file_tweets(file_path)
#         tot+=(ids)
#     return tot

