from flask import Flask
import json, utils
from flask_cors import cross_origin

app = Flask(__name__)

@app.route('/get/courses/coursera/<key_word>')
@cross_origin()
def get_course(key_word):
    return  json.dumps(utils.get_course(key_word))