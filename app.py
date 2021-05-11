# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#    return 'Hello World!'
#
#
# if __name__ == '__main__':
#   app.run()

import os
from flask import Flask, flash, request, redirect, url_for, session
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import logging

logging.basicConfig(level=logging.INFO)

# logger = logging.getLogger('HELLO WORLD')


UPLOAD_FOLDER = '/path/uploads'
ALLOWED_EXTENSIONS = set(['csv'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/upload', methods=['POST'])
def fileUpload():
    target = os.path.join(UPLOAD_FOLDER, 'test_docs')
    if not os.path.isdir(target):
        os.mkdir(target)
    # logger.info("welcome to upload`")
    file = request.files['file']
    filename = secure_filename(file.filename)
    destination = "/".join([target, filename])
    file.save(destination)
    session['uploadFilePath'] = destination
    return


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", use_reloader=False)

# @app.route('/api/upload', methods = ['POST'])
# def upload_file():
#    file = request.files['file']
#    print(file)
#    return "done"

# flask_cors.CORS(app, expose_headers='Authorization')
