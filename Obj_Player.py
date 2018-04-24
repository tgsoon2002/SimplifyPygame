from BaseObject import BaseObject
from globalData import *


class Obj_Player(BaseObject):

    def Start(self):
        # set the sprite for the object
        self.sprite = get_image('Sprite/ball.png')
        # scale down the size of object.
        self.sprite = pygame.transform.scale(self.sprite, self.spriteRect)

    def Update(self):
        self.mainScreen.blit(self.sprite, (self.x, self.y))
        self.x = self.x+1
        if MOUSE_EVENT[MOUSE_LEFT_BUTTON]:
            print(MOUSE_EVENT[MOUSE_POSITION])
        if KEYBOARD[pygame.K_a]:
            print("Press A")
