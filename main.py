from PIL import Image

image = Image.open("monro.jpg")
rgb_image = image.convert("RGB")

red, green, blue = image.split()

red_left = red.crop((40, 0, image.width, image.height)) 
red_middle = red.crop((20, 0, image.width - 20, image.height))
blue_right = blue.crop((0, 0, image.width - 40, image.height))
blue_middle = blue.crop((20, 0, image.width - 20, image.height))
green = green.crop((20, 0, image.width - 20, image.height))

red = Image.blend(red_left, red_middle, 0.5)
blue = Image.blend(blue_right, blue_middle, 0.5)
new_image = Image.merge("RGB", (red, green,blue))
new_image.thumbnail((80,80))
new_image.save('newMonro.jpg')