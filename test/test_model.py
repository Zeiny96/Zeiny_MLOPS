import os
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image,ImageOps

def load_image(img):
    img = Image.open(img)
    resized_img = img.resize((256,256),resample=Image.Resampling.BILINEAR)
    grayscale_resize_img = ImageOps.grayscale(resized_img)
    return resized_img

def test_predict(model,img):
    loaded_img = load_image(img)
    loaded_img = np.asarray(loaded_img)
    loaded_img = loaded_img.reshape(1,256,256,1)
    return model.predict(loaded_img)[0][0]
    

img = "COVID19.png"
for accuracy in ['0.948']:
    model = load_model(f'model_{accuracy}.h5')
    test_predict(model,img)
