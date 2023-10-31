# filter, normalization,
from __future__ import division, print_function
import pyedflib
import numpy as np
from scipy import signal
from scipy.signal import butter, lfilter, sosfilt, sosfreqz
import matplotlib.pyplot as plt
from pylab import figure,show,setp
import matplotlib.cbook as cbook
import matplotlib.cm as cm
from matplotlib.collections import LineCollection
from matplotlib.ticker import MultipleLocator
from tqdm import tqdm
from scipy import stats
import os


#___Notch_Filter___#
fs=250
f0 = 50.0  # Frequency to be removed from signal (Hz) notch_freq
Q = 30.0  # Quality factor
w0 = f0/(fs/2)  # Normalized Frequency


order = 4

def butter_notch(data, notch_freq, fs, Q):
    # Q 是品质因数；notch_freq 是陷波滤波的频率
    nyq = 0.5 * fs
    freq = notch_freq / nyq
    b, a = butter(2, freq, btype='bandstop')
    filtered_data = lfilter(b,a,data)
    return filtered_data

# ___Bandpass_Filter___#
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    sos = butter(order, [low, high], analog=False, btype='band', output='sos')
    # Array of second-order filter coefficients, must have shape (n_sections, 6). Each row corresponds to a second-order section, with the first three columns providing the numerator coefficients and the last three providing the denominator coefficients.
    return sos


    # def butter_bandpass_filter(data, lowcut, highcut, fs, order=order):
    #     b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    #     y = lfilter(b, a, data)
    
    
    #     return y

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    sos = butter_bandpass(lowcut, highcut, fs, order=order)
    y = sosfilt(sos, data) # Filter data along one dimension using cascaded second-order sections.

    return y


class signal_filtering:
    def __init__(self, dataset):
        self.dataset = dataset


    def main(self, data):
        if self.dataset =='BCI_IV_2a':
            start_point, end_point = 2.0, 6.0
            channel_num = 22
        if self.dataset =='BCI_IV_2b':
            start_point, end_point = 3.4, 7.5
            channel_num = 3
        # plt.plot(data.T)
        # plt.show()
        data = data[:,int(fs*start_point):int(fs*end_point)] # 为什么load数据的时候用7*250的窗，现在又截成1000的？？？

        # for channel in range(data.shape[0]):
        #     data[channel] = (data[channel] - np.min(data[channel]))/ (np.max(data[channel])-np.min(data[channel]))

        new_data = np.zeros((25, data.shape[0], data.shape[1])) #frequency_band, channels, time-series
        # plt.plot(data[2])
        # plt.show()
        for m in range(0, 25): #frequency band
            for k in np.arange(0, channel_num):              
                new_data[m, k] = butter_bandpass_filter(data[k], lowcut= 0.5 + m*2 , highcut= 0.5 +(m+1)*2, fs=250, order=order)
                # if m == 0:
                #     new_data[m, k,:] = butter_bandpass_filter(data[k,:], lowcut= 0.5 , highcut= 2.0, fs=250, order=order)
                # elif m == 1:
                #     new_data[m, k,:] = butter_bandpass_filter(data[k,:], lowcut= 2.0 , highcut= 4.0, fs=250, order=order)
                # elif m == 2:
                #     new_data[m, k,:] = butter_bandpass_filter(data[k,:], lowcut= 4.0,  highcut= 10.0, fs=250, order=order)
                # elif m == 3:
                #     new_data[m, k,:] = butter_bandpass_filter(data[k,:], lowcut= 10.0 ,  highcut= 20, fs=250, order=order)
                # else:
                #     new_data[m, k,:] = butter_bandpass_filter(data[k,:], lowcut= 20.0 ,  highcut= 40, fs=250, order=order)
        #
                # plt.plot(new_data[m,k])
                # plt.show()
        # exit(0)
        # new_data[m, k,:] = (new_data[m, k,:] - min(new_data[m, k,:]))/ (max(new_data[m, k,:])-min(new_data[m, k,:]))
        # for channel in range(new_data.shape[0]):
        #     new_data[channel] = (new_data[channel] - np.min(new_data[channel]))/ (np.max(new_data[channel])-np.min(new_data[channel]))

        new_data = new_data.tolist()

        return new_data







#
