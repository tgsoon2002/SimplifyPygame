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

    def update(self):
        (self.rect[0], self.rect[1]) = MOUSE_EVENT[MOUSE_POSITION]
        self.mainScreen.blit(self.sprite, (self.rect[0], self.rect[1]))

        if MOUSE_EVENT[MOUSE_LEFT_BUTTON]:
            print(MOUSE_EVENT[MOUSE_POSITION])
        if KEYBOARD[pygame.K_a]:
            print("Press A")
