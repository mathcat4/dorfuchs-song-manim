import manim as mn
import numpy as np

mn.config.background_color = mn.WHITE

class MainSketch(mn.Scene):
    def construct(self):
        # Number line

        number_line = mn.NumberLine(x_range = [0, 10, 1], include_numbers = True, color = mn.BLACK).shift(mn.DOWN)
        for num in number_line.numbers:
            num.set_color(mn.BLACK)

        self.add(number_line)

        num_a = 1.5
        num_b = 8.5

        # Draw a and b

        dot_a = mn.Dot(number_line.n2p(num_a), color=mn.RED)
        label_a = mn.MathTex("a", color = mn.BLACK).next_to(dot_a, mn.UP)

        dot_b = mn.Dot(number_line.n2p(num_b), color=mn.DARK_BLUE)
        label_b = mn.MathTex("b", color = mn.BLACK).next_to(dot_b, mn.UP)

        self.play(mn.Create(dot_a), mn.Write(label_a))
        self.play(mn.Create(dot_b), mn.Write(label_b))

        # Draw moving mean Dot

        dot_mean = mn.Dot(number_line.n2p((num_a + num_b)/2), color=mn.ORANGE)
        label_mean = mn.MathTex("M", color = mn.ORANGE).next_to(dot_mean, mn.UP)
        label_mean.add_updater(lambda label: label.next_to(dot_mean, mn.UP))

        self.play(mn.FadeIn(dot_mean), mn.FadeIn(label_mean))
        self.play(dot_mean.animate.move_to(number_line.n2p(0.2 * num_a + 0.8 * num_b)))
        self.play(dot_mean.animate.move_to(number_line.n2p(0.8 * num_a + 0.2 * num_b)))
        self.play(dot_mean.animate.move_to(number_line.n2p((num_a + num_b)/2)))
        self.wait(1)

        label_mean.clear_updaters()

        # Four mean dots

        dot_am = mn.Dot(number_line.n2p((num_a + num_b)/2), color=mn.ORANGE)
        label_am = mn.MathTex("AM", color = mn.ORANGE).scale(0.75).next_to(dot_mean, mn.UP)

        dot_gm = mn.Dot(number_line.n2p((num_a * num_b)**0.5), color=mn.GREEN_D)
        label_gm = mn.MathTex("GM", color = mn.GREEN_D).scale(0.75).next_to(dot_gm, mn.UP).align_to(label_am, mn.UP)

        dot_qm = mn.Dot(number_line.n2p(((num_a**2 + num_b**2)/2)**0.5), color=mn.BLUE_D)
        label_qm = mn.MathTex("QM", color = mn.BLUE_D).scale(0.75).next_to(dot_qm, mn.UP).align_to(label_am, mn.UP)

        dot_hm = mn.Dot(number_line.n2p((2 * num_a * num_b)/(num_a + num_b)), color=mn.PURPLE_D)
        label_hm = mn.MathTex("HM", color = mn.PURPLE_D).scale(0.75).next_to(dot_hm, mn.UP).align_to(label_am, mn.UP)

        # Mean descriptions
        desc_am = mn.Text("AM: Arithmetische Mittel", color=mn.ORANGE)
        desc_gm = mn.Text("GM: Geometrische Mittel", color=mn.GREEN_D)
        desc_qm = mn.Text("QM: Quadratische Mittel", color=mn.BLUE_D)
        desc_hm = mn.Text("HM: Harmonische Mittel", color=mn.PURPLE_D)

        group_desc = mn.VGroup(desc_am, desc_gm, desc_qm, desc_hm).arrange_in_grid(rows = 2, cols = 2, buff = 2)
        group_desc.scale(0.5).shift(2 * mn.UP)
        
        self.play(mn.Transform(dot_mean, dot_am), mn.Transform(label_mean, label_am), mn.Write(desc_am))
        self.wait(1)
        self.play(mn.FadeIn(dot_gm), mn.FadeIn(label_gm), mn.Write(desc_gm))
        self.wait(1)
        self.play(mn.FadeIn(dot_qm), mn.FadeIn(label_qm), mn.Write(desc_qm))
        self.wait(1)
        self.play(mn.FadeIn(dot_hm), mn.FadeIn(label_hm), mn.Write(desc_hm))

        self.wait(3)
        