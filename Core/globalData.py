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

COLLIDERTYPE_RECT = 0
COLLIDERTYPE_CIRCLE = 1
COLLIDERTYPE_POLYGON = 0


def cameraMove(xcod,ycod):
    for obj in listObject:
        obj.self.rect[0] - xcod
        obj.self.rect[1] - ycod

def NewObject(newObject):
    listObject.append(newObject)

def DestroyObject(newObject):
    for obj in listObject:
        if newObject == obj:
            listObject.remove(newObject)
            del newObject
            return True
    return False
    

def FindObjects(objectName):
    result = []
    for obj in listObject:
        if obj.__class__.__name__ == objectName:
            result.append(obj)
    return result

def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image

def ColCheckRectToRect(obj1,obj2):
    return (obj1.rect[0] < obj2.rect[0] + obj2.rect[2] and
            obj1.rect[0] + obj1.rect[2] > obj2.rect[0] and
        obj1.rect[1] < obj2.rect[1] + obj2.rect[3] and
            obj1.rect[1] + obj1.rect[3] > obj2.rect[1])
    

def CompareObject(obj, className):
    return(obj.__class__.__name__ == className)
