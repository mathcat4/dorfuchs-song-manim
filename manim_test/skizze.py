import manim as mn
import numpy as np

def circle_point(radius, diameter_point):
    height = (radius**2 - diameter_point[0]**2)**0.5
    return np.asarray([0, height, 0]) + diameter_point

class ProofSketch(mn.Scene):
    def construct(self):
        radius = 3

        point_A = np.asarray([-radius, 0, 0])
        point_B = np.asarray([radius, 0, 0])

        point_C = np.asarray([1, 0, 0])

        dot_A = mn.Dot(color=mn.WHITE).move_to(point_A).scale(0.5)
        self.add(dot_A)

        dot_B = mn.Dot(color=mn.WHITE).move_to(point_B).scale(0.5)
        self.add(dot_B)

        semicircle = mn.ArcBetweenPoints(start=point_B, end=point_A, angle=mn.PI)
        self.add(semicircle)

        diameter = mn.Line(start=point_A, end=point_B)
        self.add(diameter)

        dot_C = mn.Dot(color=mn.RED).move_to(point_C).scale(0.5)
        label_C = mn.MathTex("C").next_to(dot_C, 0.5*mn.DOWN).scale(0.5).set_color(mn.RED)
        group_C = mn.VGroup(dot_C, label_C)
        self.add(group_C)

        dot_D = mn.always_redraw(lambda: mn.Dot(color=mn.BLUE).move_to(circle_point(radius, dot_C.get_center())))
        self.add(dot_D)

        self.play(group_C.animate.shift(2*mn.LEFT))
        self.play(group_C.animate.shift(2*mn.RIGHT))


        self.wait(2)