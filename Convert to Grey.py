from PIL import Image

def save_image(img, output_path):
    """Save the image to a specified path."""
    img.save(output_path)
    print(f"Image saved to {output_path}")

image_path = 'JEFF_01.png' #Get input image

img = Image.open(image_path) #open image
img = img.convert('L') #convert to grey ("RGB" gives RGB)
save_image(img, 'New.png') #Save image
