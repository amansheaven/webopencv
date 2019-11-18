from PIL import Image


class webopencv(object):
    def __init__(self):
        pass

    def process(self, img):
        return img.transpose(Image.FLIP_LEFT_RIGHT)
