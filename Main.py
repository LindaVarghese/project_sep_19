# -*- coding: utf-8 -*-

Main.py

import os
from app import app
import urllib.request
from werkzeug.utils import secure_filename
from flask import Flask, flash, request, redirect, url_for, render_template

app = Flask(__name__)


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_form():
	return render_template('upload.html')

def transform(images):
	for i, image in enumerate(images):
		fname = 'image'+str(i)+'.png'
		fname = 'image'+str(i)+'.jpg
		fname = 'image'+str(i)+'.jpeg
    		image.save(fname, "PNG")
		image.save(fname, "JPG")
    		image.save(fname, "JPEG")
return images

@app.route('/convert', methods=["POST"])
def convert():
    file = request.files['img_file']
    if not file:
        return "No file"

    img = Image.open(file)
    result = transform(img)
    response = make_response(result)
    return response

@app.route('/compress', methods=["POST"])
def compress():
 	file = request.files['img_file']
    	if not file:
        		return "No file"
    	img = Image.open(file)
	ext = img.rsplit('.', 1)[1].lower()
    	resized_img = img.resize((50, 50))
    	resized_img.save("resized_image",ext)
    	return resized_img.

@app.route('/', methods=['POST'])
def upload_image():
	if 'files' not in request.files:
		flash('No file')
		return redirect(request.url)
	files = request.files.getlist('files')
	file_names = []
	for file in files:
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file_names.append(filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		else:
			flash('Allowed image types are -> png, jpg, jpeg, gif')
			return redirect(request.url)
			return render_template('upload.html', filenames=file_names)
	
if __name__ == "__main__":
	app.run(host=’0.0.0.0’, port=5000,debug=True)
