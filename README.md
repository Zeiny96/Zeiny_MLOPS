# Zeiny_API
- This is a flask based Covid-19_detector API
- To test it you can use:
```
curl -X 'GET' 'http://mahmoudelzeiny.pythonanywhere.com/alive'
```
- Or to send an x-rays image and get the result use:
```
curl -X 'POST' 'http://mahmoudelzeiny.pythonanywhere.com/prediction' \
     -H 'accept: application/json'   \
     -H 'Content-Type: multipart/form-data' \
     -F 'file=$image'
```
