#Imports
import pygame as pg
import os

def LoadAll(): #Loads all sprites from Sprites directory
    AppPath = os.path.dirname(__file__)
    Path = f'{AppPath}\\Sprites\\'
    Paths = []
    for path in os.listdir(Path):
        Paths.append(path)
    Sprites = str()
    for Sprite in Sprites:
        Sprites = os.listdir(path=Paths[Sprite])
        pg.image.load(Sprite)
LoadAll()