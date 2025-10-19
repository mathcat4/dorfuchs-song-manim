from helpers import *


def construct_scene(scene: mn.Scene):
    """Konstruktion QM"""
    geo = Geo()

    term10 = (
        mn.MathTex(r"{{{a+b \over 2}}}", color=TXTCOL)
        .move_to(right_half_center)
        .shift(mn.LEFT * 1.5)
    )
    term11 = (
        mn.MathTex(r"{a+b \over 2} - a", color=TXTCOL)
        .move_to(right_half_center)
        .shift(mn.RIGHT * 1.5)
    )
    term12 = (
        mn.MathTex(r"{{{b-a \over 2}}}", color=TXTCOL)
        .move_to(right_half_center)
        .shift(mn.RIGHT * 1.5)
    )
    term13 = (
        mn.MathTex(
            r"{{|\overline{SN}|}}{{^2}} {{=}} {{(\kern0pt}}{{{a+b \over 2}}}{{)\kern0pt}}{{^2\kern0pt}} {{+}} {{(}}{{{b-a \over 2}}}{{)}}{{\hspace{0pt}^2}} ",
            color=TXTCOL,
        )
        .move_to(right_half_center)
        .shift(mn.UP * 1.5)
    )
    term135 = (
        mn.MathTex(
            r"{{|\overline{SN}|}}{{^2}} {{=}} {  {{(\kern0pt}}a+b{{)\kern0pt}} {{^2\kern0pt}}  {{\over}} {{2^2}} } {{+}} { {{(}}b-a{{)}} {{\hspace{0pt}^2}} {{\over}} {{2^2}} } ",
            color=TXTCOL,
        )
        .move_to(right_half_center)
        .shift(mn.UP * 1.5)
    )
    term14 = (
        mn.MathTex(
            r"{{|\overline{SN}|}}{{^2}} {{=}} {  {{(\kern0pt}}a+b{{)\kern0pt}} {{^2\kern0pt}} {{+}} {{(}}b-a{{)}} {{\hspace{0pt}^2}}  {{\over}} {{2^2}}}",
            color=TXTCOL,
        )
        .move_to(right_half_center)
        .shift(mn.UP * 1.5)
    )
    term15 = mn.MathTex(
        r"{{|\overline{SN}|}}{{^2}} {{=}} {{{a^2}} + 2ab + {{b^2}} {{+}} {{a^2}} - 2ab + {{b^2}} \over {{2^2}}}",
        color=TXTCOL,
        font_size=36,
    ).move_to(right_half_center)
    term16 = mn.MathTex(
        r"{{|\overline{SN}|}}{{^2}} {{=}} {2{{a^2}} {{+}} 2{{b^2}} {{\over}} {{2^2}}}",
        color=TXTCOL,
    ).move_to(right_half_center)
    term17 = mn.MathTex(
        r"{{|\overline{SN}|}}{{^2}} {{=}}  { {{a^2}} {{+}} {{b^2}} {{\over}} {{2}} } ",
        color=TXTCOL,
    ).move_to(right_half_center)
    term17skid = mn.MathTex(
        r"{{|\overline{SN}|}}{{^2}} {{=}}  {{ {a^2 + b^2 \over 2} }}"
    )
    term18 = (
        mn.MathTex(
            r"{{|\overline{SN}|}} {{=}}  {{ \sqrt{a^2 + b^2 \over 2} }}",
            color=TXTCOL,
        )
        .move_to(right_half_center)
        .shift(mn.DOWN * 1.5)
    )

    term19 = mn.MathTex(
        r"{{|\overline{SN}|}} {{=}} {{ \sqrt{a^2 + b^2 \over 2} }} = QM(a,b)",
        color=QMCOL,
    ).move_to(right_half_center)

    # ANIMATION START 1:22,97

    scene.add(geo.construction)
    # vorbereitung
    scene.add(geo.lineMS)
    tex1 = mn.MathTex(r"QM(a,b) = \sqrt{\frac{a^2+b^2}{2}}", color=QMCOL).shift(
        mn.UP * 3
    )
    scene.play(mn.Write(tex1), run_time=2)
    # 24,97
    scene.wait(7.27)
    # 32,24
    scene.bring_to_back(geo.am2)
    scene.play(mn.FadeIn(geo.am2), mn.FadeIn(geo.N), run_time=1)
    scene.wait(1.88)
    # 35,12
    scene.bring_to_back(geo.qm)
    scene.play(mn.Create(geo.qm), run_time=1)
    scene.play(mn.Create(geo.labelN), run_time=1)
    scene.play(mn.Create(geo.rightM), run_time=1)
    scene.play(mn.FadeIn(geo.bquestion, geo.bqtext), run_time=0.33)
    scene.wait(0.33)
    scene.play(mn.FadeOut(geo.bquestion, geo.bqtext), run_time=0.33)
    scene.wait(1.5)
    # 40,61
    scene.play(mn.Wiggle(geo.QMAMDreieck), run_time=1.7)
    scene.add(
        geo.am2
    )  # sieht zwar fett dumm aus aber is nötig, weil das anwenden von Gruppen Daten komisch umformatiert (und man das iwie wieder auflösen muss) und deswegen meine hex hex funktion nd funktioniert.
    scene.bring_to_back(geo.am2)
    scene.play(mn.FadeOut(tex1, run_time=0.5))
    zauberfunktion(scene, geo.GanzeSkizze, lambda m: m.shift(mn.LEFT * 3))
    scene.wait(0.25)
    # 44,06
    scene.play(mn.Wiggle(geo.am2), run_time=1.7)
    am2_copy = geo.am2.copy()
    scene.play(
        mn.Transform(am2_copy, term10, replace_mobject_with_target_in_scene=True),
        run_time=1,
    )
    scene.wait(1.02)
    # 47,78
    scene.remove(geo.lineMS)
    geo.lineMS.color = mn.RED
    scene.play(mn.FadeIn(geo.am3), run_time=0.4)
    scene.play(mn.ReplacementTransform(geo.am3, geo.lineMS), run_time=1.2)
    scene.play(mn.Wiggle(geo.lineMS, scale_value=1.5), run_time=1.3)
    scene.play(mn.ReplacementTransform(geo.lineMS, term11), run_time=0.76)
    scene.play(mn.TransformMatchingShapes(term11, term12), run_time=0.5)

    # scene.play(geo.lineMS.animate.set_color(TXTCOL), run_time=0.14)
    # 51,86
    scene.play(mn.TransformMatchingTex(mn.Group(term12, term10), term13), run_time=1)
    scene.wait(0.03)
    scene.play(mn.TransformMatchingTex(term13, term135), run_time=1)
    scene.wait(0.03)
    scene.play(mn.TransformMatchingTex(term135, term14), run_time=1)
    scene.wait(0.03)
    # 54,95
    scene.play(TransformMatchingTexNoReplace(term14, term15), run_time=1)
    scene.play(mn.TransformMatchingTex(term15, term16), run_time=1)
    scene.play(mn.TransformMatchingTex(term16, term17), run_time=1)
    # alt
    # scene.add(mn.index_labels(term17))
    # scene.add(mn.index_labels(term18))
    scene.play(
        mn.TransformMatchingShapes(term17[0].copy(), term18[0]),
        mn.TransformMatchingShapes(term17[3].copy(), term18[2]),
        mn.TransformMatchingShapes(
            mn.VGroup(term17[5], term17[7], term17[9], term17[11], term17[13]).copy(),
            term18[4],
        ),
        run_time=1,
    )

    scene.play(
        mn.TransformMatchingTex(term18, term19),
        mn.FadeOut(term17),
        mn.FadeOut(term14),
        run_time=1,
    )
    # 59.95


class MainSketch(mn.Scene):
    def construct(self):
        START = int(Audio.strophe2 * 1000)
        STOP = int(Audio.refrain3 * 1000)
        if os.path.exists(Audio.path):
            self.renderer.file_writer.add_audio_segment(Audio.song[START:STOP])
        construct_scene(self)
