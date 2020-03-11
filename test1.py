from PIL import Image
from PIL import ImageFilter
im = Image.open('6f84425d7947721dfdbc30b6e9c96ebb.jpg')
om = im.filter(ImageFilter.CONTOUR)
om.save('birdnestContour.jpg')
