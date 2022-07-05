import requests

def test_alive():
  res_code = str(res).split('[')[1].split(']')[0]
  assert (res_code == '200')
  assert (res.json()['message']=='Server is alive!')

def test_response():
  res_code = str(res).split('[')[1].split(']')[0]
  assert (res_code == '200')

res = requests.get('http://mahmoudelzeiny.pythonanywhere.com/alive')
test_alive()

dir="COVID19.png"
image_file=open(dir,"rb")
dicttosend={'file':image_file}
res = requests.post('http://mahmoudelzeiny.pythonanywhere.com/prediction', files=dicttosend)
test_response()
