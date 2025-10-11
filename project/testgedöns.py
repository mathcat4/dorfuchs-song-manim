from manim import *


class MainSketch(Scene):
    def construct(self):
        tr = MathTex(r"a^2 + b^2 \over 2")
        tr2 = MathTex(r"{ \sqrt{a^2 + b^2 \over 2} }")
        #self.play(FadeIn(tr[0]))
        self.play(FadeIn(tr))
        self.play(TransformMatchingShapes(tr,tr2))

        #self.play(FadeIn(tr2[1], tr2[3], tr2[4], tr2[5], tr2[6], tr2[7], tr2[8], tr2[9]))
        self.wait
        self.play(FadeIn(tr))
        #self.play(TransformMatchingShapes(tr[0],tr2[0]),TransformMatchingShapes(tr[1],tr2[1]), TransformMatchingShapes(tr[2],tr2[2]
