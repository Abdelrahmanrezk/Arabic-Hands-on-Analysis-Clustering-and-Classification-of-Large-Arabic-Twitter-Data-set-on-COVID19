# unCheck comment for any to_csv, or pickle  function comments if you need to run and save the function


# Usage libraries

from sklearn.feature_extraction.text import TfidfVectorizer
import pickle



def tfidf_vectorizer_for_supervised_models(X):
    '''
    The function used for features extraction from the text.
    Argumen:
        X: This is a list of tweets from the whole directory files.
    return:
        tfidf_vectorizer: The vectorized model that fit on the dataset to transform, training and test tweets
    '''

    tfidf_vectorizer = TfidfVectorizer(ngram_range=(1,2), max_features=50000)
    tfidf_vectorizer = tfidf_vectorizer.fit(X) 
    word_idf_weights = tfidf_vectorizer.idf_
    print("Our 10 words weights\n\n",word_idf_weights[:10])

    # pickle.dump(tfidf_vectorizer, open("models_weights/tf_idf/tf_idf_vectorizer_50000_fetures.pickle", "wb"))

    return tfidf_vectorizer

def load_tfidf_vectorizer_for_supervised_models(file_path):
    '''
    Load the fitted tf-idf file.
    Argument:
        file_path: The file contain the model weights.
    '''
    tfidf_vectorizer = pickle.load(open(file_path, "rb"))
    return tfidf_vectorizer
    














