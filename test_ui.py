import os
import io
from PIL import Image,ImageOps
from tensorflow.keras.models import load_model
import numpy as np

def load_image(img):
    img = Image.open(img)
    resized_img = img.resize((256,256),resample=Image.BILINEAR)
    grayscale_resize_img = ImageOps.grayscale(resized_img)

    return grayscale_resize_img

def predict(model,img):
    loaded_img = load_image(img)
    loaded_img = np.asarray(loaded_img)
    loaded_img = loaded_img.reshape(1,256,256,1)
    result = model.predict(loaded_img)[0][0]

    result = "NORMAL" if result >= 0.5 else "COVID19"
    assert result

img = "COVID19.png"
for accuracy in ['0.948','0.988']:
    model = load_model('model_0.948.h5')
    predict(model,img)



