# Zeiny_train
- In this repo the training steps will be discussed
- Where 2 models were trained a small model trained from scratch with the following architecture:
```
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
First_Conv2D (Conv2D)        (None, None, None, 32)    320
_________________________________________________________________
First_Maxpool (MaxPooling2D) (None, None, None, 32)    0
_________________________________________________________________
dropout (Dropout)            (None, None, None, 32)    0
_________________________________________________________________
Second_Conv2D (Conv2D)       (None, None, None, 64)    18496
_________________________________________________________________
Second_Maxpool (MaxPooling2D (None, None, None, 64)    0
_________________________________________________________________
global_average_pooling2d (Gl (None, 64)                0
_________________________________________________________________
Dense (Dense)                (None, 128)               8320
_________________________________________________________________
Output (Dense)               (None, 1)                 129
=================================================================
Total params: 27,265
Trainable params: 27,265
Non-trainable params: 0
_________________________________________________________________
```
- Where the other model was an efficientnet based model with the following architecture:
```
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
input_2 (InputLayer)         [(None, None, None, 1)]   0
_________________________________________________________________
efficientnetb0 (Functional)  (None, None, None, 1280)  4049571
_________________________________________________________________
avg_pool (GlobalAveragePooli (None, 1280)              0
_________________________________________________________________
dense (Dense)                (None, 128)               163968
_________________________________________________________________
Output (Dense)               (None, 1)                 129
=================================================================
Total params: 4,213,668
Trainable params: 164,097
Non-trainable params: 4,049,571
_________________________________________________________________
```
- The difference in the number of parameters is huge so the performance of the small model is by far much faster
