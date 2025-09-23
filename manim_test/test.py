import manim as mn

class AnimateSquareToCircle(mn.Scene):
    def construct(self):
        circle = mn.Circle()
        circle.set_fill(mn.PINK, opacity=0.5)

        square = mn.Square()
        square.set_fill(mn.BLUE, opacity=0.8)
        square.rotate(mn.PI/4)
        square.next_to(circle, mn.LEFT, buff=0.5)
        

        self.play(mn.Create(square))
        self.play(mn.Transform(square, circle))
        self.play(mn.FadeOut(square))

class TransformCycle(mn.Scene):
    def construct(self):
        a = mn.Circle()
        t1 = mn.Square()
        t2 = mn.Triangle()
        self.add(a)
        self.wait()
        for t in [t1,t2]:
            self.play(mn.Transform(a,t))


class LatexTest(mn.Scene):
    mn.config.background_color = mn.WHITE
    def construct(self):
        a = mn.MathTex(r"\underbrace{\frac{a + b}{2}}_{AM}", tex_to_color_map={"AM": mn.ORANGE}, color = mn.BLACK)
        self.add(a)