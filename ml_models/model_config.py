# Directions handling
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir + '/config_files')

import matplotlib.pyplot as plt
import numpy as np

# Static method for shuffle data
from sklearn.model_selection import StratifiedShuffleSplit

# Models
from sklearn.model_selection import GridSearchCV

# Evaluation
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score

# Main developed files
from direction_and_file_handleing import *
from features_engineering import *
from cleaning import *
from configs import *


def shuffle_split(df_file):
	'''
	Instead of random shuffle, we used the StratifiedShuffleSplit object, 
	to distribute the shuffle depends on the class attribute,
	which helps to get an approximate number of instances(rows of data) per class.

	Argument:
		df_file: 		The dataframe which contain the whole dataset we have.
	Return:
		df_file: 		which we have used
		start_train_set:The training set we will train the model on.
		start_test_set:	The test set will test the model once we decide to use this model.
	'''

	split = StratifiedShuffleSplit(n_splits=1, test_size=.2, random_state=42)
	

	for train_index, test_index in split.split(df_file, df_file['class']):

	    start_train_set 		= df_file.loc[train_index]
	    start_test_set 			= df_file.loc[test_index]

    # Class 1 Vs Class 0 in test set
	train_0_1 					= start_train_set['class'].value_counts() / len(start_train_set)

	# Class 1 Vs Class 0 in train set
	test_0_1					= start_test_set['class'].value_counts() / len(start_test_set)

	print("percentage of class 0 to 1 in the train set", train_0_1)

	print("percentage of class 0 to 1 in the test set", test_0_1)



	start_train_set['class'] 	= start_train_set['class'].fillna(0).astype(int)
	start_train_set['class'].astype(int)


	start_test_set['class'] 	= start_test_set['class'].fillna(0).astype(int)
	start_test_set['class'].astype(int)

	start_train_set 			= start_train_set.reset_index(drop=True)

	start_test_set 				= start_test_set.reset_index(drop=True)
	return df_file, start_train_set, start_test_set

def split_train_test_set(start_train_set, start_test_set):
	'''
	The method used to separate the target variable from the features(attributes) of training and test set.
	Argument:
		start_train_set:The training set we will train the model on.
		start_test_set: The test set will test the model once we decide to use this model.
	Return:
		tweets_train: 	The training attributes we will fit the model on.
		target_train: 	The training target we will fit the model on with tweets_train to learn from.
		tweets_test:  	The training attributes we will predict how the model work on.
		target_test:  	After radiation check the percentage where the predicted classes are as the actual target class or not.
	'''
	tweets_train 				= start_train_set['tweet_text']
	tweets_test 				= start_test_set['tweet_text']

	target_train 				= start_train_set['class']
	target_test 				= start_test_set['class']

	print("Number of Training Tweets is: ", len(tweets_train))
	print("Number of Tagets class in Training Tweets is: ", len(target_train))

	print("Number of Testing Tweets is: ", len(tweets_test))
	print("Number of Tagets class in Testing Tweets is: ", len(target_test))

	return tweets_train, target_train, tweets_test, target_test

def pie_graph(df_file):
	'''
	The function used just to help get insights into what number of class 1 and class 0 in the pie graph.
	'''
	# Separate classes 
	corona_tweets 				= len(df_file[df_file['class'] == 1])
	genral_tweets 				= len(df_file[df_file['class'] == 0])
	histogram 					= [0, 1]

	labels 						= 'Class 1 coronavirus', 'Class 0 genral'
	sizes 						= [corona_tweets, genral_tweets]
	explode 					= (0, 0.1)  
	fig1, ax1 					= plt.subplots()
	ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
	plt.show()

	return True


def grid_search(model, param_grid, X_train, y_train):
	'''
	Each model has a lot of different parameters and hyperparameters associated with it,
	and to check this manually is consumed out of time and a lot of combination would we have think of,
	so grid search object from Scikit Learn to help us of doing that, just we pass the model 
	and the parameters he used then this makes all the combination for us.

	Argument:
		model: 		The model we will use with the Grid search.
		param_grid: All parameters that you need to try with the model.
		X_train: 	The traiing attributes will run on.
		y_train: 	The target associated with each instances of the training attributes.
	'''
    search_model 				= GridSearchCV(model, param_grid, cv = 5)
    search_model.fit(X_train, y_train)
    return search_model

def model_predict_train__test_data(model, X_train, y_train, X_test, y_test):
	
	predict 					= model.predict(X_train)
	print("===================== Training Result =====================")
	print("F1 score of our training data is: ", f1_score(y_train, predict, average='micro'))
	print("Evalution Matrix of training data is \n", confusion_matrix(y_train, predict))

	predict 					= model.predict(X_test)
	print("===================== Testing Result =====================")
	print("F1 score of our Testing data is: ", f1_score(y_test, predict, average='micro'))
	print("Evalution Matrix of Testing data is \n", confusion_matrix(y_test, predict))

	return True


def check_search_params(search_model):
	'''
	The function used to get all results that the grid search doing 
	along with each fold of the cross-validation.
	Argument:
		search_model: The grid search model that we used above in the grid_search method.
	'''
	cures 						= search_model.cv_results_
	for mean_score, params in zip(cures['mean_test_score'], cures['params']):
		print(mean_score, params)
	return True

def word_2_vec_matrix(text_list,word_to_vec_model,number_of_features, max_len_str):
    '''
    The function used to build our word2vec matrix for the training and testing data.
    Argument:
            List of string each of them is list of words
            the word_to_vec_model model
            number of features you apply to word2vec model
            number of words of greatest string in your reviews
    return:
        embedding matrix that can apply to machine learning algorithms
    '''
    embedding_matrix 			= np.zeros((len(text_list), number_of_features*max_len_str)) # largest sentence and 5 fetures
    print("The shape of matrix", embedding_matrix.shape)
#loop over each review
    for index,review in enumerate(text_list):
# list of each reviw which will be appended to embedding matrix
        one_sentence_list 		= [] 
        for word in review:
            word 				= word_to_vec_model[word]
            one_sentence_list.extend(word)
            
# make padding for small strings
        zero_pad 				= np.zeros(number_of_features*max_len_str-len(one_sentence_list))
        zero_pad 				= list(zero_pad)
    
# apply the padding
        one_sentence_list.extend(zero_pad)
        embedding_matrix[index] = one_sentence_list
    return embedding_matrix