import flask
import requests
from gevent.pywsgi import WSGIServer
from werkzeug.exceptions import HTTPException
import os
import magic
import tensorflow as tf
from tensorflow.keras.models import load_model
from predict import predict

# Forcing the server to use only cpu
os.environ["CUDA_VISIBLE_DEVICES"]="-1"

# Loading the model
model = load_model('Zeiny_MLOPS/model.h5')

# Preparing error messages
invalid_file={"error":"Invalid file ","Description":"The received file was either of an invalid extension, corrupted or empty"}
empty_json={"error":"Empty request","Description":"The received request had no file in it or wasn't in the required json form"}

app = flask.Flask(__name__)

@app.route("/")
def index():
        return "Welcome To My Covid-19_detector API"

@app.route('/git_update', methods=['POST'])
def git_update():
    repo = git.Repo('./orbe')
    origin = repo.remotes.origin
    repo.create_head('main',
                     origin.refs.main).set_tracking_branch(origin.refs.API).checkout()
    origin.pull()
    return '', 200

@app.route("/alive", methods=["GET"])
def alive():
    js={"message":"Server is fkin alive!"}
    return js


@app.route("/prediction", methods=["POST"])
def prediction():
    try:
        received_file = flask.request.files['file']
    except:
        return empty_json,400
    image = received_file.read()
    file_type = magic.from_buffer(image,mime=True).split('/')[0]
    if file_type != 'image':
        return invalid_file,400
    result = predict(model,image)
    js = {"result":result}
    return js


@app.errorhandler(Exception)
def handle_error(e):
    code=0
    if isinstance(e,HTTPException):
        code = e.code
    if (code==404):
        msg={"error":"Wrong endpoint","Description":"Tried to access an undefined endpoint, The only available endpoints are /alive /prediction"}
        return msg,code
    elif (code==405):
        msg={"error":"Method not allowed","Description":"A wrong method was used"}
        return msg,code
    elif(code==400):
        msg={"error":"Bad Request Error","Description":"The process couldn't be proceeded due to a client error"}
        return msg,code
    else:
        msg={"error":"Internal server error","Description":"An internal server error has occured"}
        return e.description,msg,500

#server = WSGIServer(('', 5000), app)
print('Server initiated successfully')
#server.serve_forever()








