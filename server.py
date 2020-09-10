import os

from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from pathlib import Path

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['apk', 'ipa', 'app', 'png', 'jpg', 'jpeg'])
path = Path(__file__).parent.absolute()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = os.urandom(24)
app.config['MAX_CONTENT_LENGTH'] = 200000000

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
        # submit an empty part without filename
        if file.filename == 'file':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash("Upload realizado com sucesso!!! ")
            return redirect(url_for('upload_file'))

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=9090, debug=True)