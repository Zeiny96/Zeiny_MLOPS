import requests

def test_response():
  res_code = res.status_code #str(res).split('[')[1].split(']')[0]
  assert (res_code == expected_code)

# Alive endpoint test
res = requests.get('https://zeiny-mlops.herokuapp.com/alive')
expected_code = '200'
test_response()

# Prediction endpoint test
dir="COVID19.png"
image_file=open(dir,"rb")
dicttosend={'file':image_file}
res = requests.post('https://zeiny-mlops.herokuapp.com/prediction', files=dicttosend)
expected_code = '200'
test_response()

# Error handling
## Invalid, empty or corrupted file
dir="NORMAL.png"
image_file=open(dir,"rb")
dicttosend={'file':image_file}
res = requests.post('https://zeiny-mlops.herokuapp.com/prediction', files=dicttosend)
expected_code = '400'
test_response()

## Wrong endpoint
res = requests.get('https://zeiny-mlops.herokuapp.com/isalive')
expected_code = '404'
test_response()

## Wrong method
res = requests.post('https://zeiny-mlops.herokuapp.com/alive')
expected_code = '405'
test_response()

