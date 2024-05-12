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
        n = 0
        while True:
            if n != 0 :
                previous_frame = self.matrix.copy()
                self.matrix = law(previous_frame)
                if np.array_equal(previous_frame, self.matrix) :
                    break
            for i in range(self.a) :
                for j in range(self.b) :
                    surface.set_at((i, j), self.colors[self.matrix[i][j]])
            pg.display.flip()
            clock.tick(fps)
            n+=1

    def get_video(self, law, name, duration, frames, FPS) :
        images = []
        breaker = frames+1
        for n in range(frames+1) :
            if n != 0 :
                previous_frame = self.matrix.copy()
                self.matrix = law(previous_frame)
                if np.array_equal(previous_frame, self.matrix) :
                    breaker = n
                    break
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
            if n == breaker :
                break
            os.remove('img_' + str(n) + '.jpg')