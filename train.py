import os
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers,models
from tensorflow.keras.preprocessing import image_dataset_from_directory
from tensorflow.keras.applications import EfficientNetB0
import matplotlib.pyplot as plt

class EarlyStopping(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs=None):
        if logs.get('val_accuracy') >= 9.8e-1:
            self.model.stop_training = True

EarlyStopping_callback = EarlyStopping()

def Model():
    model = tf.keras.models.Sequential()

    model.add(layers.Conv2D(filters=32, kernel_size=(3,3), padding='same', input_shape=(None,None,1), activation='relu', name='First_Conv2D'))
    model.add(layers.MaxPool2D(pool_size=(2,2), name='First_Maxpool'))
    model.add(layers.Dropout(0.25))
    model.add(layers.Conv2D(filters=64, kernel_size=(3,3), padding='same', activation='relu', name='Second_Conv2D'))
    model.add(layers.MaxPool2D(pool_size=(2,2), name='Second_Maxpool'))
    model.add(layers.GlobalAveragePooling2D())
    model.add(layers.Dense(units=128, activation='relu', name='Dense'))
    model.add(layers.Dense(units=1, activation='sigmoid', name='Output'))

    return model

def efficientnet():
    efficientnet_model = EfficientNetB0(weights='imagenet',include_top=False)
    efficientnet_model.trainable = False

    input = layers.Input(shape=(None,None,1))
    efficientnet_layer = efficientnet_model(input)
    x = layers.GlobalAveragePooling2D(name="avg_pool")(efficientnet_layer)
    x = layers.Dense(units=128, activation='relu')(x)

    output = layers.Dense(units=1, activation='sigmoid', name='Output')(x)

    model = models.Model(inputs=input, outputs=output)
    return model

train_dir = "../DataSet/Data/train_png"
input_shape = (256,256)
train_generator = image_dataset_from_directory(directory=train_dir,label_mode='binary',batch_size=32,color_mode='grayscale',image_size=input_shape,seed=375729,validation_split=0.2,subset='training')
valid_generator = image_dataset_from_directory(directory=train_dir,label_mode='binary',batch_size=32,color_mode='grayscale',image_size=input_shape,seed=375729,validation_split=0.2,subset='validation')


model = efficientnet()
model.compile(loss='binary_crossentropy',
              optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
              metrics=['accuracy'])
model.summary()

history = model.fit(train_generator,validation_data=valid_generator,epochs=5,callbacks=[EarlyStopping_callback])

# summarize history for accuracy
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='upper left')
plt.savefig('acc.png')
# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='upper left')
plt.savefig('val.png')

test_dir = "../DataSet/Data/test_png"
evaluate_gen = image_dataset_from_directory(directory=test_dir,label_mode='binary',batch_size=32,color_mode='grayscale',image_size=input_shape)
loss,acc = model.evaluate(evaluate_gen)
print(acc)

model.save(f'model_{round(acc,3)}.h5')



