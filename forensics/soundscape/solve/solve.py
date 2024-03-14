"""
Based on the prompt, it appears that we need to create an image using sound files. We have three sound files named Raine, Beryl, and Gideon, which contain values for the R (Red), B (Blue), and G (Green) channels respectively. However, the values are not directly given; instead, they are encoded as binary data within the audio frames, with frames containing either 127 or 0. By analyzing the frames, we can extract the binary data and use it to construct the image.

Each sequence of 8 bits from Raine.wav corresponds to the Red value of one pixel, while the sequences from Beryl.wav and Gideon.wav correspond to the Blue and Green values respectively. However, to construct the image, we need to know its dimensions. By examining the total number of pixels (221,184), we can deduce that the dimensions are 576x384.

With this information, we can proceed to create the image by assigning the pixel values accordingly. Once the image is constructed, we can obtain the flag. 

flag : pearl{pearls_gleam_in_the_ocean's_embrace}
"""


import wave 
import array
from PIL import Image


def get_array(filename):
    with wave.open(filename, 'rb') as f:
        total_frame = f.getnframes()
        audio_frames = f.readframes(total_frame)
        audio_data = array.array('b', audio_frames)
        return audio_data

def get_binary(arr):
    val = ''
    for i in arr:
        val += '0' if (i==0 ) else '1'
    return val

def make_tuple():
    r_val = get_binary(get_array(r_file))
    b_val = get_binary(get_array(b_file))
    g_val = get_binary(get_array(g_file))

    pixel = []
    
    for i in range(0,len(r_val),8):
        pixel_tuple = (int(r_val[i:i+8],2),int(g_val[i:i+8],2),int(b_val[i:i+8],2))
        pixel.append(pixel_tuple)

    return pixel
    
def make_image(pixel):
    (wd,ht) = (576,384)
    image = Image.new("RGB", (wd,ht), "black")
    image.putdata(pixel)
    image.save("./flag.jpg")
    image.show()


r_file = "./Raine.wav"
g_file = "./Gideon.wav"	
b_file = "./Beryl.wav"

pixel = make_tuple()
make_image(pixel)
