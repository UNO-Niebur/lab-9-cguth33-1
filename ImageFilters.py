# Lab 9 - Image Processing
# Name: Carter
# Date: April 5, 2026
# Assignment: Lab 9

from PIL import Image

def swapGreenBlue(img):
    """Swap the green and blue values for every pixel in the image."""
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            red, green, blue = pixels[x, y]
            # Swap green and blue positions
            pixels[x, y] = (red, blue, green)

    img.save("swapGB.png")


def darken(img, amount):
    """Darken the image by reducing RGB values by the given amount."""
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            red, green, blue = pixels[x, y]
            
            # Reduce values and ensure they do not go below 0
            new_red = max(0, red - amount)
            new_green = max(0, green - amount)
            new_blue = max(0, blue - amount)
            
            pixels[x, y] = (new_red, new_green, new_blue)

    img.save("darkImg.png")


def bwFilter(img):
    """Example function: converts image to grayscale."""
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            red, green, blue = pixels[x, y]
            avg = (red + green + blue) // 3
            pixels[x, y] = (avg, avg, avg)

    img.save("bwImg.png")


def main():
    # Open the image file
    # Ensure "durango.png" is in your current folder
    myImg = Image.open("durango.png")

    # 1. Run the swap filter
    # We reload the image each time so the filters apply to the original
    swapGreenBlue(myImg)
    
    # 2. Run the darken filter
    myImg = Image.open("durango.png")
    darken(myImg, 20)

    # Example (already completed in starter code)
    # myImg = Image.open("durango.png")
    # bwFilter(myImg)


if __name__ == "__main__":
    main()