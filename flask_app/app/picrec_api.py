import os
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

##*Dec8 pickle a new notebook with loading data and cos sim, then use on uploaded image within dataset in api!
##* alt: pickle/keras.save CNN also, so can actually extract features from new uploaded image, then do cos sim (properly)


#with open("../bbc_ft_id.csv", "rb") as f: 
#   features = pickle.load(f) #might not need pickle, upload file instead?


#move cos sim code to api to get rec results:
bbc_ft = pd.read_csv('static/data/Features.csv')

#*need to get index from img title or url first!
def cos_sim_vs_all(img_idx, datasetft, num):
    '''Find the pairwise cosine similarity between features of the chosen image and all the images in the dataset
    Takes in index of image and a dataset of image features previously extracted from CNN
    Returns a sorted array of the top number (num) of most similar images by index, from most similar (except for itself) to least similar'''
    sim_list = []
    imageft = bbc_ft.iloc[img_idx].values.reshape(1, -1)
    for i in range(len(datasetft)):
        cos_sim = cosine_similarity(imageft, datasetft.iloc[i].values.reshape(1,-1)) 
        sim_list.append(cos_sim)
        sim_array = np.array(sim_list).argsort(axis=None)
        #flip to sort from largest cos sim values (most similar) to smallest
        sim_sorted = np.flipud(sim_array)[1:num+1]
    return sim_sorted
#prev getting diff results from bbf_ft_id -- back to Features.csv, worked
#execution slow

#test similar recipes for turkey -- need to replace this index with user input on app!*
turkey_sorted = cos_sim_vs_all(1412, bbc_ft, 11)


##---
bbc_path='/Users/xinrucheng/Documents/Metis_bootcamp/week_9/project5data/2017_140k/recipe_photos/bbc_photos/pages-photos/'
#better way to do this?

#bbclist = !ls doesn't work outside of jupyter, for loop?
def get_names_list(directory):
    '''stores all image names in directory into a list'''
    names_lst = []
    for entry in os.scandir(directory): #loop through files in directory, path is file path of folder containing images
        if entry.path.endswith(".jpg"):
        #if entry.path == directory + '/.DS_Store':
        #    continue  #avoid reading mac os's .DS_Store as an image
        #else:
            names_lst.append(entry.path) #"name" is entire path; if append entry: <DirEntry 'zesty_tofu_cheesecake_84103_16x9.jpg'> (type?)
    return names_lst

bbc_list = get_names_list(bbc_path)
#print(bbc_list)  

#if need to return text predictions separately from image
def print_similar_names(sorted_array):
    similar_list = []
    for idx in sorted_array:
        similar_list.append(bbc_list[idx])
        #print(bbc_list[idx])
    return similar_list
print_similar_names(turkey_sorted) 
#clean up path to display name only? use regex?

# def print_similar_imgs(sorted_array, num):        
#     for idx in sorted_array[:num]:
#         print(bbc_list[idx])
#         img=mpimg.imread(bbc_list[idx]) 
#         #imgplot = plt.imshow(img) #unused var?
#         plt.show(img) #change and save img/display on webpage?
# print_similar_imgs(turkey_sorted,5) 



# This section checks that the prediction code runs properly
# To run, type "python predictor_api.py" in the terminal. 

#if __name__ == '__main__':
#     from pprint import pprint
#     print("Checking to see what setting all params to 0 predicts")
#     features = {f: '0' for f in feature_names}
#     print('Features are')
#     pprint(features)

#     x_input, probs = make_prediction(features)
#     print(f'Input values: {x_input}')
#     print('Output probabilities')
#     pprint(probs)
