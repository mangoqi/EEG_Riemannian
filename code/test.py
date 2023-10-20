import os
import numpy as np
from library.feature_extraction import feature_extraction
# from load_data import load_MI
import preprocessing
from utils import root_mean_squared_error_numpy, load_dataset_signal_addr, load_dataset_feature_addr, parse_valid_data_all, save_test_result

# save preprocessing data
# preprocessing.bci_iv_2a()

# extraction features
data = np.load("./DATA/BCI_IV_2a/train/EEG/filter_data_1.npy") # trial*freq_band*channel*1000
features = feature_extraction(data[0,:,0,:])
trial = data.shape[0]
channel = data.shape[2]
features = np.zeros(trial,channel)
for i in range(0,trial):
    for j in range(0,channel):
        features[i,j] = feature_extraction(data[i,:,j,:])


# test part
path = './DATA/BCI_IV_2a/train/'
a = np.load('./DATA/BCI_IV_2a/train/filter_data_1.npy',allow_pickle=True)
print(a.shape[1])


