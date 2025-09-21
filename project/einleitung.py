import manim as mn
import numpy as np

mn.config.background_color = mn.WHITE

class MainSketch(mn.Scene):
    def construct(self):
        ax = mn.Axes(x_range = [0, 10, 1]).set_color(mn.BLACK)

        self.add(ax)