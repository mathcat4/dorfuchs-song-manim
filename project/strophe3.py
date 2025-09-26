from helpers import *


def construct_scene(scene: mn.Scene):
    qm.set_opacity(0.5)
    scene.add(construction, qm, N)
    GanzeSkizze.shift(mn.RIGHT*3)
    

    # scene.play(mn.FadeOut(am2), mn.FadeOut(rightM), qm.animate.set_opacity(0.5)) # nehme an das gehört noch zur transition qm-gm, deshalb nicht nötig?
    term4 = mn.MathTex(r"a \cdot b", color=TXTCOL).shift(mn.UP * 3)
    term5 = mn.MathTex(r"\sqrt{ab}", color=TXTCOL).shift(mn.UP * 3)
    term6 = mn.MathTex(r"GM(a,b) =", r"\sqrt{ab}", color=GMCOL).shift(mn.UP * 3)
    term5.generate_target()
    assert term5.target is not None
    term5.target.move_to(term6[1].get_center())  # move into place
    term5.target.set_color(GMCOL)
    # ANIMATION START 2:24,97
    scene.wait(1.77)
    #26:74
    scene.play(mn.Write(term4), run_time=1.5)
    scene.wait(1.62)
    #29,86
    scene.play(mn.TransformMatchingShapes(term4, term5), run_time=1)
    scene.play(mn.FadeIn(term6[0]), mn.MoveToTarget(term5), run_time=1.5)
    scene.wait(4.7)
    #37,06
    scene.play(mn.FadeOut(term6), mn.FadeOut(term5), run_time=1)
    scene.wait(6.14)
    #44,2
    scene.play(mn.Create(gm), mn.Create(rightS), run_time=1)
    scene.wait(2.48)
    #47,68
    scene.play(mn.Create(X), run_time=1)
    scene.play(mn.Create(labelX), run_time=1)
    scene.play(mn.AnimationGroup(mn.Create(lineAX), mn.Create(lineBX), mn.Create(am1)), run_time=1)
    scene.wait(1.17)
    #51,85
    scene.play(mn.AnimationGroup(mn.Create(rightAXB)), run_time=1)
    scene.wait(2.72)
    #55,57
    term7 = mn.MathTex(
        r"{{ |\overline{SX}| }}", r"^2 {{=}}", r"{{a}} \cdot", r"{{b}}", color=TXTCOL
    ).shift(mn.UP * 3)

    # term70 = typing.cast(mn.VMobject, term7[0]) # usw. shuts pylance tf up, but kinda unnecessary
    scene.play(mn.Write(term7[0]), mn.Wiggle(gm), run_time=0.9)
    scene.play(mn.Write(term7[1]), mn.Wiggle(gm), run_time=0.9)
    scene.play(mn.Write(term7[2]), mn.Write(term7[3]), mn.Wiggle(sega), run_time=0.9)
    scene.play(mn.Write(term7[4]), mn.Write(term7[5]), mn.Wiggle(segb), run_time=0.9)
    scene.wait(0.5)
    term8 = mn.MathTex(
        r"{{|\overline{SX}|}} {{=}} \sqrt{{{a}}{{b}}}", color=TXTCOL
    ).shift(mn.UP * 3)
    term9 = mn.MathTex(r"|\overline{SX}| = \sqrt{ab}", r"= GM(a,b)", color=GMCOL).shift(
        mn.UP * 3
    )
    scene.play(mn.TransformMatchingTex(term7, term8))
    term8.generate_target()
    assert term8.target is not None
    term8.target.move_to(term9[0].get_center())  # move into place
    term8.target.set_color(GMCOL)
    scene.play(mn.FadeIn(term9[1]), mn.MoveToTarget(term8))
    #scene.wait(20)



    #scene.play(
    #    mn.FadeOut(term8),
    #    mn.FadeOut(term9),
    #    mn.FadeOut(lineAX),
    #    mn.FadeOut(lineBX),
    #    mn.FadeOut(rightAXB),
    #)
    #scene.play(mn.ReplacementTransform(am2, am1))
    

    


class MainSketch(mn.Scene):
    def construct(self):
        construct_scene(self)
