#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import zipfile
from flask import Flask, request, redirect, url_for, flash, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.path.dirname(os.path.realpath(__file__))
ALLOWED_EXTENSIONS = set(['txt'])

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file_count = request.files['count']
        file_gene = request.files['gene']
        file_sgrna = request.files['sgrna']
        for file in [file_count, file_gene, file_sgrna]:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(UPLOAD_FOLDER, filename))
        return redirect(url_for('upload_file',filename=filename))
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
