from PIL import Image

im = Image.open('image.jpg')
im.save('image.png')

i = Image.open('image.png')
i.show()
