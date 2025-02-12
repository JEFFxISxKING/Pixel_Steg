from PIL import Image
import numpy as np

def save_image(img, output_path):
    """Save the image to a specified path."""
    img.save(output_path)
    print(f"Image saved to {output_path}")


def encodeImage(image_path, message, offset, interval):
    # Open the image and convert to RGB
    img = Image.open(image_path)
    img = img.convert('RGB')

    #Save image as array
    pixels = np.array(img)

    # Get the total number of pixels in the image
    height, width, _ = pixels.shape


    #make sure starting pixel is within range
    row = offset // width
    if offset > width:
        offset = offset % width
    
    
    
    #Starting pixel
    pix = offset
    i=0

    #print(height, width, _)
    #print(pixels)
    #print(pixels[0,offset])    

    for y in range(row,height):
        for x in range(pix, int(width), interval):

            if i >= len(msg):
                break

            # Get the current pixel
            r, g, b = pixels[y, x]
            
            # Update the pixel with modified values
            if msg[i] == "0":
                pixels[y, x] = [r, g, 190] #210, 200, 190 = 0
            elif msg[i] == "1":
                pixels[y, x] = [r, g, 191] #191 = 1
            elif msg[i] == "#":
                pixels[y, x] = [255, 0, 0]
            else:
                print("error")
            i += 1
                
        #reset the x value
        pix = x-width      

    output = Image.fromarray(pixels)
    return(output)

def toBinString(msg):
    binary_list = []
    newStr = ""
     
    for char in msg:
        binary_list.append(bin(ord(char))[2:].zfill(8))
        
    return ''.join(binary_list)

#Start
start_image = 'Test_Image.jpg'
msg = "This is what I would hide in a message"
offset = 111
interval = 111

# '#' is the sentinel
msg = toBinString(msg) + "#"

#print(msg)
newIMG = encodeImage(start_image, msg, offset, interval)

save_image(newIMG, 'Output.png')
