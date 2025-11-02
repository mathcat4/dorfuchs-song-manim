from helpers import *


def construct_scene(
    scene: mn.Scene,
    ext_objs: mn.VGroup | None = None,
    mObjsFocus: dict[int, mn.VGroup] | None = None,
):
    """
    Variable animation for refrains 1 to 5.
    External objects can be passed to `ext_objs`.
    Objects to be focused can be passed along with its iteration-index as a dictionary to `mObjsFocus`.
    """

    if mObjsFocus is None:
        mObjsFocus = {}

    # Equation and Relation objects

    eq_QM = mn.MathTex(r"\sqrt{\frac{a^2+b^2}{2}}", color=TXTCOL)
    eq_AM = mn.MathTex(r"\frac{a+b}{2}", color=TXTCOL)
    eq_GM = mn.MathTex(r"\sqrt{ab}", color=TXTCOL)
    eq_HM = mn.MathTex(r"\frac{2}{\frac{1}{a} + \frac{1}{b}}", color=TXTCOL)

    rel_QM_AM = mn.MathTex(r"\geq", color=TXTCOL)
    rel_AM_GM = mn.MathTex(r"\geq", color=TXTCOL)
    rel_GM_HM = mn.MathTex(r"\geq", color=TXTCOL)

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

    final_text = mn.Text("Das sind die Mittelungleichungen!", color=TXTCOL).scale(0.75)
    final_text.next_to(group_eq, mn.DOWN, buff=1.2)

    # Conditionally add either the external objects or the helper text
    if isinstance(ext_objs, mn.VGroup):
        ext_objs.shift(1.2 * mn.DOWN)

        group_eq.shift(2 * mn.UP)
        group_text.shift(2 * mn.UP)

        scene.add(ext_objs)
    else:
        scene.add(
            mn.MathTex(
                r"\text{Für alle } a,b \in \mathbb{R}^+ \text{ gilt:}", color=TXTCOL
            ).shift(2.5 * mn.UP)
        )

    # Focus and scale animations

    fade_in = []

    for iteration, group_anim in enumerate([group_QM_AM, group_AM_GM, group_GM_HM]):
        # Fade out last iteration and fade in current iteration

        fade_out = [mobj for mobj in [*group_eq, *group_text] if mobj not in group_anim]

        fade_out_anims = [
            mobj.animate.set_opacity(0.3) for mobj in fade_out if mobj not in fade_in
        ]
        fade_in_anims = [
            mobj.animate.set_opacity(1) for mobj in fade_in if mobj not in fade_out
        ]

        scene.play(*(fade_out_anims + fade_in_anims), run_time=1)

        wait_duration = 1
        if iteration in mObjsFocus:
            assert isinstance(ext_objs, mn.VGroup)
            focus_obj = mObjsFocus[iteration]

            # this is so hacky I hate that it works
            # update: i acutally forgor why this works so don't touch it and it won't break
            fade_group = ext_objs.copy().remove(focus_obj)
            scene.add(fade_group)
            scene.remove(ext_objs)

            # Focus in external objects
            scene.play(
                group_anim.animate.scale(1.25),
                fade_group.animate.fade(0.8),
                focus_obj.animate.scale(
                    1.25, about_point=focus_obj.get_center_of_mass()
                ),
                rate_func=mn.rate_functions.rush_from,
                run_time=1,
            )

            scene.wait(wait_duration)

            # Focus out external objects
            if iteration != 2:
                scene.play(
                    group_anim.animate.scale(0.8),
                    fade_group.animate.fade(
                        -4
                    ),  # fu manim I had to solve a fricking equation to figure out this value
                    focus_obj.animate.scale(
                        0.8, about_point=focus_obj.get_center_of_mass()
                    ),
                    rate_func=mn.rate_functions.rush_into,
                    run_time=1,
                )
                scene.add(ext_objs)
                scene.remove(fade_group)
            else:
                # Final iteration anims
                scene.play(
                    group_anim.animate.scale(0.8),
                    focus_obj.animate.scale(
                        0.8, about_point=focus_obj.get_center_of_mass()
                    ).fade(1),
                    mn.FadeOut(fade_group),
                    rate_func=mn.rate_functions.rush_into,
                    run_time=1,
                )

        else:
            # Focus in external objects
            scene.play(
                group_anim.animate.scale(1.25),
                rate_func=mn.rate_functions.rush_from,
                run_time=1,
            )

            scene.wait(wait_duration)

            # Focus out external objects
            if iteration != 2 or not isinstance(ext_objs, mn.VGroup):
                scene.play(
                    group_anim.animate.scale(0.8),
                    rate_func=mn.rate_functions.rush_into,
                    run_time=1,
                )
            else:
                # Final iteration anims
                scene.play(
                    group_anim.animate.scale(0.8),
                    mn.FadeOut(ext_objs),
                    rate_func=mn.rate_functions.rush_into,
                    run_time=1,
                )

        fade_in = fade_out.copy()

    # Play final animations

    for mobj in fade_in:
        mobj.set_opacity(1)

    all_final_anims = [mn.Write(final_text)]

    if isinstance(ext_objs, mn.VGroup):
        scene.remove(ext_objs)
        all_final_anims += [
            group_eq.animate.shift(2 * mn.DOWN),
            group_text.animate.shift(2 * mn.DOWN),
        ]

    scene.play(*all_final_anims, run_time=3.3)


class MainSketch(mn.Scene):
    def construct(self):
        START = int(Audio.refrain1 * 1000)
        STOP = int(Audio.strophe1 * 1000)
        if os.path.exists(Audio.path):
            self.renderer.file_writer.add_audio_segment(Audio.song[START:STOP])

        # construct_scene(self)

        geo = Geo()
        construct_scene(
            self,
            ext_objs=mn.VGroup(
                geo.construction,
                geo.N,
                geo.labelN,
                geo.X,
                geo.labelX,
                geo.G,
                geo.labelG,
                geo.QMAMDreieck,
                geo.AMGMDreieck,
                geo.GMHMDreieck,
            ),
            mObjsFocus={
                0: geo.QMAMDreieck,
                1: geo.AMGMDreieck,
                2: geo.GMHMDreieck,
            },
        )
