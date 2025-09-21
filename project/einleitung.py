import manim as mn
import numpy as np

mn.config.background_color = mn.WHITE

class MainSketch(mn.Scene):
    def construct(self):
        number_line = mn.NumberLine(x_range = [0, 10, 1], include_numbers = True, color = mn.BLACK)

        self.add(number_line)