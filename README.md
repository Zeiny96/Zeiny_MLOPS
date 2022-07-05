# Zeiny_API
- This is a flask based Covid-19_detector API
- To test it you can use:
```
curl -X 'GET' 'http://mahmoudelzeiny.pythonanywhere.com/alive'
```
- Or to send an image and get the result use:
```
curl -X POST -F file=@"$file_path" https://zeiny-mlops.herokuapp.com/prediction
```
