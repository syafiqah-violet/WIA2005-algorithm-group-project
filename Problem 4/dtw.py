import wave
import numpy as np

#this audio says "memohon maaf"
jnt = wave.open("jnt-memohonmaaf.wav", "r")
jnt_soundwave = jnt.readframes(-1)

jnt_slow = wave.open("jnt-memohonmaaf-slowed.wav", "r")
jnt_soundwave_slow = jnt_slow.readframes(-1)

#---------------------------------------------------------------
#this audio says "jnt perak"
jnt2 = wave.open("jnt-perak.wav", "r")
jnt2_soundwave = jnt2.readframes(-1)

jnt2_slow = wave.open("jnt-perak-slowed.wav", "r")
jnt2_soundwave_slow = jnt2_slow.readframes(-1)

# # this is to show just how big the array is 
# jnt_signal = np.frombuffer(jnt_soundwave, dtype='int16')
# # print(jnt_signal[:10])

# jnt_framerate = jnt.getframerate() #frame rate
# print(jnt_framerate)

def dtw(s, t):
    n, m = len(s), len(t)
    dtw_matrix = np.zeros((n+1, m+1))
    for i in range(n+1):
        for j in range(m+1):
            dtw_matrix[i, j] = np.inf
    dtw_matrix[0, 0] = 0
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            cost = abs(s[i-1] - t[j-1])
            # take last min from a square box
            last_min = np.min([dtw_matrix[i-1, j], dtw_matrix[i, j-1], dtw_matrix[i-1, j-1]])
            dtw_matrix[i, j] = cost + last_min
    return dtw_matrix

print("\nmemohon maaf vs memohon maaf (slowed):")
print(dtw(jnt_soundwave[:10], jnt_soundwave_slow[:10]))

print("\n\njnt perak vs jnt perak (slowed):")
print(dtw(jnt2_soundwave[:10], jnt2_soundwave_slow[:10]))

print("\n\nmemohon maaf vs jnt perak:")
print(dtw(jnt_soundwave[:10], jnt2_soundwave[:10]))