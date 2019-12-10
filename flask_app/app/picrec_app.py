import flask
from flask import Flask, flash, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import os



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
		
# if __name__ == '__main__':
#    app.run(debug = True)


#example from docs, broke code?
# UPLOAD_FOLDER = './static/uploads'
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'csv', 'pkl'}

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#check if an extension is valid and that uploads the file and redirects the user to the URL for the uploaded file

# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['file']
#         # if user does not select file, browser also
#         # submit an empty part without filename
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             return redirect(url_for('uploaded_file',
#                                     filename=filename))

#     return '''
#     <!doctype html>
#     <title>Upload new file</title>
#     <h1>Upload new file</h1>
#     <form method=post enctype=multipart/form-data>
#       <input type=file name=file>
#       <input type=submit value=Upload>
#     </form>
#     '''

# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'],filename)
  



@app.route("/recommend")#, methods = ['GET', 'POST'])
def recommend():
    return render_template('picrec.html')


if __name__ == '__main__':
    app.run(debug=True)