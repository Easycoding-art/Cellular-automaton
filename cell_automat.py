import pygame as pg
import numpy as np
from moviepy.editor import *
from PIL import Image
import os

class Automat :
    def __init__(self, matrix) :
        self.RES = matrix.shape
        self.a, self.b = matrix.shape
        self.matrix = matrix
        self.colors = [(255,255,255), (0,0,0), (0,0,255), (0,255,0), (255,0,0), (255,100,10),
                (255,255,0), (0,255,170), (115,0,0), (180,255,100), (255,100,180), (240,0,255),
                (127,127,127), (255,0,230), (100,40,0), (0,50,0), (0,0,100), (210,150,75),
                (255,200,0), (255,255,100), (0,255,255), (200,200,200), (50,50,50), (230,220,170),
                (200,190,140), (235,245,255)]
    def render(self, law, fps) :
        pg.init()
        surface = pg.display.set_mode(self.RES)
        clock = pg.time.Clock()
        generation = 0
        while True:
            if generation != 0 :
                self.matrix = law(self.matrix)
            for i in range(self.a) :
                for j in range(self.b) :
                    if self.matrix[i][j] == 0 :
                        surface.set_at((i, j), pg.Color('white'))
                    elif self.matrix[i][j] == 1 :
                        surface.set_at((i, j), pg.Color('black'))
                    elif self.matrix[i][j] == 2 :
                        surface.set_at((i, j), pg.Color('blue'))
                    elif self.matrix[i][j] == 3 :
                        surface.set_at((i, j), pg.Color('green'))
                    elif self.matrix[i][j] == 4 :
                        surface.set_at((i, j), pg.Color('red'))
                    elif self.matrix[i][j] == 5 :
                        surface.set_at((i, j), pg.Color('orange'))
                    elif self.matrix[i][j] == 6 :
                        surface.set_at((i, j), pg.Color('yellow'))
                    elif self.matrix[i][j] == 7 :
                        surface.set_at((i, j), pg.Color('blue_green'))
                    elif self.matrix[i][j] == 8 :
                        surface.set_at((i, j), pg.Color('marroon'))
                    elif self.matrix[i][j] == 9 :
                        surface.set_at((i, j), pg.Color('lime'))
                    elif self.matrix[i][j] == 10 :
                        surface.set_at((i, j), pg.Color('pink'))
                    elif self.matrix[i][j] == 11 :
                        surface.set_at((i, j), pg.Color('purple'))
                    elif self.matrix[i][j] == 12 :
                        surface.set_at((i, j), pg.Color('gray'))
                    elif self.matrix[i][j] == 13 :
                        surface.set_at((i, j), pg.Color('magenta'))
                    elif self.matrix[i][j] == 14 :
                        surface.set_at((i, j), pg.Color('brown'))
                    elif self.matrix[i][j] == 15 :
                        surface.set_at((i, j), pg.Color('forest_green '))
                    elif self.matrix[i][j] == 16 :
                        surface.set_at((i, j), pg.Color('navy_blue'))
                    elif self.matrix[i][j] == 17 :
                        surface.set_at((i, j), pg.Color('rust'))
                    elif self.matrix[i][j] == 18 :
                        surface.set_at((i, j), pg.Color('dandilion_yellow'))
                    elif self.matrix[i][j] == 19 :
                        surface.set_at((i, j), pg.Color('highlighter'))
                    elif self.matrix[i][j] == 20 :
                        surface.set_at((i, j), pg.Color('sky_blue'))
                    elif self.matrix[i][j] == 21 :
                        surface.set_at((i, j), pg.Color('light_gray'))
                    elif self.matrix[i][j] == 22 :
                        surface.set_at((i, j), pg.Color('dark_gray'))
                    elif self.matrix[i][j] == 23 :
                        surface.set_at((i, j), pg.Color('tan'))
                    elif self.matrix[i][j] == 24 :
                        surface.set_at((i, j), pg.Color('coffee_brown'))
                    elif self.matrix[i][j] == 25 :
                        surface.set_at((i, j), pg.Color('moon_glow'))
            generation+=1
            pg.display.flip()
            clock.tick(fps)

    def get_video(self, law, name, duration, frames, FPS) :
        images = []
        for n in range(frames+1) :
            if n != 0 :
                self.matrix = law(self.matrix)
            img  = Image.new( mode = "RGB", size = (self.a, self.b) )
            pix = img.load()
            for i in range(self.a) :
                for j in range(self.b) :
                    pix[i, j] = self.colors[int(self.matrix[i,j])]
            img.save('img_' + str(n) + '.jpg')
            images.append(ImageClip('img_' + str(n) + '.jpg').set_duration(duration))
        final_clip = concatenate_videoclips(images, method="compose")
        final_clip.write_videofile(name + ".mp4", fps= FPS)
        for n in range(frames+1) :
            os.remove('img_' + str(n) + '.jpg')