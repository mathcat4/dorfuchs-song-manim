from helpers import *


def construct_scene(scene: mn.Scene):
    #ANIMATION START 1::22,97
    scene.add(construction)
    # vorbereitung
    scene.add(lineMS)
    tex1 = mn.MathTex(r"QM(a,b) = \sqrt{\frac{a^2+b^2}{2}}", color=QMCOL).shift(
        mn.UP * 3
    )
    scene.play(mn.Write(tex1))
    scene.play(mn.FadeIn(am2), mn.FadeIn(N))
    scene.play(mn.Create(qm))
    scene.play(mn.Create(labelN))
    scene.play(mn.Create(rightM))
    scene.play(mn.Wiggle(QMAMDreieck))
    scene.add(
        am2
    )  # sieht zwar fett dumm aus aber is nötig, weil das anwenden von Gruppen Daten komisch umformatiert (und man das iwie wieder auflösen muss) und deswegen meine hex hex funktion nd funktioniert.
    scene.play(mn.FadeOut(tex1))
    zauberfunktion(scene, GanzeSkizze, lambda m: m.shift(mn.LEFT * 3))
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
            r"{{|\overline{SM}|}}{{^2}} {{=}} {{(\kern0pt}}{{{a+b \over 2}}}{{)\kern0pt}}{{^2\kern0pt}} {{+}} {{(}}{{{b-a \over 2}}}{{)}}{{\hspace{0pt}^2}} ",
            color=TXTCOL,
        )
        .move_to(right_half_center)
        .shift(mn.UP * 1.5)
    )
    term135 = (
        mn.MathTex(
            r"{{|\overline{SM}|}}{{^2}} {{=}} {  {{(\kern0pt}}a+b{{)\kern0pt}} {{^2\kern0pt}}  {{\over}} {{2^2}} } {{+}} { {{(}}b-a{{)}} {{\hspace{0pt}^2}} {{\over}} {{2^2}} } ",
            color=TXTCOL,
        )
        .move_to(right_half_center)
        .shift(mn.UP * 1.5)
    )
    term14 = (
        mn.MathTex(
            r"{{|\overline{SM}|}}{{^2}} {{=}} {  {{(\kern0pt}}a+b{{)\kern0pt}} {{^2\kern0pt}} {{+}} {{(}}b-a{{)}} {{\hspace{0pt}^2}}  {{\over}} {{2^2}}}",
            color=TXTCOL,
        )
        .move_to(right_half_center)
        .shift(mn.UP * 1.5)
    )
    term15 = mn.MathTex(
        r"{{|\overline{SM}|}}{{^2}} {{=}} {{{a^2}} + 2ab + {{b^2}} {{+}} {{a^2}} - 2ab + {{b^2}} \over {{2^2}}}",
        color=TXTCOL,
        font_size=36,
    ).move_to(right_half_center)
    term16 = mn.MathTex(
        r"{{|\overline{SM}|}}{{^2}} {{=}} {2{{a^2}} + 2{{b^2}} {{\over}} {{2^2}}}", color=TXTCOL
    ).move_to(right_half_center)
    term17 = mn.MathTex(
        r"{{|\overline{SM}|}}{{^2}} {{=}}  {{{a^2}} {{+}} {{b^2}} {{\over}} {{2}}} ", color=TXTCOL
    ).move_to(right_half_center)
    term18 = (
        mn.MathTex(
            r"{{|\overline{SM}|}} {{=}} {{ \sqrt{  { {{a^2}} {{+}} {{b^2}} {{\over}} {{2}} }  } }}",
            color=TXTCOL,
        )
        .move_to(right_half_center)
        .shift(mn.DOWN * 1.5)
    )
    term19 = mn.MathTex(
        r"{{|\overline{SM}|}} {{=}} {{ \sqrt{  {{{a^2}} + {{b^2}} \over 2}  } }} = QM(a,b)",
        color=QMCOL,
    ).move_to(right_half_center)
    scene.play(mn.Wiggle(am2), mn.Write(term10))
    scene.remove(lineMS)
    lineMS.color = mn.RED
    scene.play(mn.FadeIn(am3), run_time=0.5)
    scene.play(mn.ReplacementTransform(am3, lineMS), mn.Write(term11))
    scene.play(mn.Wiggle(lineMS))
    scene.play(lineMS.animate.set_color(TXTCOL))
    scene.play(mn.TransformMatchingShapes(term11, term12))
    scene.play(mn.TransformMatchingTex(mn.Group(term12, term10), term13))
    scene.wait(1)
    scene.play(mn.TransformMatchingTex(term13, term135))
    scene.play(mn.TransformMatchingTex(term135, term14))
    scene.play(TransformMatchingTexNoReplace(term14, term15))
    scene.play(mn.TransformMatchingTex(term15, term16))
    scene.play(mn.TransformMatchingTex(term16, term17))
    scene.play(TransformMatchingTexNoReplace(term17, term18))
    scene.play(
        mn.TransformMatchingTex(term18, term19), mn.FadeOut(term17), mn.FadeOut(term14)
    )

    # Maybe das hier unten nicht mehr nötig, da es zum Refrain gecuttet wird?
    scene.wait(1)
    scene.play(mn.FadeOut(term19))
    zauberfunktion(scene, GanzeSkizze, lambda m: m.shift(mn.RIGHT * 3))


class MainSketch(mn.Scene):
    def construct(self):
        construct_scene(self)
