# Zeiny_API
- This is a flask based Covid-19_detector API.

## Content
- [Prerequisites](#prerequisites)
- [Structure](#structure)
- [Requests-Responses](#requests-responses)
- [Error_handling](#error_handling)

## Prerequisites
- Just install the libraries in the [requirements.txt](requirements.txt) file.

## Structure
- The main flask script is [app.py](app.py).
- It was first build using [python any where](https://www.pythonanywhere.com/), but it was inconsistent and unreliable at all.
- Then the final version was made using [herokuapp](https://dashboard.heroku.com/apps), where it will be linked to this repo and continuos deployment will be done between them using this [Webhook](https://github.com/Zeiny96/Zeiny_MLOPS/settings/hooks/366920485).
- The model used here is the small model, to use the efficientnet model it can be changed in the [app.py](app.py) by passing the [efficientnet based model path](models/model_efficientnet.h5).
- Then to be continuosly integrated [Test.yaml](.github/workflows/Test_CI.yaml) was created to run [test_api.py](test/test_api.py) to assert that the model and the api are running properly as expected.
- Now it can be accessed using this [url](https://zeiny-mlops.herokuapp.com/)

## Requests-Responses
- To test the api you can use:
```
curl -X 'GET' 'https://zeiny-mlops.herokuapp.com/alive'
```
- To get the same response in python:
```
import requests
res = requests.get('https://zeiny-mlops.herokuapp.com/alive')
print ('response from server:',res.json())
```
- Or to send an image and get the result use:
```
curl -X POST -F file=@"$file_path" https://zeiny-mlops.herokuapp.com/prediction
```
- To get the same response in python:
```
dir ="image.png"
image_file=open(dir,"rb")
dicttosend={'file':image_file}
res = requests.post('https://zeiny-mlops.herokuapp.com/prediction',files=dicttosend)
print ('response from server:',res.json())
```

## Error_handling
- In case of sending an invalid, empty or corrupted image, the api will response with code 400, with the following message:
```
{"error":"Invalid file ","Description":"The received file was either of an invalid extension, corrupted or empty"}
```
- In case of sending an empty json, the api will response with code 400, with the following message:
```
{"error":"Empty request","Description":"The received request had no file in it or wasn't in the required json form"}
```
- In case of client mistakes, the api will response with an error code of 400, with the following message:
```
{"error":"Bad Request Error","Description":"The process couldn't be proceeded due to a client error"}
```
- In case of trying to access a wrong endpoint , the api will response with an error code of 404, with the following message:
```
{"error":"Wrong endpoint","Description":"Tried to access an undefined endpoint, the only available endpoints are /alive /prediction"}
```
- In case of using a wrong method, the api will response with an error code of 405, with the following message:
```
{"error":"Method not allowed","Description":"A wrong method was used"}
```
- In case of internal server errors, the api will response with an error code starting from 500, with the following message:
```
{"error":"Internal server error","Description":"An internal server error has occured"}
```
