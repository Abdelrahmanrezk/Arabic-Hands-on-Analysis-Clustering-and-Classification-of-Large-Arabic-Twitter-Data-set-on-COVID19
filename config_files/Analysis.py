# unCheck comment for any to_csv, or pickle  function comments if you need to run and save the function

# Usage libraries
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import os
import re

# Main developed files
from direction_and_file_handleing import *
from configs import *



def words_frequency(list_of_all_words):
    '''
    The function used to get all the frequency of each word.
    Argument:
       list_of_all_words: The whole words of all files strings in one direction
   Return
       data_frame: the dataframe which have two column of all words and frequency of each word
    '''
    vect            = CountVectorizer().fit(list_of_all_words)
    # get the words it self
    dict_words      = list(vect.vocabulary_.keys())
    # get the words frequency
    dict_frequency  = list(vect.vocabulary_.values())
    print("Sample of first 10 top words: ", dict_words[:10])
    print("Sample of first 10 top words frequency: ", dict_frequency[:10])
    
    # create a dictionary that maps each word to its frequency
    words_frequency = {'frequency': dict_frequency, 'words': dict_words}
    # create a data frame with 2 columns from the dictionary
    data_frame      = pd.DataFrame(data=words_frequency)
    return data_frame



def drop_rows(df):
    '''
    Drop all row that not contain on Arabic words
    Argument:
        df: pandas dataframe that have some columns ans rows
    Return:
        Return the same data frame but cleaned from cell that contains anything except Arabic words
    '''
    # drop rows contain numbers
    drop_rows = df[df['words'].str.isdigit()].index
    df.drop(drop_rows, inplace=True)
    
    # drop rows contain Chinese and English words
    drop_rows = df[df['words'].str.contains('[a-zA-z0-9⺀-⺙⺛-⻳⼀-⿕々〇〡-〩〸-〺〻㐀-䶵一-鿃豈-鶴侮-頻並-龎]',  
                                  regex=True)].index
    df.drop(drop_rows, inplace=True)
    
    return df




def analysis_pipline(direction, save_csv_path):
    '''
    The pipline to make all of our work in one direction
    Argument:
        direction: Which direction you need to make an analysis on.
        save_csv_path: After the analysis dave the result in csv file.
    Return
        True once it save the file that cotain the dataframe we reutrned
    '''
    try:
        list_of_all_words_direction = read_direction_analysis(direction)
        print("==========")
        print("The total words are: ", len(list_of_all_words_direction))
        print("==========")
        data_frame                  = words_frequency(list_of_all_words_direction)
        print("The total Unique words now are: ", len(data_frame))
        
        data_frame                  =  drop_rows(data_frame)
        print("After drop Chinese and English words: ",len(data_frame))
        
#         data_frame.to_csv(save_csv_path + 'words_frequency.csv', index=False)
        print("#" * 70)
    except Exception as e:
        file = open("../logs/Analysis_file.log","+a")
        file.write("This error related to function analysis_pipline of Analysis_file in direction config_files n" 
                   + str(e) + "\n" + "#" *99 + "\n") # "#" *99 as separated lines
    return data_frame




def count_tweets_file(direction_path, save_csv_path):
    '''
    The fcuntion used to get what is the number of tweets per day
    Argument:
    Direction_path: which direction you need to deal with.
    save_csv_path: After we get the count of tweets of each file day,
        we have save one file represent this direction.
    
    '''
    all_path_files  = os.listdir(direction_path)
    counts_tweets   = []
    file_day        = []
    for file_path in all_path_files:
        file_path   = direction_path + file_path
        day         = re.findall('([0-9]+.csv)', file_path)
        day         = day[0].split('.')[0]
        df          = pd.read_csv(file_path, lineterminator='\n', error_bad_lines=False, encoding='utf-8')
        file_day.append(day)
        counts_tweets.append(len(df))
    dicts           = {'file_day': file_day, 'counts_tweets': counts_tweets}
    df              = pd.DataFrame(data=dicts)
    df              = df.sort_values(by=['file_day'])
#     save_csv_path = save_csv_path +'tweets_per_day.csv'
#     df.to_csv(save_csv_path, index=False)
    return df

