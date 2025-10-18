from helpers import *


def construct_scene(scene: mn.Scene, reverse=False):

    # Multi variable means
    eq_QM = mn.MathTex(
        r"\frac{ \sqrt{ {a_1}^2 + {a_2}^2 + \dots + {a_n}^2 } } { n }",
        color=QMCOL,
    )
    eq_AM = mn.MathTex(r"\frac{ a_1 + a_2 + \dots + a_n } { n }", color=AMCOL)
    eq_GM = mn.MathTex(r"\sqrt[n]{ a_1 a_2 \ldots a_n }", color=GMCOL)
    eq_HM = mn.MathTex(
        r"\frac{ n }{ \frac{1}{a_1} + \frac{1}{a_2} + \dots + \frac{1}{a_n} }",
        color=HMCOL,
    )

    group_eq = mn.VGroup(eq_QM, eq_AM, eq_HM, eq_GM).arrange_in_grid(
        rows=2, cols=2, buff=4
    )

    # Relations

    rel_QM_AM = mn.MathTex(r"\geq", color=TXTCOL).move_to(
        (eq_QM.get_right() + eq_AM.get_left()) / 2
    )
    rel_AM_GM = mn.MathTex(r"\leq", color=TXTCOL).move_to(
        (eq_AM.get_bottom() + eq_GM.get_top()) / 2
    )
    rel_AM_GM.rotate(mn.PI / 2)
    rel_GM_HM = mn.MathTex(r"\leq", color=TXTCOL).move_to(
        (eq_GM.get_left() + eq_HM.get_right()) / 2
    )

    group_rel = mn.VGroup(rel_QM_AM, rel_AM_GM, rel_GM_HM)

    scene.add(group_eq, group_rel)

    # Text objects

    text_QM = mn.MathTex(r"\textbf{QM } (p = 2)", color=QMCOL).scale(0.75)
    text_QM.move_to(eq_QM).align_to(
        mn.VGroup(eq_QM, eq_AM).get_bottom() + mn.DOWN, mn.DOWN
    )
    group_QM = mn.VGroup(eq_QM, text_QM)

    text_AM = mn.MathTex(r"\textbf{AM } (p = 1)", color=AMCOL).scale(0.75)
    text_AM.move_to(eq_AM).align_to(
        mn.VGroup(eq_QM, eq_AM).get_bottom() + mn.DOWN, mn.DOWN
    )
    group_AM = mn.VGroup(eq_AM, text_AM)

    text_GM = mn.MathTex(r"\textbf{GM } (\textstyle p \to 0)", color=GMCOL).scale(0.75)
    text_GM.move_to(eq_GM).align_to(mn.VGroup(eq_GM, eq_HM).get_top() + mn.UP, mn.UP)
    group_GM = mn.VGroup(eq_GM, text_GM)

    text_HM = mn.MathTex(r"\textbf{HM } (p = -1)", color=HMCOL).scale(0.75)
    text_HM.move_to(eq_HM).align_to(mn.VGroup(eq_GM, eq_HM).get_top() + mn.UP, mn.UP)
    group_HM = mn.VGroup(eq_HM, text_HM)

    group_text = mn.VGroup(text_QM, text_AM, text_GM, text_HM)
    scene.add(group_text)

    group_QM_AM = mn.VGroup(*group_QM, rel_QM_AM, *group_AM)
    group_AM_GM = mn.VGroup(*group_AM, rel_AM_GM, *group_GM)
    group_GM_HM = mn.VGroup(*group_GM, rel_GM_HM, *group_HM)

    # Fade and scale animations

    fade_in = []
    group_anims = [group_QM_AM, group_AM_GM, group_GM_HM]
    if reverse:
        group_anims = group_anims[::-1]

    for group_anim in group_anims:
        fade_out = [
            mobj
            for mobj in [*group_eq, *group_rel, *group_text]
            if mobj not in group_anim
        ]

        fade_out_anims = [
            mobj.animate.set_opacity(0.3) for mobj in fade_out if mobj not in fade_in
        ]
        fade_in_anims = [
            mobj.animate.set_opacity(1) for mobj in fade_in if mobj not in fade_out
        ]

        scene.play(*(fade_out_anims + fade_in_anims))
        scene.play(mn.Circumscribe(group_anim, color=TXTCOL), run_time=3)

        fade_in = fade_out.copy()

    for mobj in fade_in:
        mobj.set_opacity(1)

    # Final text

    final_text = mn.Text("Das sind die Mittelungleichungen!", color=TXTCOL).scale(0.6)
    scene.play(mn.Write(final_text), run_time=3.3)


class MainSketch(mn.Scene):
    def construct(self):
        START = int(Audio.refrain6 * 1000)
        STOP = int(Audio.refrain7 * 1000)
        self.renderer.file_writer.add_audio_segment(Audio.song[START:STOP])
        construct_scene(self)

        # construct_scene(self, reverse=True)
