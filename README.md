# Zeiny_API
- This is a flask based Covid-19_detector API.
- The main flask script is [app.py](app.py).
- It was first build using [python any where](https://www.pythonanywhere.com/), but it was inconsistent and unreliable at all.
- Then the final version was made using [herokuapp](https://dashboard.heroku.com/apps), where it will be linked to this repo and continuos deployment will be done between them.
- The model used here is the small model, to use the efficientnet model it can be changed in the [app.py](app.py) by passing the [efficientnet based model path](models/model_efficientnet.h5).
- Then to be continuosly integrated [Test.yaml](.github/workflows/Test_CI.yaml) was created to run [test_api.py](test/test_api.py) to assert that the model is running properly.
- Now it can be accessed using this [url](https://zeiny-mlops.herokuapp.com/)
- To test it you can use:
```
curl -X 'GET' 'https://zeiny-mlops.herokuapp.com/alive'
```
- Or to send an image and get the result use:
```
curl -X POST -F file=@"$file_path" https://zeiny-mlops.herokuapp.com/prediction
```
