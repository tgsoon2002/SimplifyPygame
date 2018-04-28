# SimplifyPygame
# Author : Kien Nguyen
This project is inspired by pixelpad.

To start the game. start main.py file.

Structure of the project will have
*main.py*, *game.py*, and *Core* folder, which contain some important script. 

# To Create Class
Class is where we put the code, we can think class as blueprint or list of instruction that object will use to build.
You should create a new object that inherit from BaseObject. example, We create a Obj_Player class/file

>from BaseObject import BaseObject
>from globalData import *
>
>class Obj_Player(BaseObject):
>
>    def Start(self):
>        pass
>    def Update(self):
>        pass

# To Create Object
Each object should have 2 function, Start and Update. Start function will be call when this object being created.
and update function will be called every game loop. To create object base on the file. We need to create that object and add to the system to keep track. Example we creat Obj_Player and add to the system. we should to create it in the *game.py* file

>from globalData import *
>import Obj_Player
>
>def GameClass(screen):
>    player = Obj_Player.Obj_Player(screen)
>    NewObject(player)

We also can specify the size of the object, how big it gonna be.Example we create the same object again with width 150 and height 150

>    player = Obj_Player.Obj_Player(screen, 150, 150)

# Sprite and Move
Now we know how to create object, we need to add picture and know how to move it.
To create Sprite, we need sprite to be store in *Sprite* folder. then in the start function we call *SetSprite* method
This function will create ues sprite that we want and can be used to draw on the screen. This also create *rect* to store data 
of location and size of our sprite. It is array with 4 element. first two element is x and y position of our object; third and fourth is width and height of our object. this is zero-base array.
# -- Notice, Sprite can create a strip of sprite to use. I currently not enable and will implemetn in future we so can do animation. 
## SetSrpite(string : file name) -> void

>   self.SetSrpite("Ball.png")
>   self.rect[0] = 100
>   self.rect[1] = 200

# Rotate
Sprite can be rotate by call *RotateObject* function and pass in angle
## RotateObject(number:angle) -> void

>   self.RotateObject(self.offSet)


# Collision
For collision, we can simply pass in the name of the object and system will find and check if any object in the system is collide with the object and return a list of object with that class name.
# -- Notice, right now only rect collision is being used. I will add in circle collision and polygon collision later --
## Collision_Check(string : className ) -> [object] 

>   self.Collision_Check("Obj_Enemy")

#Play music
To play music, we use the pygame function built in. Remember to keep sound file in the *Sound* folder to keep trac. pygame mixer is already easy to use like so I keepit the same. Play this one time. to loop keep it -1.


>   pygame.mixer.music.load('Sound/testMusic.mp3')
>   pygame.mixer.music.play(0)
>   pygame.mixer.music.queue('next_song.mp3')
>   pygame.mixer.music.stop()