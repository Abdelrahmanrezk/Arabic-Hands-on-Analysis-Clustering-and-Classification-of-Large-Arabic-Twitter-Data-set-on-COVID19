# unCheck comment for any to_csv, or pickle  function comments if you need to run and save the function

# Usage libraries
import pandas as pd

# Features Extraction word2vec
from gensim.models import Word2Vec

# Main developed files
from direction_and_file_handleing import *
from configs import *



# Main word2vec parameters
number_of_features = 300
window_size = 5
min_words_count = 500



def dir_max_all_tweets(preprocessed_direction_path_tweets):
    '''
    The function used to get the tweet that contains maximum words, which help us building the Word2vec Matrix
    Argument:
        preprocessed_direction_path_tweets: The directory path
    '''
    all_tweets_of_direction = read_direction_analysis(preprocessed_direction_path_tweets, "")
    print("The number of tweets in our direction is: ", len(all_tweets_of_direction))

    # The maximum tweet contains words
    max_len_str = max([len(i.split()) for i in all_tweets_of_direction])
    print("The greatest string of our reviews: ", max_len_str)

    # Retrieve each tweet as a list of words that contain 
    all_tweets_of_direction = [i.split() for i in all_tweets_of_direction] # split each review to list of words
    print("The firt 5 tweets are: ", all_tweets_of_direction[:5])
    return all_tweets_of_direction, max_len_str






def word_to_vec(text_list, number_of_features, window_size, min_words_count):
    '''
    The function used to build our word2vec vocabs, then save these files to be loaded for next time we need.
    Argument:
        text_list: list of strings and each string is list of words.
        number_of_features: The number of features you need for each word.
        window_size = take the context of neighbour words.
        min_words_count = 1 consider each word that even repeated 1 time.
    return:
        the word2vec model
    '''
    word_to_vec_model = Word2Vec(text_list, size =number_of_features, window = window_size, min_count=min_words_count, sg = 1) 
    print("Our word2vec model: ", word_to_vec_model)
    print("The number of frequent words of our data: ", len(word_to_vec_model.wv.vocab)) # the frequent words
    # save model
    # word_to_vec_model.save('../ml_models/models_weights/word2vec/' + model_bin_saved)

    
    return word_to_vec_model

def load_word_to_vec(model_file):
    """The function used only to load the word2vec model"""

    word_to_vec_model = Word2Vec.load('../ml_models/models_weights/word2vec/'+ model_file)
    return word_to_vec_model



def save_words(saved_path, model_file_path):
    '''
    The function used to save words that we used in Tableau to graph the most appeared words.
    Argument:
        saved_path: After getting the most repeated words in which direction need to be saved.
        model_file_path: The word2vec file that contains the learned vocabs
    '''
    word_to_vec_model = load_word_to_vec(model_file_path)
    w2c = dict()
    for item in word_to_vec_model.wv.vocab:
        if not item.isdigit() and len(item) > 2 and not "_" in item and not (item[0] >= 'a' and item[0] <= 'z'):
            w2c[item]   =   word_to_vec_model.wv.vocab[item].count
    dicts = {'word2vec_model_words': list(w2c.values()), 'word2vec_model_frequency': list(w2c.keys())}
    df = pd.DataFrame(dicts)
    saved_path = saved_path + 'csv/word2vec_model_words.csv'
    df.to_csv(saved_path, index=False)
    return True

