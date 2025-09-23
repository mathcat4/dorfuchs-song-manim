from helpers import *
from refrain1 import BaseSketch


class MainSketch(BaseSketch):
    def construct(self):
        self.construct_scene(shift=True, mObjs={0: mn.Square(2, color=mn.BLACK)})
