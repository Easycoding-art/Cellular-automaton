from PIL import Image
import numpy as np
from cell_automat.cell_automat import Automat
from moviepy.editor import *
import os

class EffectMaker :
    def __init__(self, file_name) :
        self.video_file = file_name
        clip = VideoFileClip(self.video_file)
        clip.save_frame("frame.jpg", t = clip.duration - 1)
        im = Image.open("frame.jpg") # Can be many different formats
        pix = im.load()
        s, h = im.size  # Get the width and hight of the image for iterating over
        self.matrix = np.zeros((s, h))
        self.colors = [(255,255,255), (0,0,0), (0,0,255), (0,255,0), (255,0,0), (255,100,10),
                (255,255,0), (0,255,170), (115,0,0), (180,255,100), (255,100,180), (240,0,255),
                (127,127,127), (255,0,230), (100,40,0), (0,50,0), (0,0,100), (210,150,75),
                (255,200,0), (255,255,100), (0,255,255), (200,200,200), (50,50,50), (230,220,170),
                (200,190,140), (235,245,255)]
        
        for i in range(s) :
            for j in range(h) :
                for n in range(len(self.colors)) :
                    if ((pix[i, j][0] >= self.colors[n][0] - 50 and pix[i, j][0] <= self.colors[n][0] + 50) and
                        (pix[i, j][1] >= self.colors[n][1] - 50 and pix[i, j][1] <= self.colors[n][1] + 50) and
                        (pix[i, j][2] >= self.colors[n][2] - 50 and pix[i, j][2] <= self.colors[n][2] + 50)) :
                        self.matrix[i, j] = n
                        break
        os.remove("frame.jpg")
        
    def video(self, video_name, law, duration, frames, FPS) :
        automat = Automat(self.matrix)
        automat.get_video(law, video_name + "_effect", duration, frames, FPS)
        clip1 = VideoFileClip(self.video_file)
        clip2 = VideoFileClip(video_name + "_effect" + ".mp4")
        final_clip = concatenate_videoclips([clip1,clip2])
        final_clip.write_videofile(video_name + ".mp4")
        os.remove(video_name + "_effect" + ".mp4")