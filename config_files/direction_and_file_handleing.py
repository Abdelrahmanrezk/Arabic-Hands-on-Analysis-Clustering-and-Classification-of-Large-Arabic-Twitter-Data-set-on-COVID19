# unCheck comment for any to_csv, or pickle  function comments if you need to run and save the function

# Usage libraries
import pandas as pd
import os
import re

# Main developed files
from configs import *
from cleaning import *


def one_file_preprocess(Inputfile):
    '''
    The function used to read CSV file and convert the read tweets from this file to list.
    After that the function path the list of tweets to the Cleaning Arabic pipeline.
    Argument:
        Inputfile: The file path that you need to read.
    Return:
        The tweets contained in this file as one list that contain all tweets.
    
    '''
    df_file                     = pd.read_csv(Inputfile,lineterminator='\n', error_bad_lines=False, encoding='utf-8')
    
    print(len(df_file))
    full_text_list              = list(df_file['full_text'])
    full_text_list_preprocessed = arabic_pip_line(full_text_list)
    return full_text_list_preprocessed




def read_direction_preprocess(direction_path):
    '''
    Loop over each direction and path each file in this direction to get all tweets,
    then to save the new preprocessed data which cleaned tweets we have make another dierction,
    to save the data in for each file create the same file name and save in another dierction.
    Argument:
        direction_path: The dierction you aimed to read files from.
    '''
    try:
        all_path_files                          = os.listdir(direction_path)
        for file_path in all_path_files:
            file_path                           = direction_path + file_path
            full_text_list_preprocessed         = one_file_preprocess(file_path)
            file_path                           = file_path.split('/')
            file_path[1]                        = 'preprocessed'
            file_path                           = '/'.join(file_path)
            dict_full_text_list_preprocessed    = {'full_text': full_text_list_preprocessed}
            dict_full_text_list_preprocessed    = pd.DataFrame(dict_full_text_list_preprocessed)
            file_path                           = file_path[:-7]
            file_path                           = file_path + 'csv'
            dict_full_text_list_preprocessed.to_csv(file_path, index=False)
    except Exception as e:
        file = open("../logs/direction_and_file_handleing_file.log","+a")
        file.write("This error related to function read_direction_preprocess of direction_and_file_handleing file in direction config_files n"
                   + str(e) + "\n" + "#" *99 + "\n") # "#" *99 as separated lines
    return True




def handle_direction_analysis(direction, replace_with):
    '''
    Use one default direction and replace this with others like below:
    "COVID-19-Arabic-Tweets-Dataset/COVID19-tweetID-2020-01/" - to
    "COVID-19-Arabic-Tweets-Dataset/COVID19-tweetID-2020-02/"
    Argument:
        direction: the folder path you need to change.
        replace_with: replace the folder name.
    reutrn:
        The new directions we need to work with
    '''
    direction = re.sub('([1-9]/)', replace_with , direction)
    return direction




def one_file_analysis(Inputfile):
    '''
    The function to get all rows in file in one list
    Argument:
        Inputfile: The file path we aimed to get all of its strings.
    Return:
        full_text_list: retrun these strings as a list each index represent one string.
    '''
    df_file         = pd.read_csv(Inputfile,  lineterminator='\n',  error_bad_lines=False, encoding='utf-8')
    full_text_list  = list(df_file['full_text'])
    return full_text_list




def read_direction_analysis(direction_path, convert_list = "to_list_of_words"):
    '''
    Loop over each direction and path each file in this direction, then get the tweets of one path as a list,
    then get all of the words of this list, and extend this list to contain all words in all files of one direction.
    Argument:
        direction_path: The dierction you aimed to read files from.
        convert_list: default argument used when it's required.
    Return:
        All the words in all files of one direction
    '''
    try:
        
        all_path_files          = os.listdir(direction_path)

        all_words_of_direction  = []
        word_list               = []
        for file_path in all_path_files:

            file_path           = direction_path + file_path
            full_text_list      = one_file_analysis(file_path)
            
            if convert_list == "to_list_of_words":
                full_text_list  = convert_list_of_strings_to_list_of_words(full_text_list)
            # extend the list of words of previous files to new words of another file
            all_words_of_direction.extend(full_text_list)

            
#             print("The total words now are: ", len(all_words_of_direction))
#     pull the error to logs direction
        
    except Exception as e:
        print("="*50)
        file = open("../logs/direction_and_file_handleing.log","+a")
        file.write("This error related to function read_direction_analysis of direction_and_file_handleing file in direction config_files n" 
                   + str(e) + "\n" + "#" *99 + "\n") # "#" *99 as separated lines
    return all_words_of_direction

