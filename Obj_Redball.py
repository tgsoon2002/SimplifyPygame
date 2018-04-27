from BaseObject import BaseObject


class Obj_Player(BaseObject):

    def Start(self):
        # set the sprite for the object
        self.SetSrpite("redBall.png")
        # scale down the size of object.
        self.offSet = 0
        print(self.rect)
        # self.RotatteObject(29)

    def update(self):
        self.offSet += 0.1
        self.RotatteObject(self.offSet)
        print(self.offSet)
        self.mainScreen.blit(self.sprite, (self.rect[0], self.rect[1]))
