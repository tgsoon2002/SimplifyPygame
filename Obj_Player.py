import sys
sys.path.insert(0, 'Core')
from BaseObject import BaseObject
from globalData import *


class Obj_Player(BaseObject):

    def Start(self):

        # set the sprite for the object
        self.SetSrpite("ball.png")
        # scale down the size of object.
        print(self.rect)
        # self.sprite = pygame.transform.rotate(self.sprite, 45)
        # self.RotatteObject(45)
        self.offSet = 0
        self.Counter = 0

    def Update(self):
        self.Counter += DELTATIME
        print(self.Counter)
        self.MoveObjectTo(MOUSE_EVENT[MOUSE_POSITION]
                          [0], MOUSE_EVENT[MOUSE_POSITION][1])
        if MOUSE_EVENT[MOUSE_LEFT_BUTTON]:
            print(MOUSE_EVENT[MOUSE_POSITION])
        if KEYBOARD[pygame.K_a]:
            print("Press A")
        self.offSet += 1
        if self.offSet > 360:
            self.offSet = 0
        # self.RotateObject(self.offSet)
        # pygame.draw.rect(self.sprite, RED, [5, 5, 25, 25])
