import PIL
from PIL import Image
PIL.Image.MAX_IMAGE_PIXELS =None
img = Image.open('IMAGE YOU WANT TO RESIZE')

img_resize = img.resize((img.width // 4, img.height // 4)) #This time reduced to 1/4
img_resize.save('NEW IMAGE NAME')
