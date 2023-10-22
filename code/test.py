import sys, os
import yaml
import numpy as np
import preprocessing
from library.feature_extraction import feature_extraction
from main_spatial_val import experiments

from utils import root_mean_squared_error_numpy, load_dataset_signal_addr, load_dataset_feature_addr, parse_valid_data_all, save_test_result

# save preprocessing data
# preprocessing.bci_iv_2a()

# extraction features
# PATH = './DATA/BCI_IV_2a/'
# data_train_addr  = os.path.join(PATH,'train/' + 'Extracted Features/features_{}.npy') # subject
# data_test_addr   = os.path.join(PATH,'test/'  + 'Extracted Features/features_{}.npy') # subject

# for subject_No in (range(1, 10)):  
#     #_________________training_data_________________________#
#     data = np.load('./DATA/BCI_IV_2a/train/EEG/filter_data_'+str(subject_No)+'.npy') # trial*freq_band*channel*1000
#     features_len = 50 # 25len psd and 25len DE
#     trial = data.shape[0]
#     channel = data.shape[2]
#     features = np.zeros((trial,channel,features_len))
#     for i in range(0,trial):
#         for j in range(0,channel):
#             features[i,j,:] = feature_extraction(data[i,:,j,:])
#     np.save(data_train_addr.format(subject_No), features)

#     #_________________testing_data_________________________#
#     data = np.load('./DATA/BCI_IV_2a/test/EEG/filter_data_'+str(subject_No)+'.npy') # trial*freq_band*channel*1000
#     features_len = 50 # 25len psd and 25len DE
#     trial = data.shape[0]
#     channel = data.shape[2]
#     features = np.zeros((trial,channel,features_len))
#     for i in range(0,trial):
#         for j in range(0,channel):
#             features[i,j,:] = feature_extraction(data[i,:,j,:])
#     np.save(data_test_addr.format(subject_No), features)

# spatial feature processing
experiments('BCI_IV_2a').run_bci()

# test part

def load_config(name):
    with open(os.path.join(sys.path[0], name)) as file:
        config = yaml.safe_load(file)

    return config

config = load_config('dataset_params.yaml')
addr_dict = load_dataset_signal_addr('BCI_IV_2a')

data_train_addr, data_test_addr, label_train_addr, label_test_addr = list(addr_dict.values())
print(data_test_addr)


