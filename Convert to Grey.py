from PIL import Image
import numpy as np

def save_image(img, output_path):
    """Save the image to a specified path."""
    img.save(output_path)
    print(f"Image saved to {output_path}")


image_path = 'JEFF_01.png'

img = Image.open(image_path)
img = img.convert('L')
img = img.convert('RGB')
save_image(img, 'New.png')
