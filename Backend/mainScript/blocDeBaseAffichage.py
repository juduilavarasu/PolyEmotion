import pyqtgraph as pg
import numpy as np
<<<<<<< .merge_file_YE34RR
from pyqtgraph.Qt import QtGui
plt = pg.plot()
plt1 = pg.plot()
bufferSize = 1000
data = np.zeros(bufferSize)
curve = plt.plot()
line = plt.addLine(x=0)
plt.setRange(xRange=[0, bufferSize], yRange=[-50, 50])
plt1.setRange(xRange=[0, bufferSize], yRange=[-50, 50])
i = 0
def update():
    global data, curve, line, i
    n = 10  # update 10 samples per iteration
    rand = np.random.normal(size=n)
    data[i:i+n] = np.clip(data[i-1] + rand, -50, 50)
    curve.setData(data)
    i = (i+n) % bufferSize
    line.setValue(i)
=======
from pyqtgraph.Qt import QtGui, QtCore
from collections import deque
from random import random
from time import time

# lire les donnees du fichier
eeg_data = []
with open('OpenBCI-RAW-2018-02-01_19-15-17.txt') as f:
    for i, line in enumerate(f):
        if 5 < i:
            line = line.split(',')
            ch2 = float(line[2])
            eeg_data.append(ch2)


# filtrer le signal
# def butter_lowpass(cutOff, fs, order=5):
#     nyq = 0.5 * fs
#     normalCutoff = cutOff / nyq
#     b, a = butter(order, normalCutoff, btype='low', analog = True)
#     return b, a
#
# def butter_lowpass_filter(data, cutOff, fs, order=4):
#     b, a = butter_lowpass(cutOff, fs, order=order)
#     y = lfilter(b, a, data)
#     return y
#
# eeg_data_filter = butter_lowpass_filter(data=eeg_data, cutOff=60, order=4)

plt = pg.plot()
bufferSize = 500
data = deque(np.zeros(bufferSize), maxlen=bufferSize)
curve = plt.plot()
plt.setRange(xRange=[0, bufferSize], yRange=[-60000, -50000])
i = 0
sample_no = 0

def update():
    global data, curve, line, i, sample_no
    if i % bufferSize == 0:
        i = 0
    data.append(eeg_data[sample_no])
    curve.setData(data)
    i += 1
    sample_no += 1
    # time.sleep(0.05)

>>>>>>> .merge_file_ZOZAk5

timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(10)
<<<<<<< .merge_file_YE34RR
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
=======

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
>>>>>>> .merge_file_ZOZAk5
