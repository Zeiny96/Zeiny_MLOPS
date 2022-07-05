import requests

def test_response():
  res_code = str(res).split('[')[1].split(']')[0]
  assert (res_code == '200')

res = requests.get('https://zeiny-mlops.herokuapp.com/alive')
test_response()

dir="COVID19.png"
image_file=open(dir,"rb")
dicttosend={'file':image_file}
res = requests.post('https://zeiny-mlops.herokuapp.com/prediction', files=dicttosend)
test_response()
