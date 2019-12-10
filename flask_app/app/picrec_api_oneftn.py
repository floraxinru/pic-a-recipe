#putting all of cos_sim into one function as api for picrec_app.py

import os
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import re

bbc_path='/Users/xinrucheng/Documents/Metis_bootcamp/week_9/project5data/2017_140k/recipe_photos/bbc_photos/pages-photos/'
bbc_ft = pd.read_csv('/Users/xinrucheng/Documents/Metis_bootcamp/week_9/metis_passion_project/data/processed/Features.csv')

#another ftn to clean URl to get ID? then import ftn from api into app.py

def ft_to_rec(img_idx):#input from user (html form) is dict
    '''Function that takes in an image index in dataset, 
    compares its cosine similarity with the rest of the images in dataset,
    generates a list of the top 5 recommendations and their images'''
    #next stage - need separate pkl file to extract image features before getting index?
    
    #find feature of selected image in previously extracted features.csv file
    sim_list = []
    index_key = int(img_idx.get('image_index', 1412)) #default 1412 is turkey image*
    #index_key = 1412
    imageft = bbc_ft.iloc[index_key].values.reshape(1, -1) #next: get index from url from user?
    #img_idx.get()--input?
    #imageft = bbc_ft.iloc[img_idx].values.reshape(1, -1)
   
    #*input of .get needs to match input name in html!
    #request.form['name']: use indexing if you know the key exists
    #request.form.get('name'): use get if the key might not exist
    
    #Find cosine similarity between selected image and the rest of the dataset, sort from highest to lowest similarity,
    #omit the image itself in the result
    for i in range(len(bbc_ft)):
        cos_sim = cosine_similarity(imageft, bbc_ft.iloc[i].values.reshape(1,-1)) 
        sim_list.append(cos_sim)
        sim_array = np.array(sim_list).argsort(axis=None)
        #flip to sort from largest cos sim values (most similar) to smallest
        sim_sorted = np.flipud(sim_array)[1:5+1] #num=5, hardcoded
    #return sim_sorted
    
    #Stores all image names in directory into a list - same as bbc_list = !ls... in jupyter - cmd line doesn't work in py?
    
    files = os.listdir(bbc_path) #equiv of !ls, easier than loop below
    img_list = [x for x in files if x.endswith('.jpg')]
    #print(img_list) #already showing relative path like 'roast_goose_with_apples_74479_16x9.jpg'

    #img_list = []
    # for entry in os.scandir(bbc_path): #loop through files in directory, path is file path of folder containing images
    #     if entry.path.endswith(".jpg"):
    #     #if entry.path == directory + '/.DS_Store':
    #     #    continue  #avoid reading mac os's .DS_Store as an image
    #     #else:
    #         img_list.append(entry.path) #this gets absolute file path
    # #return img_lst        
            
    import pprint
    path_list = []
    for idx in sim_sorted:
        path_list.append(img_list[idx])
        #print(bbc_list[idx])
    #pprint.pprint(path_list)

    #get list of recipe names from cleaned filepath, from text_processing, clean url
    recipe_list = [] 
    pic_list = []
    for filepath in path_list:
        #pic_list.append(filepath)
        pic_list.append(bbc_path+filepath)

        #recipename = re.sub(r'_',' ',str(filepath))
        recipename = re.findall(r"(\w+_)", str(filepath))
        recipename = re.sub(r'(_)',' ', str(recipename)) 
        recipe_list.append(recipename)
        #print(recipe_list) #how to clean up output further?
        #inconsistent, some image names don't have underscores!


    #Prints out top 5 most similar images
  
    #for filename in path_list:
        #img=mpimg.imread(bbc_path+filename) 
        #print(img) #array from imread, not filepath!!
        #imgplot = plt.imshow(img) #unused var? 

            #use diff ftn to show image - html
            #plt.show(img) #get truth value ambiguous error (even though no == in my ftn) with this line, without, prints last img
            #change and save img/display on webpage?
        #pic_list.append(img)
        #pic_list.append(imgplot)
        
    #return pic_list



    recs = [{'name': recipe_list}, {'pic': pic_list}]
    #loop? probs = [{'name': lr_model.target_names[index], 'prob': pred_probs[index]} #save prediction prob as list of dict
             #for index in np.argsort(pred_probs)[::-1]]
           

    
    return (index_key, recs)

 

# This section checks that the prediction code runs properly
# To run, type "python3 picrec_api_oneftn.py" in the terminal. **
#
# The if __name__='__main__' section ensures this code only runs
# when running this file; it doesn't run when importing
if __name__ == '__main__':
    from pprint import pprint
    print("Checking to see what it recommends for roast turkey recipe image (index=1412)")
    img_idx = 1412 #need to comment out .get line above, just use img_idx for testing api.py
    print('Recipe image index is')
    pprint(img_idx)

    recipe_list = ft_to_rec(img_idx)
    print(f'Input image index: {img_idx}')
    print('Output list of similar recipe names')
    pprint(recipe_list)

#test on 1412('perfect_roast_turkey_72482_16x9.jpg') passed, try different recipe index?
#193 'black_forest_gateau_43895_16x9.jpg'


