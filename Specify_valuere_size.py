from PIL import Image

img = Image.open('IMAGE YOU WANT TO RESIZE')
img_resize_lanczos = img.resize((500,600 ), Image.LANCZOS)
img_resize_lanczos.save('NEW IMAGE NAME')
