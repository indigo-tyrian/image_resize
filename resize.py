# from PIL import Image

# img = Image.open('SK-C-1768.jpg')

# img_resize = img.resize((256, 256))
# img_resize.save('data/dst/lena_pillow_resize_nearest.jpg')

# img_resize_lanczos = img.resize((256, 256), Image.LANCZOS)
# img_resize_lanczos.save('data/dst/lena_pillow_resize_lanczos.jpg')

# img_resize = img.resize((img.width // 2, img.height // 2))
# img_resize_lanczos.save('data/dst/lena_pillow_resize_half.jpg')

# img_resize = img.resize((img.width // 2, img.height // 2))
# img_resize_lanczos.save('SK-C-1768/lena_pillow_resize_half.jpg')



import requests
url='https://ymori.com/books/python2nen/test1.html'
response=requests.get(url)
response.encodig='utf-8'
print(response.text)