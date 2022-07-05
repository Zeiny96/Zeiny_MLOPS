# Zeiny_API
- This is a flask based Covid-19_detector API.
- The main flask script is [app.py](app.py).
- It was first build using [python any where](https://www.pythonanywhere.com/), but it was inconsistent and unreliable at all.
- Then the final version was made using [herokuapp](https://dashboard.heroku.com/apps)
- The model used here is the small model, to use the efficientnet model it can be changed in the [app.py](app.py) by passing the [efficientnet based model path](models/model_efficientnet.h5).
- Now it can be accessed using this [url](https://zeiny-mlops.herokuapp.com/)
- To test it you can use:
```
curl -X 'GET' 'http://mahmoudelzeiny.pythonanywhere.com/alive'
```
- Or to send an image and get the result use:
```
curl -X POST -F file=@"$file_path" https://zeiny-mlops.herokuapp.com/prediction
```
