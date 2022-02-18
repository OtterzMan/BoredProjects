import time
import click
import os
import random

from random import shuffle

game1 = ("J:\Games\Steam Library\steamapps\common\Crab Game\Crab Game.exe")
game2 = ("J:\Games\Steam Library\steamapps\common\Detroit Become Human\DetroitBecomeHuman.exe")
game3 = ("J:\Games\Steam Library\steamapps\common\Grand Theft Auto V\GTA5.exe")
game4 = ("J:\Games\Steam Library\steamapps\common\HITMAN2\Launcher.exe")
game5 = ("J:\Games\Steam Library\steamapps\common\Keep Talking and Nobody Explodes\ktane.exe")

print("Hi, today we are going to be starting some games")

output = input("Pick a number between 1-5:")
output = int(output)
time.sleep(3)

if output == 1:
    time.sleep(3)
    os.startfile(game1)


elif output == 2:
    time.sleep(3)
    os.startfile(game2)

elif output == 3:
    time.sleep(3)
    os.startfile(game3)

elif output == 4:
    time.sleep(3)
    os.startfile(game4)

elif output == 5:
    time.sleep(3)
    os.startfile(game5)
