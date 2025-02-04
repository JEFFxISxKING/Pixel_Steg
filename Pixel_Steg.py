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
    if offset > width:
        row = offset // width
        offset = offset % width
    
    #Starting pixel
    pix = offset
    i=0

    #print(height, width, _)
    #print(pixels)
    #print(pixels[0,offset])    

    for y in range(row,height):
        for x in range(pix, int(width), interval):
            # Get the current pixel
            #r, g, b = pixels[y, x]

            if i >= len(msg):
                break
            # Update the pixel with modified values
            if msg[i] == "0":
                pixels[y, x] = [210, 200, 190] #210, 200, 190 = 0
            elif msg[i] == "1":
                pixels[y, x] = [210, 200, 191] #191 = 1
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
start_image = 'Mantis.jpg'
msg = "This is just some example text so you can try to reverse engineer this code"
offset = 43210
interval = 987

# '#' is the sentinel
msg = toBinString(msg) + "#"

newIMG = encodeImage(start_image, msg, offset, interval)

save_image(newIMG, 'Find_Me_Test.png')
