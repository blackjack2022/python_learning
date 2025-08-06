# background.jpg

from PIL import Image


image = Image.open('tempfile/background.jpg')
image_w,image_h = image.size
print(image.size)
image.rotate(45).show()
image.crop((0, 0, image_w, image_h)).save('tempfile/image.jpg')
