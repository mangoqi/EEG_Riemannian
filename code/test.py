from load_data import load_MI
import os
from library.signal_filtering import signal_filtering
import numpy as np

# load one person data
PATH = './data/BCICIV_2a/'
open_path = os.path.join(PATH,'train/')
data, label = load_MI(1,True,open_path)
print(data.shape[0])
print(label.shape)

data_train_addr  = os.path.join(PATH,'train/data_{}') # subject
data_test_addr   = os.path.join(PATH,'test/data_{}') # subject

label_train_addr = os.path.join(PATH,'train/label_{}') # subject
label_test_addr  = os.path.join(PATH,'test/label_{}') # subject

data_train_filter_addr = os.path.join(PATH,'train/filter_data_{}') # subject
data_test_filter_addr  = os.path.join(PATH,'test/filter_data_{}') # subject

# signal filtering
for subject_No in (range(1, 10)):

        #_________________training_data_________________________#
        data, label = load_MI(subject_No,True,open_path)

        filter_data = []

        for trial_No in range(data.shape[0]):
            data_trial  = data[trial_No]
            filter_data.append(signal_filtering(data_trial))

        filter_data = np.array(filter_data)
        np.save(data_train_filter_addr.format(subject_No), filter_data)

        np.save(data_train_addr.format(subject_No),  data)
        np.save(label_train_addr.format(subject_No), label)

# feature extraction

