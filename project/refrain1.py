import manim as mn
import numpy as np

mn.config.background_color = mn.WHITE

class MainSketch(mn.Scene):
    def construct(self):
        # Equation and Relation objects

        eq_QM = mn.MathTex(r"\sqrt{\frac{a^2+b^2}{2}}", color=mn.BLACK)
        rel_QM_AM = mn.MathTex(r"\geq", color = mn.BLACK)

        eq_AM = mn.MathTex(r"\frac{a+b}{2}", color = mn.BLACK)
        rel_AM_GM = mn.MathTex(r"\geq", color = mn.BLACK)

        eq_GM = mn.MathTex(r"\sqrt{ab}", color = mn.BLACK)
        rel_GM_HM = mn.MathTex(r"\geq", color = mn.BLACK)

        eq_HM = mn.MathTex(r"\frac{2}{\frac{1}{a} + \frac{1}{b}}", color = mn.BLACK)

        group_eq = mn.VGroup(eq_QM, rel_QM_AM, eq_AM, rel_AM_GM, eq_GM, rel_GM_HM, eq_HM).arrange(mn.RIGHT, buff=0.5)
        self.add(group_eq)
    
        # Text Objects

        text_QM = mn.Text("QM", color = mn.BLUE_D).move_to(eq_QM).scale(0.75)
        text_QM.move_to(eq_QM).align_to(group_eq.get_top() + mn.UP, mn.UP)
        group_QM = mn.VGroup(eq_QM, text_QM)

        text_AM = mn.Text("AM", color = mn.ORANGE).move_to(eq_AM).scale(0.75)
        text_AM.move_to(eq_AM).align_to(group_eq.get_top() + mn.UP, mn.UP)
        group_AM = mn.VGroup(eq_AM, text_AM)

        text_GM = mn.Text("GM", color = mn.GREEN_D).move_to(eq_GM).scale(0.75)
        text_GM.move_to(eq_GM).align_to(group_eq.get_top() + mn.UP, mn.UP)
        group_GM = mn.VGroup(eq_GM, text_GM)

        text_HM = mn.Text("HM", color = mn.PURPLE_D).move_to(eq_HM).scale(0.75)
        text_HM.move_to(eq_HM).align_to(group_eq.get_top() + mn.UP, mn.UP)
        group_HM = mn.VGroup(eq_HM, text_HM)

        group_text = mn.VGroup(text_QM, text_AM, text_GM, text_HM)

        group_QM_AM = mn.VGroup(*group_QM, rel_QM_AM, *group_AM)
        group_AM_GM = mn.VGroup(*group_AM, rel_AM_GM, *group_GM)
        group_GM_HM = mn.VGroup(*group_GM, rel_GM_HM, *group_HM)

        self.add(group_text)

        # Fade and scale animations

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

        # Final Text

        final_text = mn.Text("Das sind die Mittelungleichungen!", color=mn.BLACK).scale(0.75)
        final_text.next_to(group_eq, 3 * mn.DOWN)
        self.play(mn.Write(final_text), run_time=2)

        self.wait(3)
