from helpers import *


def construct_scene(scene: mn.Scene, debug: bool = False):
    """
    Animation for strophe 2. Konstruktion QM.
    """

    geo = Geo()
    scene.add(geo.construction)
    geo.GanzeSkizze.shift(2 * mn.LEFT)

    tex1 = mn.MathTex(r"QM(a,b) = \sqrt{\frac{a^2+b^2}{2}}", color=QMCOL).shift(
        mn.UP * 3 + 2 * mn.LEFT
    )
    scene.wait(1)
    scene.play(mn.Write(tex1), run_time=2)

    scene.wait(6.27)
    scene.bring_to_back(geo.am2)
    scene.play(mn.FadeIn(geo.am2), mn.FadeIn(geo.N), run_time=1)

    scene.wait(1.88)
    scene.bring_to_back(geo.qm)
    scene.play(mn.Create(geo.qm), run_time=1)
    scene.play(mn.Create(geo.labelN), run_time=1)
    scene.bring_to_back(geo.rightM)
    scene.play(mn.Create(geo.rightM), run_time=1)

    bquestion = mn.Brace(
        geo.qm,
        direction=geo.qm.copy().rotate(mn.PI / 2).get_unit_vector(),
        color=TXTCOL,
    )
    bqtext = bquestion.get_tex("?")
    bqtext.set_color(TXTCOL)
    scene.play(mn.FadeIn(bquestion, bqtext), run_time=0.75)
    scene.play(mn.FadeOut(bquestion, bqtext), run_time=0.75)

    scene.wait(0.5)
    scene.play(mn.Wiggle(geo.QMAMDreieck), run_time=1.7)
    scene.wait(0.5)

    scene.play(mn.FadeOut(tex1, run_time=0.5))

    scene.wait(0.9)
    scene.play(mn.Wiggle(geo.am2, n_wiggles=8, run_time=1.05))

    am2_copy = geo.am2.copy()
    label_rad = (
        mn.MathTex(r"a+b \over 2", color=TXTCOL)
        .scale(0.5)
        .next_to(am2_copy, mn.RIGHT, buff=0.5)
    )
    label_rad_copy = label_rad.copy()
    scene.play(
        mn.Write(label_rad),
        run_time=1,
    )

    term1 = mn.MathTex(r"{{{a+b \over 2}}}", color=TXTCOL).move_to(
        3 * mn.UP + 2 * mn.LEFT
    )

    scene.mobjects.insert(3, am2_copy)
    scene.bring_to_back(geo.rightM, geo.lineMS)
    scene.wait(0.2)
    scene.play(
        mn.Rotate(am2_copy, mn.PI / 2, about_point=tuple(geo.M.get_center())),
        RotatePreserveOrientation(label_rad, mn.PI / 2, about_point=geo.M.get_center()),
        mn.ReplacementTransform(label_rad_copy, term1),
        runtime=1.02,
    )

    scene.bring_to_front(geo.S)
    scene.bring_to_front(geo.M)
    scene.wait(0.2)

    label_rad_2 = (
        mn.MathTex(r"{ a+b \over 2 }", r" - a", color=TXTCOL)
        .scale(0.5)
        .next_to(geo.lineMS, mn.UP, buff=0.5)
    )

    scene.play(
        mn.ReplacementTransform(am2_copy, geo.lineMS.set_color(REDCOL)),
        mn.TransformMatchingShapes(label_rad, label_rad_2[0]),
        mn.FadeIn(label_rad_2[1]),
        run_time=1.2,
    )

    term2 = mn.MathTex(r"{a+b \over 2} - a", color=TXTCOL).move_to(3 * mn.UP + mn.RIGHT)
    scene.play(mn.TransformMatchingShapes(label_rad_2, term2), run_time=0.76)

    term3 = mn.MathTex(r"{{{b-a \over 2}}}", color=TXTCOL).move_to(3 * mn.UP + mn.RIGHT)
    scene.play(
        mn.TransformMatchingShapes(term2, term3),
        run_time=0.5,
    )

    scene.play(mn.Wiggle(geo.lineMS, n_wiggles=8, scale_value=1.5, run_time=1.3))

    # Pure eqution manipulation

    term4 = mn.MathTex(
        r"{{|\overline{SN}|}}{{^2}} {{=}} {{(\kern0pt}}{{{a+b \over 2}}}{{)\kern0pt}}{{^2\kern0pt}} {{+}} {{(}}{{{b-a \over 2}}}{{\right)}}{{\hspace{0pt}^2}} ",
        color=TXTCOL,
    ).move_to(3 * mn.UP + mn.LEFT)
    scene.play(
        mn.TransformMatchingTex(mn.VGroup(term3, term1), term4),
        geo.lineMS.animate.set_color(TXTCOL),
        run_time=1,
    )

    term5 = mn.MathTex(
        r"{{|\overline{SN}|}}{{^2}} {{=}} {  {{(\kern0pt}}a+b{{)\kern0pt}} {{^2\kern0pt}}  {{\over}} {{2^2}} } {{+}} { {{(}}b-a{{)}} {{\hspace{0pt}^2}} {{\over}} {{2^2}} } ",
        color=TXTCOL,
    ).move_to(3 * mn.UP + mn.LEFT)
    scene.wait(0.03)
    scene.play(mn.TransformMatchingTex(term4, term5), run_time=1)

    term6 = mn.MathTex(
        r"{{|\overline{SN}|}}{{^2}} {{=}} {  {{(\kern0pt}}a+b{{)\kern0pt}} {{^2\kern0pt}} {{+}} {{(}}b-a{{)}} {{\hspace{0pt}^2}}  {{\over}} {{2^2}}}",
        color=TXTCOL,
    ).move_to(3 * mn.UP + mn.LEFT)
    scene.wait(0.03)
    scene.play(mn.TransformMatchingTex(term5, term6), run_time=1)

    term7 = mn.MathTex(
        r"{{|\overline{SN}|}}{{^2}} {{=}} {{{a^2}} + 2ab + {{b^2}} {{+}} {{a^2}} - 2ab + {{b^2}} \over {{2^2}}}",
        color=TXTCOL,
        font_size=36,
    ).move_to(3 * mn.UP + mn.LEFT)
    scene.wait(0.03)
    scene.play(mn.TransformMatchingTex(term6, term7), run_time=1)

    term8 = mn.MathTex(
        r"{{|\overline{SN}|}}{{^2}} {{=}} {2{{a^2}} {{+}} 2{{b^2}} {{\over}} {{2^2}}}",
        color=TXTCOL,
    ).move_to(3 * mn.UP + mn.LEFT)
    scene.play(mn.TransformMatchingTex(term7, term8), run_time=1)

    term9 = mn.MathTex(
        r"{{|\overline{SN}|}}{{^2}} {{=}}  { {{a^2}} {{+}} {{b^2}} {{\over}} {{2}} } ",
        color=TXTCOL,
    ).move_to(3 * mn.UP + mn.LEFT)
    scene.play(mn.TransformMatchingTex(term8, term9), run_time=1)

    term10 = mn.MathTex(
        r"{{|\overline{SN}|}} {{=}} {{ \sqrt{ a^2 + b^2 \over 2 } }}",
        color=TXTCOL,
    ).move_to(3 * mn.UP + mn.LEFT)

    scene.play(
        mn.TransformMatchingShapes(term9[0], term10[0]),
        mn.FadeOut(term9[1]),
        mn.TransformMatchingShapes(term9[3], term10[2]),
        mn.FadeIn(term10[4][0:2]),
        mn.TransformMatchingShapes(term9[5:], term10[4][2:]),
        run_time=1,
    )

    term11 = mn.MathTex(
        r"{{|\overline{SN}|}} {{=}} {{ \sqrt{ a^2 + b^2 \over 2 } }} = QM(a,b)",
        color=QMCOL,
    ).shift(3 * mn.UP)

    # Outro Zeugs

    geo2 = Geo()
    triangle = geo2.QMAMDreieck

    group_move = mn.VGroup(geo2.construction, geo2.N, geo2.labelN, triangle)
    group_move.shift(geo.construction.get_center() - geo2.construction.get_center())

    scene.add(group_move)

    for mobj in scene.mobjects:
        if mobj != term11:
            scene.remove(mobj)

    # Hypothenuse Dings und so

    hypoangle = geo2.qm.get_angle()
    kathangle = -geo2.am2.get_angle()

    hypolabel = mn.MathTex(r"\text{Hypothenuse}", color=QMCOL).scale(0.8)
    hypolabel.rotate(hypoangle).move_to(geo2.qm)
    hypolabel.shift(
        np.asarray(
            [
                0.25 * math.cos(mn.PI / 2 + hypoangle),
                0.25 * math.sin(mn.PI / 2 + hypoangle),
                0,
            ]
        )
    )

    kathlabel = mn.MathTex(r"\text{Kathete}", color=AMCOL).scale(0.8)
    kathlabel.rotate(kathangle).move_to(geo2.am2)
    kathlabel.shift(
        np.asarray(
            [
                0.2 * math.cos(mn.PI / 2 + kathangle),
                0.2 * math.sin(mn.PI / 2 + kathangle),
                0,
            ]
        )
    )

    move_dir = (
        Geo().construction.get_center() - geo2.construction.get_center() + 1.2 * mn.DOWN
    )
    fade_out_anims = [
        # Labels shift
        mn.FadeIn(hypolabel),
        mn.FadeIn(kathlabel),
        hypolabel.animate.shift(move_dir),
        kathlabel.animate.shift(move_dir),
        # Other anims
        mn.TransformMatchingTex(term10, term11),
    ]

    for mobj in group_move:
        if mobj == triangle:
            fade_out_anims.append(mobj.animate.shift(move_dir))
        else:
            fade_out_anims.append(mobj.animate.fade(0.8).shift(move_dir))

    scene.play(*fade_out_anims, run_time=1)

    geq = (
        mn.MathTex(r"\geq", color=TXTCOL)
        .scale(0.8)
        .next_to(geo2.N.get_center(), mn.UP, buff=0.5)
    )

    fullineq = (
        mn.MathTex(r"\text{Hypothenuse}", r"\geq", r"\text{Kathete}", color=TXTCOL)
        .scale(0.8)
        .next_to(geo2.N.get_center(), mn.UP, buff=0.5)
    )
    fullineq.move_to(
        fullineq.get_center() + geq.get_center() - fullineq[1].get_center()
    )
    fullineq[0].set_color(QMCOL)
    fullineq[2].set_color(AMCOL)

    scene.wait(1)

    scene.play(
        hypolabel.animate.rotate(-hypoangle).move_to(fullineq[0]),
        kathlabel.animate.rotate(-kathangle).move_to(fullineq[2]),
        mn.FadeIn(geq),
    )

    # Fade out

    if not debug:
        scene.wait(Audio.refrain3 - scene.time - 1)
    else:
        scene.wait(Audio.refrain3 - Audio.strophe2 - scene.time - 1)

    anims = [group_move.animate.scale(FIGURE_SCALE, about_point=mn.ORIGIN)]

    keep_objs = [geo2.construction, geo2.N, geo2.labelN]
    keep_family = set()
    for obj in keep_objs:
        keep_family.update(obj.get_family())

    for mobj in scene.mobjects:
        if mobj in keep_family:
            anims.append(mobj.animate.fade(-4))
        elif mobj != triangle:
            anims.append(mn.FadeOut(mobj))

    scene.play(*anims, run_time=1)


class MainSketch(mn.Scene):
    def construct(self):
        START = int(Audio.strophe2 * 1000)
        STOP = int(Audio.refrain3 * 1000)
        if os.path.exists(Audio.path):
            self.renderer.file_writer.add_audio_segment(Audio.song[START:STOP])
        construct_scene(self, debug=True)
