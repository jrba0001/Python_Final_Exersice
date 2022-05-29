"""
In this section, you will write a Python script named changeImage.py to process the supplier images. You will be using the PIL library to update all images within ~/supplier-data/images directory to the following specifications:

Size: Change image resolution from 3000x2000 to 600x400 pixel
Format: Change image format from .TIFF to .JPEG
Create and open the file using nano editor.
"""
#!/usr/bin/env python3

#Import necessary modules
import os, sys
from PIL import Image

#Declare variables to be used
user = os.getenv('USER') # To get the username from environment variable
image_directory = '/home/{}/supplier-data/images/'.format(user)

for image_name in os.listdir(image_directory):
    if not image_name.startswith('.') and 'tiff' in image_name:
        image_path = image_directory + image_name
        path = os.path.splitext(image_path)[0]
        im = Image.open(image_path)
        new_path = '{}.jpeg'.format(path)
        im.convert('RGB').resize((600, 400)).save(new_path, "JPEG")