import pygame
import os


class spritesheet(object):
    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename)
        except pygame.error as message:
            print('Unable to load spritesheet image:' + filename)
            raise SystemExit + message
    # Load a specific image from a specific rectangle

    def image_at(self, rectangle, colorkey=None):
        "crop and return image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size)  # create empty surface
        # draw the surface with rect size.
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
    # Load a whole bunch of images and return them as a list

    def get_image(self):
        "Get the image of the file, no crop"
        return self.sheet

    def spritesheet(self, rects, col=1, row=1,  colorkey=None):
        "Loads multiple images, supply a list of coordinates"
        "else create sprite sheet with row and column."
        if len(rects) == 0:
            width = self.sheet.width / col
            height = self.sheet.height / row
            rects = []
            for x in range(col):
                for y in range(row):
                    rects.append([width * x, height * y, width, height])
        return [self.image_at(rect, colorkey) for rect in rects]
    # Load a whole strip of images

    def load_strip(self, rect, image_count, colorkey=None):
        "Loads a strip of images and returns them as a list"
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.spritesheet(tups, image_count, 1, colorkey)
