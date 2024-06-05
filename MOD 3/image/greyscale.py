from PIL import Image

i = Image.open('image.png')
ig = i.convert('L')
ig.show()