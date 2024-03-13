# beautiful song
## Solution
We are given a `.wav` file and the prompt says that `I hate frequencies which are multiple of 50`.

To get the frequency components of the audio, we apply `fft` and analyse the frequencies which are multiple of `50`, we can see that those are the `charcodes`, joining those we get the flag.

```
from scipy.fft import rfft
from scipy.io import wavfile

fs, data = wavfile.read("new_hit_song.wav", "r")

fourier = abs(rfft(data))

for i in range(32):
    print(chr(round(fourier[i * 50])), end = "")
```

## Flag
`pearl{fft5_ar3_art_aren't_7h3y?}`