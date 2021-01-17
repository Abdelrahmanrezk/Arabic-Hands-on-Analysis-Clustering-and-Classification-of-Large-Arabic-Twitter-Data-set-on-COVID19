# unCheck comment for any to_csv function comments if you need to run and save the function

# Usage libraries
import os
import re
import random
import pandas as pd

# Main developed files
from configs import *


pd.options.mode.chained_assignment = None  # default='warn'



def separate_number_of_tweet_each_file(direction_read, direction_save, number_of_tweets):
    '''
    Loop over  direction and path each file in this direction to get 100 tweets.
    Argument:
        direction_read: Which direction we will read files from.
        direction_save: After shuffle process and get first number_of_tweets 
        from each file save all these tweets, in one file which will be classifed later for our model.
    Return:
        True and before of that save the total tweets we get from each file as sample in one file.
    '''
    try:
        all_path_files      = os.listdir(direction_read)
        list_3000_tweet     = []
        for file_path in all_path_files:
            file_path       = direction_read + file_path
            df_file         = pd.read_csv(file_path, error_bad_lines=False, encoding='utf-8')
            df_file         = df_file.sample(frac=1).reset_index(drop=True)
            list_3000_tweet +=(list(df_file['full_text'][:number_of_tweets]))
            dict_300_tweets = {'sample_3000_tweets': list_3000_tweet}
            data_frame      = pd.DataFrame(dict_300_tweets)
            # data_frame.to_csv(direction_save + 'csv/3000_tweet_not_classified.csv', index=False)
            # data_frame.to_excel(direction_save + 'excel/3000_tweet_not_classified.xlsx', index=False)
    except Exception as e:
        file                = open("../logs/3000_tweet_file.log","+a")
        file.write("This error related to function separate_100_tweet_each_file of 3000_tweet file n"
                   + str(e) + "\n" + "#" *99 + "\n") # "#" *99 as separated lines
    return True



def get_random_number_of_tweets(direction_read, direction_save, number_of_tweets):
    """
    Function to read all tweets of all files in one direction into one list, 
    then take random tweets from this list, also for each tweet make some regular expression,
    like replace \n with just space to make the whole tweets in one line,
    then save the result in CSV and  XLS file.
    Arguemtn:
        direction_read: Which direction you will read files from.
        direction_save: After you take the random tweets and make a data frame of it which direction you need to save.
        number_of_tweets: which number of tweets at all you need.
    Return:
        True if the process success other send the error to log file.
    """
    try:
        all_path_files          = os.listdir(direction_read)
        all_files_tweets        = []
        for file_path in all_path_files:
            file_path           = direction_read + file_path
            df_file             = pd.read_csv(file_path, lineterminator='\n', error_bad_lines=False, encoding='utf-8')
            df_file.drop_duplicates(inplace = True)
            df_file.reset_index(inplace=True, drop=True)
            all_files_tweets    += list(df_file['full_text'])

        dicts_df                = {"tweet_text": all_files_tweets}
        df_file                 = pd.DataFrame(dicts_df)
        df_file.drop_duplicates(inplace = True)
        df_file.reset_index(drop=True, inplace=True)
        all_files_tweets        = list(df_file['tweet_text'])

        random_indexes          = random.sample(range(len(all_files_tweets)), number_of_tweets)
        all_files_tweets        = [all_files_tweets[tweet_index] for tweet_index in random_indexes]
        all_files_tweets_last   = []

        for tweet in all_files_tweets:
            tweet               = re.sub("(\\n)+", " ", tweet)
#             tweet = tweet.replace("  ", "")
            tweet               = tweet.strip()
            all_files_tweets_last.append(tweet)

        tweet_text              = {'class': 0, 'tweet_text': all_files_tweets_last}
        data_frame              = pd.DataFrame(tweet_text)
        # data_frame.to_csv(direction_save + 'csv/tweet_not_classified_2000_26_12.csv', index=False)
        # data_frame.to_excel(direction_save + 'excel/tweet_not_classified_1050_28_12.xlsx', index=False)

    except Exception as e:
        file = open("../logs/get_tweet_to_classify.log","+a")
        file.write("This error related to function get_random_number_of_tweets of get_tweet_to_classify file in direction config_files n"
                   + str(e) + "\n" + "#" *99 + "\n") # "#" *99 as separated lines
    return data_frame
