from cell_automat import Automat
from effect_maker import EffectMaker
import laws
import numpy as np

def light() :
    screen = np.zeros((400, 400))
    screen[1, 100] = 1
    screen[200:203, 0:200] = 10
    screen[200:203, 203:254] = 10
    screen[200:203, 256:400] = 10
    auto = Automat(screen)
    auto.render(laws.bactery, 24)
if __name__ == "__main__" :
    light()