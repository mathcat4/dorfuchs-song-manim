import manim as mn
import numpy as np

mn.config.background_color = mn.WHITE

class MainSketch(mn.Scene):
    def construct(self):
        # Number line

        number_line = mn.NumberLine(x_range = [0, 10, 1], include_numbers = True, color = mn.BLACK)
        for num in number_line.numbers:
            num.set_color(mn.BLACK)

        self.add(number_line)

        num_a = 1.5
        num_b = 8.5

        # Draw a and b

        dot_a = mn.Dot(number_line.n2p(num_a), color=mn.DARK_BLUE)
        label_a = mn.MathTex("a", color = mn.DARK_BLUE).next_to(dot_a, mn.UP)

        dot_b = mn.Dot(number_line.n2p(num_b), color=mn.DARK_BLUE)
        label_b = mn.MathTex("b", color = mn.DARK_BLUE).next_to(dot_b, mn.UP)

        self.play(mn.Create(dot_a), mn.Write(label_a))
        self.play(mn.Create(dot_b), mn.Write(label_b))

        # Draw moving mean Dot

        dot_mean = mn.Dot(number_line.n2p((num_a + num_b)/2), color=mn.RED)
        label_mean = mn.MathTex("M", color = mn.RED).next_to(dot_mean, mn.UP)
        label_mean.add_updater(lambda label: label.next_to(dot_mean, mn.UP))

        self.play(mn.FadeIn(dot_mean), mn.FadeIn(label_mean))
        self.play(dot_mean.animate.move_to(number_line.n2p(0.2 * num_a + 0.8 * num_b)))
        self.play(dot_mean.animate.move_to(number_line.n2p(0.8 * num_a + 0.2 * num_b)))
        self.play(dot_mean.animate.move_to(number_line.n2p((num_a + num_b)/2)))
        self.wait(1)

        label_mean.clear_updaters()

        # Draw all four means

        dot_am = mn.Dot(number_line.n2p((num_a + num_b)/2), color=mn.ORANGE)
        label_am = mn.MathTex("AM", color = mn.ORANGE).scale(0.75).next_to(dot_mean, mn.UP)

        dot_gm = mn.Dot(number_line.n2p((num_a * num_b)**0.5), color=mn.ORANGE)
        label_gm = mn.MathTex("GM", color = mn.ORANGE).scale(0.75).next_to(dot_gm, mn.UP).align_to(label_am, mn.UP)

        dot_qm = mn.Dot(number_line.n2p(((num_a**2 + num_b**2)/2)**0.5), color=mn.ORANGE)
        label_qm = mn.MathTex("QM", color = mn.ORANGE).scale(0.75).next_to(dot_qm, mn.UP).align_to(label_am, mn.UP)

        dot_hm = mn.Dot(number_line.n2p((2 * num_a * num_b)/(num_a + num_b)), color=mn.ORANGE)
        label_hm = mn.MathTex("HM", color = mn.ORANGE).scale(0.75).next_to(dot_hm, mn.UP).align_to(label_am, mn.UP)
        
        self.play(mn.Transform(dot_mean, dot_am), mn.Transform(label_mean, label_am))
        self.wait(1)
        self.play(mn.FadeIn(dot_gm), mn.FadeIn(label_gm))
        self.wait(1)
        self.play(mn.FadeIn(dot_qm), mn.FadeIn(label_qm))
        self.wait(1)
        self.play(mn.FadeIn(dot_hm), mn.FadeIn(label_hm))

        self.wait(3)
        