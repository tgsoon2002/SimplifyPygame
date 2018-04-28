
from globalData import *
import Obj_Redball
import Obj_Player

def GameClass(screen):
    player = Obj_Player.Obj_Player(screen)
    ball = Obj_Redball.Obj_Redball(screen, 150, 150)
    NewObject(player)
    NewObject(ball)
