#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Flask, request, redirect, url_for, flash, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/Users/cuiyb/workspace/upload-multi-files-one-shot'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'yaml'])

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            return redirect(url_for('upload_file',
                                    filename=filename))
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
