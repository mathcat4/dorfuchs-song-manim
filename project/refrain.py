import manim as mn
import numpy as np

mn.config.background_color = mn.WHITE

class MainSketch(mn.Scene):
    def construct(self):
        eq_QM = mn.MathTex("\\sqrt{\\frac{a^2+b^2}{2}}").set_color(mn.BLACK)
        rel_QM_AM = mn.MathTex("\\geq").set_color(mn.BLACK).next_to(eq_QM, 2 * mn.RIGHT)

        eq_AM = mn.MathTex("\\frac{a+b}{2}").set_color(mn.BLACK).next_to(rel_QM_AM, 2 * mn.RIGHT)
        rel_AM_GM = mn.MathTex("\\geq").set_color(mn.BLACK).next_to(eq_AM, 2 * mn.RIGHT)

        eq_GM = mn.MathTex("\\sqrt{ab}").set_color(mn.BLACK).next_to(rel_AM_GM, 2 * mn.RIGHT)
        rel_GM_HM = mn.MathTex("\\geq").set_color(mn.BLACK).next_to(eq_GM, 2 * mn.RIGHT)

        eq_HM = mn.MathTex("\\frac{2ab}{a+b}").set_color(mn.BLACK).next_to(rel_GM_HM, 2 * mn.RIGHT)

        group_eq = mn.VGroup(eq_QM, rel_QM_AM, eq_AM, rel_AM_GM, eq_GM, rel_GM_HM, eq_HM).center()

        text_QM = mn.Text("QM").set_color(mn.RED).move_to(eq_QM).scale(0.75)
        text_QM.move_to(np.array([eq_QM.get_x(), group_eq.get_top()[1], 0]) + 0.5*mn.UP)
        group_QM = mn.VGroup(eq_QM, text_QM)

        text_AM = mn.Text("AM").set_color(mn.RED).move_to(eq_AM).scale(0.75).shift(mn.UP)
        text_AM.move_to(np.array([eq_AM.get_x(), group_eq.get_top()[1], 0]) + 0.5*mn.UP)
        group_AM = mn.VGroup(eq_AM, text_AM)

        text_GM = mn.Text("GM").set_color(mn.RED).move_to(eq_GM).scale(0.75).shift(mn.UP)
        text_GM.move_to(np.array([eq_GM.get_x(), group_eq.get_top()[1], 0]) + 0.5*mn.UP)
        group_GM = mn.VGroup(eq_GM, text_GM)

        text_HM = mn.Text("HM").set_color(mn.RED).move_to(eq_HM).scale(0.75).shift(mn.UP)
        text_HM.move_to(np.array([eq_HM.get_x(), group_eq.get_top()[1], 0]) + 0.5*mn.UP)
        group_HM = mn.VGroup(eq_HM, text_HM)

        group_text = mn.VGroup(text_QM, text_AM, text_GM, text_HM)

        group_QM_AM = mn.VGroup(*group_QM, rel_QM_AM, *group_AM)
        group_AM_GM = mn.VGroup(*group_AM, rel_AM_GM, *group_GM)
        group_GM_HM = mn.VGroup(*group_GM, rel_GM_HM, *group_HM)

        self.add(group_eq)
        self.add(group_text)

        fade_in_anims = []

        for group_anim in [group_QM_AM, group_AM_GM, group_GM_HM]:
            fade_out_anims = []
            for mobj in [*group_eq, *group_text]:
                if mobj not in group_anim:
                    fade_out_anims.append(mobj.animate.set_opacity(0.3))
            
            self.play(*(fade_out_anims + fade_in_anims))

            self.play(group_anim.animate.scale(1.5))
            self.wait(0.5)
            self.play(group_anim.animate.scale(1/1.5))

            fade_in_anims = [mobj.animate.set_opacity(1) for mobj in [*group_eq, *group_text]]

            self.wait(1)
        
        self.play(*fade_in_anims)

        final_text = mn.Text("Das sind die Mittelungleichungen!").set_color(mn.BLACK).scale(0.75)
        final_text.next_to(group_eq, 3 * mn.DOWN)
        self.play(mn.Create(final_text), run_time=2)

        self.wait(3)
