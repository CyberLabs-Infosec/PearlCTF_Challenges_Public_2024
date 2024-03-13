from scipy.fft import rfft, irfft
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt

SAMPLE_RATE = 22050
DURATION = 18

def generateSine(freq, duration, sample_rate):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    y = irfft(freq, sample_rate * duration)
    return x, y

FLAG = "pearl{fft5_ar3_art_aren't_7h3y?}"
FREQS = np.zeros((len(FLAG) * 50))

all_freqs = []

for i, c in enumerate(FLAG):
    freq_copy = FREQS.copy()
    freq_copy[i * 50] = ord(c)
    all_freqs.append(freq_copy)

x, y = generateSine(all_freqs[0], DURATION, SAMPLE_RATE)

for f in all_freqs[1:]:
    _, y_ = generateSine(f, DURATION, SAMPLE_RATE)
    y += y_

fs, data = wavfile.read("song.wav", "r")
channel_1 = data.T[0]
normalize = [(ele / 2**8.) * 2 - 1 for ele in channel_1]

song_freqs = rfft(normalize)

for i in range(len(FLAG)):
    song_freqs[i * 50] = 0

new_song = irfft(song_freqs)

new_song += y

wavfile.write("new_hit_song.wav", SAMPLE_RATE, new_song)