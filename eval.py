import os
import tensorflow as tf

import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing import image_dataset_from_directory
from tensorflow.keras.models import load_model

import matplotlib.pyplot as plt

input_shape = (256,256)
model = load_model("models/model_0.988.h5")
test_dir = "../DataSet/Data/test_png"
evaluate_gen = image_dataset_from_directory(directory=test_dir,label_mode='binary',batch_size=32,color_mode='grayscale',image_size=input_shape)

predictions = np.array([])
labels =  np.array([])
for x, y in evaluate_gen:
    predictions = np.concatenate([predictions, model.predict(x).flatten()])
    labels = np.concatenate([labels, y.numpy().flatten()])

predictions = predictions > 0.5

from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import accuracy_score
import seaborn as sns
cm = confusion_matrix(labels, predictions)
sns.heatmap(cm, annot=True, xticklabels=['Covid', 'Normal'], yticklabels=['Covid', 'Normal'])
Precision,Recall,F1_score,_ = precision_recall_fscore_support(labels, predictions, average='macro')
Accuracy = accuracy_score(labels, predictions)
print(f'Precision: {round(Precision*100,4)}%\nRecall: {round(Recall,4)}%\nF1_score: {round(F1_score,4)}%\nAccuracy: {round(Accuracy,4)}%')
plt.show()
