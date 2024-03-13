import wave
import array
from PIL import Image, ImageDraw, ImageFont


output_path = "flag.jpg"

def image_create(path):
    #adding flag to image

    image = Image.open(image_path)
    image = image.resize((576,384))
    draw = ImageDraw.Draw(image)

    print(image.size)

    font = ImageFont.truetype("./font/StoryChoiceSansSerif-B9v5.ttf", size=20)
    text = "pearl{pearls_gleam_in_the_ocean's_embrace}"
    position = (50,50)

    text_color = (255,255,255)
    print(image.size)
    draw.text(position, text, font=font, fill=text_color)
    
    image.save(output_path)

def make_sound(output_file, arr):
    #make audio files from the r,b,b vlaues

    binary_seq = list(arr)
    audio_sample = array.array('b', [int(bit) * 127 for bit in binary_seq])
    
    sample_width = 1
    frame_rate = 26460
    duration = 5
        
    with wave.open(output_file, 'w') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(sample_width)
        wf.setframerate(frame_rate)
        # print(audio_sample.tobytes())
        wf.writeframes(audio_sample.tobytes())




image_path = "./sample.jpg"
image_create(image_path)

image = Image.open(output_path)

image_data = list(image.getdata())
print(len(image_data))

r_8_final = []
g_8_final = []
b_8_final = []

for (r,g,b) in image_data:
    r_8 = format(r, '08b')
    b_8 = format(b, '08b')
    g_8 = format(g, '08b')

    for i in range(8):
        r_8_final.append(r_8[i])
        b_8_final.append(b_8[i])
        g_8_final.append(g_8[i])


red_file = "Raine.wav"
green_file = "Gideon.wav"
blue_file = "Beryl.wav"

make_sound(red_file,r_8_final)
make_sound(green_file,g_8_final)
make_sound(blue_file, b_8_final)

