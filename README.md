# pic-a-recipe

### Motivation
We are often taking photos of our food when eating out. How many times have you seen a photo on social media and thought - *"I want to have that"*? But what if you don't know the name of the dish?

A related problem is, when travelling abroad we may eat something we really like, snap a photo of it, then forget what it is called. So we couldn't easily search for the recipe when we get home. 

I would like to **build a usable recipe recommendation system in the form of a web app, where the recommendation is generated based on a photo.**

Another personal motivation for this data science project is to dive deeper into the domain for my Metis Project 4. Like in my previous Metis project ([Project 4 proposal](https://github.com/floraxinru/metisproject04/blob/master/Project4_proposal_v2.pdf)), I want to encourage people to expand their palate, as well as help them recreate dishes similar to the ones they’ve had in restaurants.


### Design
Because this was my final project at Metis and a passion project, I got really excited and a bit too ambitious in the proposal stage. I wanted to work NLP which was my favourite aspect, as well as work with images and deep learning which was the newest field we covered during lectures. My initial goal was to tackle image classification of food pictures. But after some initial research I realized this is a difficult problem in an area of ongoing research and would be impractical for me to expect to make a significant contribution within a few weeks (each improvement on a CNN architecture might be a valid PhD thesis).

But I did accomplish the following goals in my proposal:
> The pipeline I am hoping to build will start from the photograph of a dish (which could be taken at a restaurant and uploaded to Instagram), to a classifier which outputs the type of food (for example: pasta, pizza, cake), to recipe recommendations of related dishes. 
For the end product, I hope to make a (mobile-friendly) working Flask web app, where the user can click on (or upload) an image, get the list of top classification results, as well as recipe recommendations in the form of links to recipes on the source websites.

### Data
I used data from this data dump of 140K English recipes with images (https://archive.org/details/recipes-en-201706), and figured out how to extract the tar.xz files. Since recipe data is time-insensitive, I decided to use this data instead of scraping from the same websites on my own. The data was scraped from four websites in the Summer of 2017:
Contents
    allrecipes.com: 91K recipes, with photos, HTML, and crawling code
    epicurious.com: 34K recipes, with photos, JSON, and crawling code
    bbc.co.uk:      10K recipes, with photos, HTML, and crawling code
    cookstr.com:    8K recipes, with photos, HTML, and crawling code
There were issues with the labelling of the images as well as image formats. I ended up using the bbc dataset for my mvp as well as the final Flask App demo because it has the most informative image names.

### Tools
Python, Pandas, NumPy, SciPy, scikit-learn, nltk, Gensim

Deep Learning, CNN: Keras, VGG16

Web App: Flask, HTML, CSS, Jinja2

Scripting: Jupyter Notebook, Visual Studio Code

AWS EC2, GitHub, cookiecutter (datasciencemvp template)


### Results
I successfully built a pipeline which goes from an uploaded image to the top 5 recipe recommendations, using cosine similarity (between VGG16-extracted image features) as the metric, all interactive in my very first Flask app. 
(currently having trouble uploading/displaying Flask App demo video, will update soon)

### Future Work
I was fairly close to merging the CNN and NLP portions of this project, before I had to make the difficult decision of scrapping the NLP and topic modelling results to focus on making a Flask web app and practice my presentation. For future work I would like to finish debugging that part of the code, in order to reduce the amount of images that would be included in the cosine similarity calculation ("filtering" the images by the NLP-generated topics).

Eventually I would also like to train the model on a larger dataset, so it would perform better when predicting user images. At that point it would be great to make the web app mobile-friendly (probably need to change the CNN architecture to use MobileNetV2, which would be a side project on its own), and to deploy it so other people can use it.

### Lessons Learned
(blogpost coming soon)

------
### Selected References
StackOverflow

Design Inspirations - two excellent Metis projects: 
- https://jhonsen.github.io/2019/04/22/Produce2Recipe/
- https://hengrumay.github.io/MenuPlannerHelper/

Flask and HTML Tutorials:
- https://www.w3schools.com/html/html_forms.asp
- https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates
- https://github.com/ibrahimokdadov/upload_file_python

Keras-CNN Image Preprocessing:
- https://keras.io/applications/#models-for-image-classification-with-weights-trained-on-imagenet
- https://github.com/mlBhanuYerra/Metis_prj3/blob/master/Code/1b_VGG19Data.ipynb
