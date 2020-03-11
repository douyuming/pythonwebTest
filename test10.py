
from PIL import Image
from PIL import ImageChops
im1=Image.open('1.jpg')
im2=Image.open('6f84425d7947721dfdbc30b6e9c96ebb.jpg')
m=ImageChops.screen(im1,im2)
m.show()
m.save('5.jpg')
