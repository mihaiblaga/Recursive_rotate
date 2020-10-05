from PIL import Image
im = Image.open("cat.jpg")
imload = im.load()

for j in range(0,511):
    for i in range(0,511):
        