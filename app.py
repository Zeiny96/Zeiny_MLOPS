import streamlit as st
import os, io
import magic
from PIL import Image,ImageOps
from tensorflow.keras.models import load_model
import numpy as np

def load_image(img):
    img = io.BytesIO(img)
    img = Image.open(img)
    resized_img = img.resize((256,256),resample=Image.Resampling.BILINEAR)
    grayscale_resize_img = ImageOps.grayscale(resized_img)

    return grayscale_resize_img

def predict(model,img):
    loaded_img = load_image(img)
    loaded_img = np.asarray(loaded_img)
    loaded_img = loaded_img.reshape(1,256,256,1)
    result = model.predict(loaded_img)[0][0]

    result = "NORMAL" if result >= 0.5 else "COVID19"
    return result

st.title("Covid-19_detector")
st.write("Choose the suitable model from the left sidebar, upload the image then click predict to get the result")
nav = st.sidebar.radio("Model selection",["Large Efficientnet based model","Small trained from scratch model"])

if nav == "Large Efficientnet based model":
    model = load_model('models/model_efficientnet.h5')
    st.write("You chose the Efficientnet based model with about 99% accuracy ")

if nav == "Small trained from scratch model":
    model = load_model('models/model_small.h5')
    st.write("You chose the smaller trained from scratch model with about 95% accuracy ")

uploaded_file = st.file_uploader("Upload an image")
if uploaded_file is not None:
    uploaded_file = uploaded_file.read()
    file_type = magic.from_buffer(uploaded_file,mime=True).split('/')[0]
    if file_type == 'image':
        img = uploaded_file
        if st.button("Predict"):
            state = predict(model,img)
            if state=='NORMAL':
                st.title(f'**This x-rays belong to a normal person**')
            else:
                st.title(f'**This x-rays belong to a covid-19 infected person**')
        if st.checkbox("Show image"):
            st.image(img)
    else:
        st.title(f'**The uploaded file type was {file_type}, only images are accepted**')
