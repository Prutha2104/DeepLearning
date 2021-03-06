# -*- coding: utf-8 -*-
"""CNNNew.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1m_Zw0wwwF_3kNV4zcflAH5_Kh4PNUXJU
"""

##Convolutional neural network

from __future__ import print_function
import numpy as np
np.random.seed(1337)  # for reproducibility


from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Lambda
from keras.layers import Embedding
from keras.layers import Convolution1D,MaxPooling1D, Flatten
from keras.datasets import imdb
from keras import backend as K
from sklearn.metrics import accuracy_score,precision_score,cohen_kappa_score ,recall_score,roc_auc_score,fbeta_score

import pandas as pd
from google.colab import files
from keras.utils.np_utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Normalizer
from sklearn.metrics import classification_report
from keras.models import Sequential
from keras.layers import Convolution1D, Dense, Dropout, Flatten, MaxPooling1D
from keras.utils import np_utils
import numpy as np
import h5py
from keras import callbacks
from keras.layers import LSTM, GRU, SimpleRNN
from keras.callbacks import CSVLogger
from keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau, CSVLogger

uploaded=files.upload()

dataset = np.loadtxt("", delimiter="|")
# split into input (X) and output (Y) variables
X = dataset[:,0:1]
Y = dataset[:,1]

#normalize the data
scaler = Normalizer().fit(X)
X = scaler.transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=42)

# reshape input to be [samples, time steps, features]
X_train = np.reshape(X_train, (X_train.shape[0],X_train.shape[1],1))
X_test = np.reshape(X_test, (X_test.shape[0],X_test.shape[1],1))

cnn = Sequential()
cnn.add(Convolution1D(64, 3, border_mode="same",activation="relu",input_shape=(30, 1)))
cnn.add(MaxPooling1D(pool_length=(2)))
cnn.add(Flatten())
cnn.add(Dense(128, activation="relu"))
cnn.add(Dropout(0.5))
cnn.add(Dense(1, activation="sigmoid"))

cnn.compile(loss="binary_crossentropy", optimizer="adam",metrics=['accuracy'])

# train

cnn.fit(X_train.shape[0], y_train.shape[0], nb_epoch=100, validation_data=(X_test, y_test))
loss, accuracy = cnn.evaluate(X_test, y_test)
pred=cnn.predict(X_test)
y_pred = model.predict(X_test)
print(classification_report(y_true, y_pred))
print(confusion_matrix(X_test,y_test))
precision=precision_score(X_test,y_test)
reacall=recall_score(X_test,y_test)
print("\nprecision: "% precision_score(y_test,pred,normalize=False))
print("\nrecall: "% recall)
print("\nLoss: %.2f, Accuracy: %.2f%%" % (loss, accuracy*100))