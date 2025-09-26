from helpers import *


def construct_scene(scene: mn.Scene):
    qm.set_opacity(0.5)
    scene.add(construction, qm, gm, N, X, S, labelN, labelX, rightS, am1)

    tex1 = mn.MathTex(
        r"HM(a,b) = \sqrt{\frac{2}{\frac{1}{a} + \frac{1}{b}}}", color=HMCOL
    ).shift(mn.UP * 3)
    #3:24,04
    scene.play(mn.Write(tex1).run_time=2)
    scene.play(mn.ReplacementTransform(am1, dashedam))
    #28,6
    scene.play(mn.Create(dashed1))
    scene.play(mn.Create(G), mn.Create(labelG))
    scene.play(mn.Create(hm), mn.Create(rightG))
    scene.play(mn.Create(angleX), mn.Create(angleXlabel))
    scene.play(mn.Wiggle(angXl,scale_value=1.5))
    scene.play(mn.Wiggle(rightG,scale_value=1.5), mn.Wiggle(rightS,scale_value=1.5))
    scene.play(mn.FadeOut(tex1))
    scene.add(sega, angleX) # zauberfunktionfix
    zauberfunktion(scene, GanzeSkizze, lambda m: m.shift(mn.LEFT * 3))
    scene.play(mn.Wiggle(AMGMDreieck))
    scene.play(mn.Wiggle(GMHMDreieck))
    
    term20 = mn.MathTex(
        r"{ {{|\overline{XG}|}} {{\over}} |\overline{XS}|} {{=}} {|\overline{XS}| {{\over}} |\overline{XM}|}",
        color=TXTCOL,
    ).move_to(right_half_center)
    term21 = mn.MathTex(
        r"{ {{|\overline{XG}|}} {{\over}} \sqrt{ab} } {{=}} {\sqrt{ab} {{\over}}  {{ {a+b \over 2} }} }",
        color=TXTCOL
    ).move_to(right_half_center)
    term22 = mn.MathTex(
        r"{{|\overline{XG}|}} {{=}} { {{ab}} {{\over}}   {{ {a+b \over 2} }}   }",
        color=TXTCOL
    ).move_to(right_half_center)
    term23 = mn.MathTex(
        r"{{|\overline{XG}|}} {{=}} { {{ab}} \cdot \frac{2}{ab} {{\over}}   {{ {a+b \over 2} }}  \cdot \frac{2}{ab} }",
        color=TXTCOL,
    ).move_to(right_half_center)
    term24 = mn.MathTex(
        r"{{|\overline{XG}|}} {{=}} { 2 {{\over}} {1 \over a} {{+}} {1 \over b}}",
        color=TXTCOL,
    ).move_to(right_half_center)
    term25 = mn.MathTex(
        r"{{|\overline{XG}|}} {{=}} { 2 {{\over}} {1 \over a} {{+}} {1 \over b}} = HM(a,b)",
        color=HMCOL,
    ).move_to(right_half_center)
    scene.play(mn.Write(term20))
    scene.play(mn.TransformMatchingTex(term20,term21))
    scene.play(mn.TransformMatchingTex(term21,term22))
    scene.play(mn.TransformMatchingTex(term22,term23))
    scene.play(mn.TransformMatchingTex(term23,term24))
    scene.play(mn.TransformMatchingShapes(term24,term25))
    scene.wait(1)


class MainSketch(mn.Scene):
    def construct(self):
        construct_scene(self)
