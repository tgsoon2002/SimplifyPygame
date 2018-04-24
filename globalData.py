# My module
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PI = 3.141592653
import os
import pygame
_image_library = {}


MOUSE_POSITION = 0
MOUSE_LEFT_BUTTON = 1
MOUSE_RIGHT_BUTTON = 2
MOUSE_MIDDLE_BUTTON = 3

listObject = []
dt = 0
keys = [0] * 256
mouse = [(0, 0), 0, 0, 0, 0, 0, 0]  # (pos, b1,b2,b3,b4,b5,b6)
GameInput = [mouse, dt, keys]

MOUSE_EVENT = GameInput[0]
DELTATIME = GameInput[1]
KEYBOARD = GameInput[2]


def NewObject(newObject):
    listObject.append(newObject)


def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image
