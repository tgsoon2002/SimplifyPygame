import pygame
import Obj_Player
import globalData
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)

quit_attempt = False
clock = pygame.time.Clock()

# This will help get image from the current folder, just by call the file name with extension.


def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image
# =================================


class BaseObject:
    # this is teh base Object class, contain Start and Update function.
    # Update function will be call every frame.
    # Start will be setup so when object be created, it will be called once.
    x = 0
    y = 0
    sprite = ""

    def __init__(self):
        x = 0
        y = 0

    def Start(self):
        pass

    def Update(self):
        pass

# =================================


class Obj_Player(BaseObject):
    # This is test class, with player moving up.and display a sprite for the player.
    def __init__(self):
        pass

    def Start(self):
        pass

    def Update(self, deltaTime):
        self.x = self.x+1 * deltaTime
        if self.x > 250:
            self.x = 250
        # print(self.x)
        print(deltaTime)
        pygame.draw.rect(screen, globalData.BLUE, pygame.Rect(x, y, 60, 60))


player = Obj_Player()
listObject = [player]
while quit_attempt != True:
    pressed_keys = pygame.key.get_pressed()
    # Event filtering
    filtered_events = []
    for event in pygame.event.get():
        quit_attempt = False
        if event.type == pygame.QUIT:
            quit_attempt = True
        elif event.type == pygame.KEYDOWN:
            pass

    dt = clock.tick(30)
    for obj in listObject:
        obj.Update(dt)

    pygame.display.flip()
