import ffmpeg
import os
import Imagegen
import requests

import os

from dotenv import load_dotenv, dotenv_values

newpath = r'Image Generation\clips' 
if not os.path.exists(newpath):
    os.makedirs(newpath)
"""


for i in range(1, 6):
    Imagegen.img_gen(prompt_="Ram Navami greeting card", fname=f"{newpath}\\img{i}")
    print(f"{i} / 5 images done")
"""

(
    ffmpeg
    .input(f'{newpath}\\*.png', pattern_type='glob', framerate=25)
    .output(f'movie.mp4')
    #.run()
)