from helpers import *


def construct_scene(scene: mn.Scene):
    """
    Animation for strophe 2. Konstruktion QM.
    """

    geo = Geo()
    scene.add(geo.construction)

    tex1 = mn.MathTex(r"QM(a,b) = \sqrt{\frac{a^2+b^2}{2}}", color=QMCOL).shift(
        mn.UP * 3
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

    scene.wait(1)
    scene.play(mn.Wiggle(geo.QMAMDreieck), run_time=1.7)
    scene.add(
        geo.am2
    )  # sieht zwar fett dumm aus aber is nötig, weil das anwenden von Gruppen Daten komisch umformatiert (und man das iwie wieder auflösen muss) und deswegen meine hex hex funktion nd funktioniert.
    scene.bring_to_back(geo.am2)

    scene.play(mn.FadeOut(tex1, run_time=0.5))
    zauberfunktion(scene, geo.GanzeSkizze, lambda m: m.shift(mn.LEFT * 3))

    scene.wait(0.25)
    scene.play(mn.Wiggle(geo.am2), run_time=1.7)
    am2_copy = geo.am2.copy()
    term1 = (
        mn.MathTex(r"{{{a+b \over 2}}}", color=TXTCOL)
        .move_to(RIGHT_HALF_CENTER)
        .shift(mn.LEFT * 1.5)
    )
    scene.play(
        mn.ReplacementTransform(am2_copy, term1),
        run_time=1,
    )

    scene.wait(1.02)
    scene.bring_to_front(geo.am3)
    scene.bring_to_front(geo.S)
    scene.bring_to_front(geo.M)
    scene.play(mn.FadeIn(geo.am3), run_time=0.4)

    scene.play(
        mn.ReplacementTransform(geo.am3, geo.lineMS.set_color(mn.RED)),
        run_time=1.2,
    )
    scene.play(mn.Wiggle(geo.lineMS, scale_value=1.5), run_time=1.3)

    term2 = (
        mn.MathTex(r"{a+b \over 2} - a", color=TXTCOL)
        .move_to(RIGHT_HALF_CENTER)
        .shift(mn.RIGHT * 1.5)
    )
    scene.play(mn.Transform(geo.lineMS, term2), run_time=0.76)
    scene.remove(geo.lineMS)

    # Pure eqution manipulation

    term3 = (
        mn.MathTex(r"{{{b-a \over 2}}}", color=TXTCOL)
        .move_to(RIGHT_HALF_CENTER)
        .shift(mn.RIGHT * 1.5)
    )
    scene.play(mn.TransformMatchingShapes(term2, term3), run_time=0.5)

    term4 = (
        mn.MathTex(
            r"{{|\overline{SN}|}}{{^2}} {{=}} {{(\kern0pt}}{{{a+b \over 2}}}{{)\kern0pt}}{{^2\kern0pt}} {{+}} {{(}}{{{b-a \over 2}}}{{)}}{{\hspace{0pt}^2}} ",
            color=TXTCOL,
        )
        .move_to(RIGHT_HALF_CENTER)
        .shift(mn.UP * 1.5)
    )
    scene.play(mn.TransformMatchingTex(mn.Group(term3, term1), term4), run_time=1)

    term5 = (
        mn.MathTex(
            r"{{|\overline{SN}|}}{{^2}} {{=}} {  {{(\kern0pt}}a+b{{)\kern0pt}} {{^2\kern0pt}}  {{\over}} {{2^2}} } {{+}} { {{(}}b-a{{)}} {{\hspace{0pt}^2}} {{\over}} {{2^2}} } ",
            color=TXTCOL,
        )
        .move_to(RIGHT_HALF_CENTER)
        .shift(mn.UP * 1.5)
    )
    scene.wait(0.03)
    scene.play(mn.TransformMatchingTex(term4, term5), run_time=1)

    term6 = (
        mn.MathTex(
            r"{{|\overline{SN}|}}{{^2}} {{=}} {  {{(\kern0pt}}a+b{{)\kern0pt}} {{^2\kern0pt}} {{+}} {{(}}b-a{{)}} {{\hspace{0pt}^2}}  {{\over}} {{2^2}}}",
            color=TXTCOL,
        )
        .move_to(RIGHT_HALF_CENTER)
        .shift(mn.UP * 1.5)
    )
    scene.wait(0.03)
    scene.play(mn.TransformMatchingTex(term5, term6), run_time=1)

    term7 = mn.MathTex(
        r"{{|\overline{SN}|}}{{^2}} {{=}} {{{a^2}} + 2ab + {{b^2}} {{+}} {{a^2}} - 2ab + {{b^2}} \over {{2^2}}}",
        color=TXTCOL,
        font_size=36,
    ).move_to(RIGHT_HALF_CENTER)
    scene.wait(0.03)
    scene.play(TransformMatchingTexNoReplace(term6, term7), run_time=1)

    term8 = mn.MathTex(
        r"{{|\overline{SN}|}}{{^2}} {{=}} {2{{a^2}} {{+}} 2{{b^2}} {{\over}} {{2^2}}}",
        color=TXTCOL,
    ).move_to(RIGHT_HALF_CENTER)
    scene.play(mn.TransformMatchingTex(term7, term8), run_time=1)

    term9 = mn.MathTex(
        r"{{|\overline{SN}|}}{{^2}} {{=}}  { {{a^2}} {{+}} {{b^2}} {{\over}} {{2}} } ",
        color=TXTCOL,
    ).move_to(RIGHT_HALF_CENTER)
    scene.play(mn.TransformMatchingTex(term8, term9), run_time=1)

    term10 = (
        mn.MathTex(
            r"{{|\overline{SN}|}} {{=}}  {{ \sqrt{a^2 + b^2 \over 2} }}",
            color=TXTCOL,
        )
        .move_to(RIGHT_HALF_CENTER)
        .shift(mn.DOWN * 1.5)
    )
    scene.play(
        mn.TransformMatchingShapes(term9[0].copy(), term10[0]),
        mn.TransformMatchingShapes(term9[3].copy(), term10[2]),
        mn.TransformMatchingShapes(
            mn.VGroup(
                typ.cast(mn.VGroup, term9[5]),
                typ.cast(mn.VGroup, term9[7]),
                typ.cast(mn.VGroup, term9[9]),
                typ.cast(mn.VGroup, term9[11]),
                typ.cast(mn.VGroup, term9[13]),
            ).copy(),
            term10[4],
        ),
        run_time=1,
    )

    term11 = mn.MathTex(
        r"{{|\overline{SN}|}} {{=}} {{ \sqrt{a^2 + b^2 \over 2} }} = QM(a,b)",
        color=QMCOL,
    ).shift(mn.UP * 3)
    scene.play(
        mn.TransformMatchingTex(term10, term11),
        mn.FadeOut(term9),
        mn.FadeOut(term6),
        run_time=1,
    )

    anims = []
    for mobj in scene.mobjects:
        if mobj != term11:
            anims.append(mn.FadeOut(mobj))

    scene.play(*anims, run_time=0.5)
    geo2 = Geo()

    geo2.QMAMDreieck.move_to(
        geo2.AMGMDreieck.get_center() - geo2.AMGMDreieck.get_center_of_mass()
    )
    geo2.QMAMDreieck.shift(2 * mn.DOWN)

    scene.add(geo2.QMAMDreieck)
    geq = mn.MathTex(r"\geq", color=TXTCOL).next_to(
        geo2.N.get_center(), mn.UP, buff=0.3
    )
    fulluneq = mn.MathTex(
        r"\text{Hypothenuse}", r"\geq", r"\text{Kathete}", color=TXTCOL
    ).next_to(geo2.N.get_center(), mn.UP, buff=0.3)
    fulluneq.move_to(
        fulluneq.get_center() + geq.get_center() - fulluneq[1].get_center()
    )
    fulluneq[0].set_color(QMCOL)
    fulluneq[2].set_color(AMCOL)

    hypolabel = mn.Text("Hypothenuse", font_size=24, color=QMCOL).move_to(geo2.qm)
    hypolabel.rotate(geo2.qm.get_angle()).shift(
        (
            0.2 * math.cos(mn.PI / 2 + geo2.qm.get_angle()),
            0.2 * math.sin(mn.PI / 2 + geo2.qm.get_angle()),
            0,
        )
    )
    kathlabel = mn.Text("Kathete", font_size=24, color=AMCOL).move_to(geo2.am2)
    kathlabel.rotate(-geo2.am2.get_angle()).shift(
        (
            0.2 * math.cos(mn.PI / 2 - geo2.am2.get_angle()),
            0.2 * math.sin(mn.PI / 2 - geo2.am2.get_angle()),
            0,
        )
    )
    scene.add(hypolabel, kathlabel)
    scene.wait(1)
    scene.play(
        mn.Transform(hypolabel, fulluneq[0]),
        mn.Transform(kathlabel, fulluneq[2]),
        mn.FadeIn(geq),
    )


class MainSketch(mn.Scene):
    def construct(self):
        START = int(Audio.strophe2 * 1000)
        STOP = int(Audio.refrain3 * 1000)
        if os.path.exists(Audio.path):
            self.renderer.file_writer.add_audio_segment(Audio.song[START:STOP])
        construct_scene(self)
