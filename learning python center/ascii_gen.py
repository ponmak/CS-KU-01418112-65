# ascii image generator 

import PIL.Image

ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]

# resize image
def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height/width
    new_height = int(aspect_ratio * new_width)
    new_image = image.resize((new_width, new_height))
    new_image = new_image.convert('L') # convert image to grayscale
    return new_image

# Generator function: convert image to ascii
def ascii_image():
    # input: path to image
    path = input("Enter the path to the image file : \n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "Unable to find image ")

    resized_image  = resize_image(image) # resize image



if __name__ == '__main__':
    ascii_image()
