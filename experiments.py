from cell_automat import Automat
from effect_maker import EffectMaker
import laws
import numpy as np

def game() :
    screen = np.zeros((400, 400))
    screen[10:13, 10] = 1
    screen[12, 9] = 1
    screen[11, 8] = 1
    auto = Automat(screen)
    auto.get_video(laws.life, "life", 1, 50, 23)


if __name__ == "__main__" :
    game()