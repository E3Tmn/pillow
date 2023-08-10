from PIL import Image

image = Image.open("monro.jpg")
rgb_image = image.convert("RGB")

red, green, blue = image.split()

coordinates_red = (40, 0, image.width, image.height)
coordinates_green = (20, 0, image.width - 20, image.height)
coordinates_blue = (0, 0, image.width - 40, image.height)

red = red.crop(coordinates_red) 
green = green.crop(coordinates_green)
blue = blue.crop(coordinates_blue)

new_image = Image.merge("RGB", (red, green,blue))
new_image.thumbnail((80,80))
new_image.save('newMonro.jpg')