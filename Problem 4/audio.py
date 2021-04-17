# import moviepy.editor as mp

# clip = mp.VideoFileClip(r"jnt.mp4")

# clip.audio.write_audiofile(r"jnt.mp3")

'''
int DTWDistance(s: array [1..n], t: array [1..m]) 
    DTW := array [0..n, 0..m] 

    for i := 1 to n 
        for j := 1 to m 
            DTW[i, j] := infinity 
        DTW[0, 0] := 0 

    for i := 1 to n 
        for j := 1 to m 
            cost := d(s[i], t[j]) 
            DTW[i, j] := cost + minimum(DTW[i-1, j ], // insertion 
                                        DTW[i , j-1], // deletion 
                                        DTW[i-1, j-1]) // match
    return DTW[n, m] 
     
'''

import numpy as np 
import matplotlib.pyplot as plt
from scipy.io.wavfile import read, write
from numpy.fft import fft, ifft
# %matplotlib inline

Fs, data = read('jnt.wav')
data = data[:,0]
print("Sampling frequency is", Fs)

plt.figure()
plt.plot(data)
plt.xlabel("Sample index")
plt.ylabel("Amplitude")
plt.title("Waveform of Test Audio")
plt.show()