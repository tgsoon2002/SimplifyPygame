# My module
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PI = 3.141592653
import os
import pygame
import math
_image_library = {}


MOUSE_POSITION = 0
MOUSE_LEFT_BUTTON = 1
MOUSE_RIGHT_BUTTON = 2
MOUSE_MIDDLE_BUTTON = 3

listObject = []
dt = 0
gameTime = [0, 0]

keys = [0] * 256
mouse = [(0, 0), 0, 0, 0, 0, 0, 0]  # (pos, b1,b2,b3,b4,b5,b6)
GameInput = [mouse, dt, keys]

MOUSE_EVENT = mouse
DELTATIME = gameTime[0]
KEYBOARD = keys

COLLIDERTYPE_RECT = 0
COLLIDERTYPE_CIRCLE = 1
COLLIDERTYPE_POLYGON = 0


def cameraMove(xcod, ycod):
    """ THis function move every object by x and y"""
    for obj in listObject:
        obj.MoveObjectBy(xcod, ycod)


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


def ColCheckRectToRect(obj1, obj2):
    return (obj1.x < obj2.x + obj2.rect[2] and
            obj1.x + obj1.rect[2] > obj2.x and
            obj1.y < obj2.y + obj2.rect[3] and
            obj1.y + obj1.rect[3] > obj2.y)


def ColCheckRectToCircle(rectObj, circObj):
    reBR = (rectObj.x-rectObj.rect[2]/2, rectObj.y-rectObj.rect[3])
    reTR = (rectObj.x-rectObj.rect[2]/2, rectObj.y+rectObj.rect[3])
    reTL = (rectObj.x+rectObj.rect[2]/2, rectObj.y+rectObj.rect[3])
    reBL = (rectObj.x+rectObj.rect[2]/2, rectObj.y-rectObj.rect[3])
    cCenter = (circObj.x, circObj.y)

    circObj.colliderRadius
    lengthx = abs(rectObj.x - circObj.x)
    lengthy = abs(rectObj.y - circObj.y)

    # if any corner is inside the circle
    if S_Mag(reBR, cCenter) <= circObj.colliderRadius or S_Mag(reTR, cCenter) <= circObj.colliderRadius or S_Mag(reTL, cCenter) <= circObj.colliderRadius or S_Mag(reBL, cCenter) <= circObj.colliderRadius:
        return True
    # else if circle cut any line. by finding the vector and circle match.
    #  if that point is between line then we got cut the line

    # return (rectObj.lengthx < obj2.colliderRadius + obj2.rect[2] and
    #         obj1.rect[0] + obj1.rect[2] > obj2.rect[0] and
    #         obj1.rect[1] < obj2.rect[1] + obj2.rect[3] and
    #         obj1.rect[1] + obj1.rect[3] > obj2.rect[1])


def CompareObject(obj, className):
    return(obj.__class__.__name__ == className)


def S_Mag(point1, point2):
    lengthx = abs(point1.x - point2.x)
    lengthy = abs(point1.y - point2.y)
    return math.sqrt(lengthx ^ 2 + lengthy ^ 2)
