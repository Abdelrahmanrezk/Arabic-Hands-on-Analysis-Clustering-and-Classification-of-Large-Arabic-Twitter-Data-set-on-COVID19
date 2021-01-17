# unCheck comment for any to_csv, or pickle  function comments if you need to run and save the function

# Usage libraries
from tashaphyne.stemming import ArabicLightStemmer
from nltk.tokenize import word_tokenize
from nltk.stem.isri import ISRIStemmer
from textblob import TextBlob
import pandas as pd
import string
import re

# Main developed files
from direction_and_file_handleing import *
from cleaning import *
from configs import *







def convert_list_of_strings_to_list_of_words(text):
    '''
    A function used to convert list of strings to be list of all words of these strings like:
    ['تليفون جيد',
 'ايباد ميني فور من افضل الايبادات في السوق وسعره كان مغري',]
    return:
        list of all words in all string like:
        ['تليفون', 'جيد'] and so on
    '''
    word_list = []
    for i in text:
        i = i.split()
        word_list.extend(i)
    return word_list




def one_list_all_words(text_list):
    '''
    Argument:
        list of lists each of them are words
    return:
        one list contain all words
    '''
    updated_list = []
    [updated_list.extend(li) for li in text_list]
    return updated_list





def one_string_lower_conversation(sentence):
    '''
    Argument:
        text as string of words
    return:
        lower of this string
    '''
    return sentence.lower()
        




def all_string_lower_conversation(text_list):
    '''
    Argument:
        list of strings and each of these strings does contain some of words
    return:
        lower each string in this list
    '''
    text_list = [one_string_lower_conversation(sentence) for sentence in text_list]
    return text_list





def one_string_remove_diacritics(sentence):
    noise = re.compile(""" ّ    | # Tashdid
                             َ    | # Fatha
                             ً    | # Tanwin Fath
                             ُ    | # Damma
                             ٌ    | # Tanwin Damm
                             ِ    | # Kasra
                             ٍ    | # Tanwin Kasr
                             ْ    | # Sukun
                             ـ     # Tatwil/Kashida
                         """, re.VERBOSE)
    sentence = re.sub(noise, '', sentence)
    return sentence





def all_string_remove_diacritics(text_list):
    '''
    Argument:
        list of strings
    return:
        list of string without special chars from Arabic language
    '''
    text_list = [one_string_remove_diacritics(sentence) for sentence in text_list]
    return text_list





def one_string_remove_punctuation(sentence):
    '''
    Argument:
        string of words
    reutrn:
        string without punctuation like [.!?] and others
    '''
    sentence = re.sub('[@]\w+', '', sentence)
    sentence = re.sub(r'((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', '', sentence)
    sentence = sentence.split(' ')
    strs     = ''
    punctuations = string.punctuation
    for word in sentence:
#         word = re.sub(r'(.)\1+', r'\1', word) # remove repated chars
        word = re.sub('[^\w\s+]',' ',word)
        if len(word) > 1 and not (word[0] >= 'a' and word[0] < 'z' or word[0] >= 'A' and word[0] < 'Z'):
            strs += word + ' '
    translator = str.maketrans('', '', punctuations)
    strs.translate(translator)
    return strs




def all_strings_remove_punctuation(text_list):
    '''
    Argument:
        list of strings 
    reutrn:
        list of strings without punctuation like [.!?] and others
    '''
    text_list = [one_string_remove_punctuation(sentence) for sentence in text_list]
    return text_list






def one_string_normalize_arabic(sentence):
    '''
    Argument:
        string of words
    return:
        string of words but standardize the words
    '''
    sentence = re.sub("[إأآا]", "ا", sentence)
    sentence = re.sub("ى", "ي", sentence)
    sentence = re.sub("ؤ", "ء", sentence)
    sentence = re.sub("ئ", "ء", sentence)
    sentence = re.sub("ة", "ه", sentence)
    sentence = re.sub("گ", "ك", sentence)
    return sentence




def all_string_normalize_arabic(text_list):
    '''
    Argument:
        list of strings
    return:
        list of strings but replace some of chars  like ة to ه Arabic words
    '''
    text_list = [one_string_normalize_arabic(sentence) for sentence in text_list]
    return text_list





def one_string_tokenization(sentence):
    '''
    Argument:
        String of words
    return:
        list of words
    '''
    sentence = word_tokenize(sentence)
    return sentence




def all_string_tokenization(text_list):
    '''
    Argument:
        list of Strings
    return:
        list of strings and every string is list of words
    '''
    text_list = [one_string_tokenization(sentence) for sentence in text_list]
    return text_list







def one_string_un_tokenization(sentence):
    '''
    Argument:
        list of words
    return:
        string of words
    '''
    sentence = " ".join(sentence)
    return sentence
    




def all_string_un_tokenization(text_list):
    '''
    Argument:
        list of words
    return:
        string of words
    '''
    text_list = [one_string_un_tokenization(sentence) for sentence in text_list]
    return text_list
    





def one_string_spelling_correction(sentence):
    '''
    Argument:
        string of words
    return:
        string of correct words
    '''
    
    sentence = str(TextBlob(sentence).correct())
    return sentence




def all_string_spelling_correction(text_list):
    '''
    Argument:
        list of strings each of them are some of words
    return:
        list of correct strings
    '''
    text_list = [one_string_spelling_correction(sentence) for sentence in text_list]
    return text_list





def one_string_steming(sentence):
    '''
    Argument:
        String of words
    return:
        list of words with steming which the root of the word
    '''
    sentence = one_string_tokenization(sentence)
    stemmer  = ISRIStemmer()
    sentence = [stemmer.stem(word) for word in sentence]
    return sentence




def all_string_steming(text_list):
    '''
    Argument:
        list of strings
    return:
        list of strings with steming which the root of the word in each string
    '''
    text_list = [one_string_steming(sentence) for sentence in text_list]
    return text_list






def one_string_Lemmatizing(sentence, language):
    '''
    Argument:
        String of words
    return:
        list of words with Lemmatizing
    '''
    sentence = one_string_tokenization(sentence)
    stemmer  = ArabicLightStemmer()
    sentence = [stemmer.light_stem(word) for word in sentence]
    return sentence




def all_string_Lemmatizing(text_list):
    '''
    Argument:
        list of strings
    return:
        list of strings with steming which the root of the word in each string
    '''
    text_list = [one_string_Lemmatizing(sentence) for sentence in text_list]
    return text_list








def convert_file_of_stop_words_to_list(file_dir):
    '''
    Argument:
        file with stop words
    return:
        list of these stop words
    '''
    
    stop_words_designed = []
    with open(file_dir, 'r') as file:
        file                = file.readlines()
        file                = "".join(file)
        file                = re.sub('[\[\]\'\",]', '', file)
        stop_words_designed = file.split()
    return stop_words_designed
    

def one_string_stop_words(sentence):
    '''
    Argument:
        string of words
    return:
        remove stop words from this string like this, did
        but other words like not, no dont remove
    '''

    file_dir1                   =  '../stop_words/nltk_stop_words_handle.txt'
    file_di2                    = '../stop_words/stop_list1.txt'
    file_di3                    ='../stop_words/updated_stop_words.txt'

    stop_words_designed         = []
    stop_words_designed.extend(convert_file_of_stop_words_to_list(file_di2))

    stop_words_designed         = set(stop_words_designed)
    stop_words_designed         = list(stop_words_designed)
    arabic_stop_words_designed  = convert_file_of_stop_words_to_list(file_di3)

    stop_words                  = arabic_stop_words_designed 
    sentence                    = sentence.split(' ')
    updated_sentence            = ''
    for word in sentence:
        if word not in stop_words:
            updated_sentence   += word + ' '
    return updated_sentence
            




def all_string_stop_words(text_list):
    '''
    Argument:
        list of string
    return:
        list of string without stop words
    '''        
    text_list = [one_string_stop_words(sentence) for sentence in text_list]
    return text_list




def arabic_pip_line(text_list):
    text_list = all_string_remove_diacritics(text_list)
    text_list = all_strings_remove_punctuation(text_list)
    text_list = all_string_normalize_arabic(text_list)
    text_list = all_string_stop_words(text_list)

    return text_list


