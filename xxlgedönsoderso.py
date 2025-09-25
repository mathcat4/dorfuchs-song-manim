from manim import *
from project.helpers import *
import math


class Constram(Scene):
    def construct(self):
        # Konstruktion Kreis + AM
        self.play(
            FadeIn(firsta), FadeIn(firstb), FadeIn(b1), FadeIn(labelAB), FadeIn(b2)
        )
        term1 = MathTex(r"a + b", color=TXTCOL).shift(UP * 3)
        self.play(
            Transform(firsta, sega),
            FadeOut(b1),
            FadeOut(b2),
            TransformMatchingShapes(labelAB, term1),
            Transform(firstb, segb),
        )
        term2 = MathTex(r"\frac{a + b}{2}", color=TXTCOL).shift(UP * 3)
        self.play(Create(S), FadeIn(abr), FadeIn(bbr), FadeIn(abrtxt), FadeIn(bbrtxt))
        self.play(Create(M), Create(labelM), TransformMatchingShapes(term1, term2))
        self.play(Create(semikreis))
        term3 = MathTex(r"r =", r"\frac{a + b}{2}", r"= AM(a,b)", color=AMCOL).shift(
            UP * 3
        )
        term2.generate_target()
        assert term2.target is not None
        term2.target.move_to(term3[1].get_center())  # move into place
        term2.target.set_color(AMCOL)
        self.play(
            MoveToTarget(term2),  # morph fraction to new fraction
            FadeIn(term3[0]),  # r =
            FadeIn(term3[2]),  # = AM(a,b)
        )
        # bitte bite funktuniertre
        moving_dot = Dot(semikreis.point_from_proportion(0), color=RED)
        moving_dot.set_opacity(0)
        line = always_redraw(
            lambda: Line(M.get_center(), moving_dot.get_center(), color=AMCOL)
        )
        self.add(moving_dot)
        self.add(line)
        self.play(
            MoveAlongPath(
                moving_dot, semikreis, rate_func=lambda t: 1 - (1 - t) ** 2, run_time=3
            )
        )
        self.remove(line)
        self.play(Create(labelS))
        self.wait(1)
        self.play(FadeOut(term3), FadeOut(term2))

        # qm visualisieren
        # vorbereitung
        self.add(lineMS)
        tex1 = MathTex(r"QM(a,b) = \sqrt{\frac{a^2+b^2}{2}}", color=QMCOL).shift(UP * 3)
        self.play(Write(tex1))
        self.play(FadeIn(am2), FadeIn(N))
        self.play(Create(qm))
        self.play(Create(labelN))
        self.play(Create(rightM))
        self.play(Wiggle(QMAMDreieck))
        self.add(
            am2
        )  # sieht zwar fett dumm aus aber is nötig, weil das anwenden von Gruppen Daten komisch umformatiert (und man das iwie wieder auflösen muss) und deswegen meine hex hex funktion nd funktioniert.
        self.play(FadeOut(tex1))
        zauberfunktion(self, GanzeSkizze, lambda m: m.shift(LEFT * 3))
        term10 = (
            MathTex(r"{{\frac{a+b}{2}}}", color=TXTCOL)
            .move_to(right_half_center)
            .shift(LEFT * 1.5)
        )
        term11 = (
            MathTex(r"\frac{a+b}{2} - a", color=TXTCOL)
            .move_to(right_half_center)
            .shift(RIGHT * 1.5)
        )
        term12 = (
            MathTex(r"{{\frac{b-a}{2}}}", color=TXTCOL)
            .move_to(right_half_center)
            .shift(RIGHT * 1.5)
        )
        term13 = (
            MathTex(
                r"{{|\overline{SM}|}}{{^2}} {{=}} ({{\frac{a+b}{2}}})^2 + ({{\frac{b-a}{2}}})^2 ",
                color=TXTCOL,
            )
            .move_to(right_half_center)
            .shift(UP * 1.5)
        )
        term14 = (
            MathTex(
                r"{{|\overline{SM}|}}{{^2}} {{=}} \frac{(a+b)^2 + (b-a)^2}{2^2}",
                color=TXTCOL,
            )
            .move_to(right_half_center)
            .shift(UP * 1.5)
        )
        term15 = MathTex(
            r"{{|\overline{SM}|}}{{^2}} {{=}} \frac{a^2 + 2ab + b^2 + a^2 - 2ab + b^2}{2^2}",
            color=TXTCOL,
            font_size=36,
        ).move_to(right_half_center)
        term16 = MathTex(
            r"{{|\overline{SM}|}}{{^2}} {{=}} \frac{2a^2 + 2b^2}{2^2}", color=TXTCOL
        ).move_to(right_half_center)
        term17 = MathTex(
            r"{{|\overline{SM}|}}{{^2}} {{=}} \frac{a^2 + b^2}{2}", color=TXTCOL
        ).move_to(right_half_center)
        term18 = (
            MathTex(
                r"{{|\overline{SM}|}} {{=}} {{\sqrt{\frac{a^2 + b^2}{2}}}}",
                color=TXTCOL,
            )
            .move_to(right_half_center)
            .shift(DOWN * 1.5)
        )
        term19 = MathTex(
            r"{{|\overline{SM}|}} {{=}} {{\sqrt{\frac{a^2 + b^2}{2}}}} = QM(a,b)",
            color=QMCOL,
        ).move_to(right_half_center)
        self.play(Wiggle(am2), Write(term10))
        self.remove(lineMS)
        lineMS.color = RED
        self.play(FadeIn(am3), run_time=0.5)
        self.play(ReplacementTransform(am3, lineMS), Write(term11))
        self.play(Wiggle(lineMS))
        self.play(lineMS.animate.set_color(TXTCOL))
        self.play(TransformMatchingShapes(term11, term12))
        self.play(TransformMatchingTex(Group(term12, term10), term13))
        self.wait(1)
        self.play(TransformMatchingTex(term13, term14))
        self.play(TransformMatchingTexNoReplace(term14, term15))
        self.play(TransformMatchingTex(term15, term16))
        self.play(TransformMatchingTex(term16, term17))
        self.play(TransformMatchingTexNoReplace(term17, term18))
        self.play(
            TransformMatchingTex(term18, term19), FadeOut(term17), FadeOut(term14)
        )
        self.wait(1)
        self.play(FadeOut(term19))
        zauberfunktion(self, GanzeSkizze, lambda m: m.shift(RIGHT * 3))

        # gm visualisierung
        self.play(FadeOut(am2), FadeOut(rightM), qm.animate.set_opacity(0.5))
        term4 = MathTex(r"a \cdot b", color=TXTCOL).shift(UP * 3)
        term5 = MathTex(r"\sqrt{ab}", color=TXTCOL).shift(UP * 3)
        term6 = MathTex(r"GM(a,b) =", r"\sqrt{ab}", color=GMCOL).shift(UP * 3)
        term5.generate_target()
        assert term5.target is not None
        term5.target.move_to(term6[1].get_center())  # move into place
        term5.target.set_color(GMCOL)
        self.play(Write(term4))
        self.play(TransformMatchingShapes(term4, term5))
        self.play(FadeIn(term6[0]), MoveToTarget(term5))
        self.wait(1)
        self.play(FadeOut(term6), FadeOut(term5))
        self.play(Create(gm), Create(rightS))
        self.play(Create(X))
        self.play(Create(labelX))
        self.play(AnimationGroup(Create(lineAX), Create(lineBX)))
        self.play(AnimationGroup(Create(rightAXB)))
        term7 = MathTex(
            r"{{|\overline{SX}|}}", r"^2 {{=}}", r"{{a}} \cdot", r"{{b}}", color=TXTCOL
        ).shift(UP * 3)

        term70 = typing.cast(VMobject, term7[0])
        self.play(Write(term70), Wiggle(gm))
        term71 = typing.cast(VMobject, term7[1])
        self.play(Write(term71), Wiggle(gm))
        term72 = typing.cast(VMobject, term7[2])
        self.play(Write(term72), Wiggle(sega))
        term73 = typing.cast(VMobject, term7[3])
        self.play(Write(term73), Wiggle(segb))
        self.wait(1)
        term8 = MathTex(
            r"{{|\overline{SX}|}} {{=}} \sqrt{{{a}}{{b}}}", color=TXTCOL
        ).shift(UP * 3)
        term9 = MathTex(
            r"|\overline{SX}| = \sqrt{ab}", r"= GM(a,b)", color=GMCOL
        ).shift(UP * 3)
        self.play(TransformMatchingTex(term7, term8))
        term8.generate_target()
        assert term8.target is not None
        term8.target.move_to(term9[0].get_center())  # move into place
        term8.target.set_color(GMCOL)
        self.play(FadeIn(term9[1]), MoveToTarget(term8))
        self.wait(1)
        self.play(
            FadeOut(term8),
            FadeOut(term9),
            FadeOut(lineAX),
            FadeOut(lineBX),
            FadeOut(rightAXB),
        )

        self.play(ReplacementTransform(am2, am1))
        self.wait(1)

        # hm visualisieren
        tex1 = MathTex(
            r"HM(a,b) = \sqrt{\frac{2}{\frac{1}{a} + \frac{1}{b}}}", color=HMCOL
        ).shift(UP * 3)
        self.play(ReplacementTransform(am1, dashedam))
        self.play(Create(dashed1))
        self.play(Create(G), Create(labelG))
        self.play(Create(hm), Create(rightG))
        self.play(Create(angleX), Create(angleXlabel))
        self.play(Wiggle(angXl))
        self.play(Wiggle(rightG), Wiggle(rightS))
        self.play(Wiggle(AMGMDreieck))
        self.play(Wiggle(GMHMDreieck))
        zauberfunktion(self, GanzeSkizze, lambda m: m.shift(LEFT * 3))
        term20 = MathTex(
            r"\frac{|\overline{XG}|}{|\overline{XS}|} = \frac{|\overline{XS}|}{|\overline{XM}|}",
            color=TXTCOL,
        ).move_to(right_half_center)

        self.wait(1)
