from helpers import *


def construct_scene(scene: mn.Scene, mObjs=None):
    if mObjs is None:
        mObjs = {}

    shift = len(mObjs) != 0

    # Equation and Relation objects

    eq_QM = mn.MathTex(r"\sqrt{\frac{a^2+b^2}{2}}", color=TXTCOL)
    rel_QM_AM = mn.MathTex(r"\geq", color=TXTCOL)

    eq_AM = mn.MathTex(r"\frac{a+b}{2}", color=TXTCOL)
    rel_AM_GM = mn.MathTex(r"\geq", color=TXTCOL)

    eq_GM = mn.MathTex(r"\sqrt{ab}", color=TXTCOL)
    rel_GM_HM = mn.MathTex(r"\geq", color=TXTCOL)

    eq_HM = mn.MathTex(r"\frac{2}{\frac{1}{a} + \frac{1}{b}}", color=TXTCOL)

    group_eq = mn.VGroup(
        eq_QM, rel_QM_AM, eq_AM, rel_AM_GM, eq_GM, rel_GM_HM, eq_HM
    ).arrange(mn.RIGHT, buff=0.5)

    # Text objects

    text_QM = mn.Text("QM", color=QMCOL).scale(0.75)
    text_QM.move_to(eq_QM).align_to(group_eq.get_top() + mn.UP, mn.UP)
    group_QM = mn.VGroup(eq_QM, text_QM)

    text_AM = mn.Text("AM", color=AMCOL).scale(0.75)
    text_AM.move_to(eq_AM).align_to(group_eq.get_top() + mn.UP, mn.UP)
    group_AM = mn.VGroup(eq_AM, text_AM)

    text_GM = mn.Text("GM", color=GMCOL).scale(0.75)
    text_GM.move_to(eq_GM).align_to(group_eq.get_top() + mn.UP, mn.UP)
    group_GM = mn.VGroup(eq_GM, text_GM)

    text_HM = mn.Text("HM", color=HMCOL).scale(0.75)
    text_HM.move_to(eq_HM).align_to(group_eq.get_top() + mn.UP, mn.UP)
    group_HM = mn.VGroup(eq_HM, text_HM)

    group_text = mn.VGroup(text_QM, text_AM, text_GM, text_HM)

    group_QM_AM = mn.VGroup(*group_QM, rel_QM_AM, *group_AM)
    group_AM_GM = mn.VGroup(*group_AM, rel_AM_GM, *group_GM)
    group_GM_HM = mn.VGroup(*group_GM, rel_GM_HM, *group_HM)

    scene.add(group_eq, group_text)
    if shift:
        scene.play(group_eq.animate.shift(mn.UP), group_text.animate.shift(mn.UP))

    # Fade and scale animations

    fade_in = []
    iteration = 0

    for group_anim in [group_QM_AM, group_AM_GM, group_GM_HM]:
        fade_out = [mobj for mobj in [*group_eq, *group_text] if mobj not in group_anim]

        fade_out_anims = [
            mobj.animate.set_opacity(0.3) for mobj in fade_out if mobj not in fade_in
        ]
        fade_in_anims = [
            mobj.animate.set_opacity(1) for mobj in fade_in if mobj not in fade_out
        ]

        scene.play(*(fade_out_anims + fade_in_anims))

        wiggle_duration = 1
        if iteration in mObjs.keys():
            wiggle_obj = mObjs[iteration].copy()
            wiggle_obj.next_to(group_eq, mn.DOWN, buff=1)
            scene.play(
                mn.FadeIn(wiggle_obj),
                group_anim.animate.scale(1.5),
                rate_func=mn.rate_functions.rush_from,
            )
            scene.play(mn.Wiggle(wiggle_obj), run_time=wiggle_duration)
            scene.play(
                mn.FadeOut(wiggle_obj),
                group_anim.animate.scale(2 / 3),
                rate_func=mn.rate_functions.rush_into,
            )
        else:
            scene.play(
                group_anim.animate.scale(1.5), rate_func=mn.rate_functions.rush_from
            )
            scene.wait(wiggle_duration)
            scene.play(
                group_anim.animate.scale(2 / 3),
                rate_func=mn.rate_functions.rush_into,
            )

        fade_in = fade_out.copy()

        # scene.wait(1)
        iteration += 1

    # Final text

    for mobj in fade_in:
        mobj.set_opacity(1)

    final_text = mn.Text("Das sind die Mittelungleichungen!", color=TXTCOL).scale(0.75)
    final_text.next_to(group_eq, mn.DOWN, buff=2)

    all_final_anims = [mn.Write(final_text)]

    if shift:
        all_final_anims += [
            group_eq.animate.shift(mn.DOWN),
            group_text.animate.shift(mn.DOWN),
        ]

    scene.play(*all_final_anims, run_time=3)


class MainSketch(mn.Scene):
    def construct(self):
        construct_scene(self)

        # construct_scene(
        #     self, mObjs={0: QMAMDreieck, 1: AMGMDreieck, 2: GMHMDreieck}
        # )
