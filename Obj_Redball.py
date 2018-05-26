import sys
sys.path.insert(0, 'Core')
from BaseObject import BaseObject
from globalData import *


class Obj_Redball(BaseObject):

    def Start(self):
        # set the sprite for the object
        self.SetSrpite("redBall.png")
        # scale down the size of object.
        self.offSet = 0
        print(self.rect)
        self.MoveObjectTo(200, 200)
        self.colliderType = COLLIDERTYPE_CIRCLE
        # self.RotateObject(29)
        self.colliderRadius = 75

    def Update(self):
        self.offSet += 0.1
        self.RotateObject(self.offSet)
