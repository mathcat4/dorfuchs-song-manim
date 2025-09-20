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