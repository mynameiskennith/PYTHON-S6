from PIL import Image

i = Image.open('image.png')
i.thumbnail((100,100))
i.show()