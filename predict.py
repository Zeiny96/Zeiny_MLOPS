import os
import io
import numpy as np
from PIL import Image,ImageOps
from flask import abort

def load_image(image):
    image = io.BytesIO(image)
    image = Image.open(image)
    image = image.resize((256,256),resample=Image.BILINEAR)
    image = ImageOps.grayscale(image)
    return image

def predict(model,image):
    image = load_image(image)
    image = np.asarray(image).reshape(1,256,256,1)
    result = model.predict(image)[0][0]
    result = "NORMAL" if result >= 0.5 else "COVID19"
    return result


