from helpers import *


def construct_scene(scene: mn.Scene):
    qm.set_opacity(0.5)
    scene.add(construction, qm, gm, N, X, S, labelN, labelX, rightS, am1)

    tex1 = mn.MathTex(
        r"HM(a,b) = \sqrt{\frac{2}{\frac{1}{a} + \frac{1}{b}}}", color=HMCOL
    ).shift(mn.UP * 3)
    scene.play(mn.Write(tex1))
    scene.play(mn.ReplacementTransform(am1, dashedam))
    scene.play(mn.Create(dashed1))
    scene.play(mn.Create(G), mn.Create(labelG))
    scene.play(mn.Create(hm), mn.Create(rightG))
    scene.play(mn.Create(angleX), mn.Create(angleXlabel))
    scene.play(mn.Wiggle(angXl))
    scene.play(mn.Wiggle(rightG), mn.Wiggle(rightS))
    scene.play(mn.Wiggle(AMGMDreieck))
    scene.play(mn.Wiggle(GMHMDreieck))
    scene.play(mn.FadeOut(tex1))
    zauberfunktion(scene, GanzeSkizze, lambda m: m.shift(mn.LEFT * 3))
    term20 = mn.MathTex(
        r"\frac{|\overline{XG}|}{|\overline{XS}|} = \frac{|\overline{XS}|}{|\overline{XM}|}",
        color=TXTCOL,
    ).move_to(right_half_center)


class MainSketch(mn.Scene):
    def construct(self):
        construct_scene(self)
