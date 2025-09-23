import manim as mn

mn.config.background_color = mn.WHITE

class mObjs:
    # Equation and Relation objects
            
    eq_QM = mn.MathTex(r"\sqrt{\frac{a^2+b^2}{2}}", color=mn.BLACK)
    rel_QM_AM = mn.MathTex(r"\geq", color = mn.BLACK)

    eq_AM = mn.MathTex(r"\frac{a+b}{2}", color = mn.BLACK)
    rel_AM_GM = mn.MathTex(r"\geq", color = mn.BLACK)

    eq_GM = mn.MathTex(r"\sqrt{ab}", color = mn.BLACK)
    rel_GM_HM = mn.MathTex(r"\geq", color = mn.BLACK)

    eq_HM = mn.MathTex(r"\frac{2}{\frac{1}{a} + \frac{1}{b}}", color = mn.BLACK)

    group_eq = mn.VGroup(eq_QM, rel_QM_AM, eq_AM, rel_AM_GM, eq_GM, rel_GM_HM, eq_HM).arrange(mn.RIGHT, buff=0.5)

    # Text Objects

    text_QM = mn.Text("QM", color = mn.BLUE_D).scale(0.75)
    text_QM.move_to(eq_QM).align_to(group_eq.get_top() + mn.UP, mn.UP)
    group_QM = mn.VGroup(eq_QM, text_QM)

    text_AM = mn.Text("AM", color = mn.ORANGE).scale(0.75)
    text_AM.move_to(eq_AM).align_to(group_eq.get_top() + mn.UP, mn.UP)
    group_AM = mn.VGroup(eq_AM, text_AM)

    text_GM = mn.Text("GM", color = mn.GREEN_D).scale(0.75)
    text_GM.move_to(eq_GM).align_to(group_eq.get_top() + mn.UP, mn.UP)
    group_GM = mn.VGroup(eq_GM, text_GM)

    text_HM = mn.Text("HM", color = mn.PURPLE_D).scale(0.75)
    text_HM.move_to(eq_HM).align_to(group_eq.get_top() + mn.UP, mn.UP)
    group_HM = mn.VGroup(eq_HM, text_HM)

    group_text = mn.VGroup(text_QM, text_AM, text_GM, text_HM)

    group_QM_AM = mn.VGroup(*group_QM, rel_QM_AM, *group_AM)
    group_AM_GM = mn.VGroup(*group_AM, rel_AM_GM, *group_GM)
    group_GM_HM = mn.VGroup(*group_GM, rel_GM_HM, *group_HM)

    # Final text

    final_text = mn.Text("Das sind die Mittelungleichungen!", color=mn.BLACK).scale(0.75)
    final_text.next_to(group_eq, mn.DOWN, buff = 1)

class MainSketch(mn.Scene):
    def construct(self):
        # Equation and text objects

        self.add(mObjs.group_eq, mObjs.group_text)

        # Fade and scale animations

        fade_in = []

        for group_anim in [mObjs.group_QM_AM, mObjs.group_AM_GM, mObjs.group_GM_HM]:
            fade_out = [mobj for mobj in [*mObjs.group_eq, *mObjs.group_text] if mobj not in group_anim]

            fade_out_anims = [mobj.animate.set_opacity(0.3) for mobj in fade_out if mobj not in fade_in]
            fade_in_anims = [mobj.animate.set_opacity(1) for mobj in fade_in if mobj not in fade_out]
            
            self.play(*(fade_out_anims + fade_in_anims))

            self.play(group_anim.animate.scale(1.5), rate_func=mn.rate_functions.rush_from)
            self.wait(0.5)
            self.play(group_anim.animate.scale(1/1.5), rate_func=mn.rate_functions.rush_into)

            fade_in = fade_out.copy()

            # self.wait(1)
        
        self.play(*[mobj.animate.set_opacity(1) for mobj in fade_in])

        # Final text

        self.play(mn.Write(mObjs.final_text), run_time = 2)

        self.wait(3)
