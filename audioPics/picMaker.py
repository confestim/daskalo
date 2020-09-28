from PIL import Image
import random
import soundfile as sf
import pyloudnorm as pyln

def pictureMake():
  data, rate = sf.read("input.wav") # load audio (with shape (samples, channels))
  meter = pyln.Meter(rate) # create BS.1770 meter
  loudness = meter.integrated_loudness(data) # measure loudness
  loudness = int(loudness)
  if loudness < 0:
    loudness = -loudness
  print(loudness)

  random_number = random.randint(0,16777215)
  hex_number = str(hex(random_number))
  hex_number ='#'+ hex_number[2:]

  canvas = Image.new("RGB", (300,300), hex_number)
  width, height = canvas.size
  pixels = canvas.load()

  for x in range(height):
      randomCol1 = random.randint(0,255)
      randomCol2 = random.randint(0,255)
      randomCol3 = random.randint(0,255)
      for y in range(width):
          canvas.putpixel((x,y),(randomCol1, randomCol2, randomCol3))
          canvas.putpixel((x,x),(randomCol1, randomCol2, randomCol3))
  canvas.save("output.png", "PNG")

pictureMake()
