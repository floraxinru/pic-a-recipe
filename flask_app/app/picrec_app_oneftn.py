import flask
from flask import Flask, flash, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import os
from picrec_api_oneftn import ft_to_rec, bbc_path, bbc_ft



# Initialize the app
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('basetemplate.html') 


#example from tutorialspoint, changed duplicate ftn defn upload_file() - app wouldn't run without removing this:
# from flask import Flask, render_template, request
# from werkzeug import secure_filename
# app = Flask(__name__)

@app.route('/upload')
def upload():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename)) #change filepath to upload to folder?
      return 'File uploaded successfully!'
		


@app.route("/recommend")#, methods = ['GET', 'POST'])
def recommend():
    # request.args contains all the arguments passed by our form
    # comes built in with flask. It is a dictionary of the form
    # "form name (as set in template)" (key): "string in the textbox" (value)
    index_key, recs  = ft_to_rec(request.args) #input and pred from make_pred ftn; request.args-reading in user inputs from webpage
    #img_idx, names_list  = ft_to_rec(request.args) 
    return render_template('picrec.html', index_key=index_key,
                                recommendations=recs, bbc_path=bbc_path, bbc_ft=bbc_ft) 


if __name__ == '__main__':
    app.run(debug=True)