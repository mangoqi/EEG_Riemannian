import sys, os
import yaml
import numpy as np
import preprocessing
from library.feature_extraction import feature_extraction
from main_spatial_val import experiments
from main_temporal_val import experiments

from utils import root_mean_squared_error_numpy, load_dataset_signal_addr, load_dataset_feature_addr, parse_valid_data_all, save_test_result
##############################
# import numpy as np
# from scipy.signal import butter, filtfilt
# import matplotlib.pyplot as plt

# # Generate some example EEG data
# fs = 1000  # Sampling frequency (Hz)
# t = np.arange(0, 10, 1/fs)  # Time vector
# eeg_data = np.sin(2 * np.pi * 10 * t) + np.random.normal(0, 0.5, len(t))

# # Define the band-pass filter parameters
# lowcut = 0.5  # Lower cut-off frequency (Hz)
# highcut = 70.0  # Upper cut-off frequency (Hz)
# order = 5  # Filter order

# # Create the band-pass Butterworth filter
# def butter_bandpass(lowcut, highcut, fs, order=5):
#     nyquist = 0.5 * fs
#     low = lowcut / nyquist
#     high = highcut / nyquist
#     b, a = butter(order, [low, high], btype='band')
#     return b, a

# # Apply the band-pass filter
# b, a = butter_bandpass(lowcut, highcut, fs, order=order)
# filtered_eeg_data = filtfilt(b, a, eeg_data)

# # Plot the original and filtered EEG signals
# plt.figure()
# plt.subplot(2, 1, 1)
# plt.plot(t, eeg_data, 'b-', linewidth=1, label='Original EEG')
# plt.title('Original EEG Signal')
# plt.subplot(2, 1, 2)
# plt.plot(t, filtered_eeg_data, 'g-', linewidth=1, label='Filtered EEG')
# plt.title('Band-Pass Filtered EEG Signal')
# plt.tight_layout()
# plt.show()


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
#     freq_band = data.shape[1]
#     channel = data.shape[2]
#     timestep = 7
#     L = 1*250
#     features = np.zeros((trial,freq_band,channel,timestep,features_len))
#     for i in range(0,trial):
#         for j in range(0,freq_band):
#             for k in range(0,channel):
#                 for l in range(0,data.shape[3]-125,125):
#                     features[i,j,k,int(l/125),:] = feature_extraction(data[i,j,k,l:l+250])
#     np.save(data_train_addr.format(subject_No), features)

#     #_________________testing_data_________________________#
#     data = np.load('./DATA/BCI_IV_2a/test/EEG/filter_data_'+str(subject_No)+'.npy') # trial*freq_band*channel*1000
#     features_len = 50 # 25len psd and 25len DE
#     trial = data.shape[0]
#     freq_band = data.shape[1]
#     channel = data.shape[2]
#     timestep = 7
#     L = 1*250
#     features = np.zeros((trial,freq_band,channel,timestep,features_len))
#     for i in range(0,trial):
#         for j in range(0,freq_band):
#             for k in range(0,channel):
#                 for l in range(0,data.shape[3]-125,125):
#                     features[i,j,k,int(l/125),:] = feature_extraction(data[i,j,k,l:l+250])
#     np.save(data_test_addr.format(subject_No), features)

# spatial feature processing
# experiments('BCI_IV_2a').run_bci()

# temporal feature processing
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


