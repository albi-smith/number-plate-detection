
import os

def list_images(directory):
    return [f for f in os.listdir(directory) if f.endswith(('.jpg', '.png'))]
