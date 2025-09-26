from helpers import *


def construct_scene(scene: mn.Scene):
    # Konstruktion Kreis + AM
    #ANIMATIONSSTART 44,69s
    scene.play(
        mn.FadeIn(firsta),
        mn.FadeIn(firstb),
        mn.FadeIn(b1),
        mn.FadeIn(labelAB),
        mn.FadeIn(b2),
    )
    scene.wait(4.13)
    term1 = mn.MathTex(r"a + b", color=TXTCOL).shift(mn.UP * 3)
    scene.play(
        mn.Transform(firsta, sega),
        mn.FadeOut(b1),
        mn.FadeOut(b2),
        mn.TransformMatchingShapes(labelAB, term1),
        mn.Transform(firstb, segb),
    )
    term2 = mn.MathTex(r"\frac{a + b}{2}", color=TXTCOL).shift(mn.UP * 3)
    scene.play(
        mn.Create(S),
        mn.FadeIn(abr),
        mn.FadeIn(bbr),
        mn.FadeIn(abrtxt),
        mn.FadeIn(bbrtxt),
    )
    scene.play(
        mn.Create(M), mn.Create(labelM), mn.TransformMatchingShapes(term1, term2)
    )
    scene.wait(1.74)
    scene.play(mn.Create(semikreis))
    scene.wait(0.47)
    term3 = mn.MathTex(r"r =", r"\frac{a + b}{2}", r"= AM(a,b)", color=AMCOL).shift(
        mn.UP * 3
    )
    term2.generate_target()
    assert term2.target is not None
    term2.target.move_to(term3[1].get_center())  # move into place
    term2.target.set_color(AMCOL)
    #scene.play()
    # bitte bite funktuniertre
    moving_dot = mn.Dot(semikreis.point_from_proportion(0), color=mn.RED)
    moving_dot.set_opacity(0)
    line = mn.always_redraw(
        lambda: mn.Line(M.get_center(), moving_dot.get_center(), color=AMCOL)
    )
    scene.add(moving_dot)
    scene.add(line)
    scene.play(
        mn.MoveToTarget(term2),  # morph fraction to new fraction
        mn.FadeIn(term3[0]),  # r =
        mn.FadeIn(term3[2]),  # = AM(a,b)
        mn.MoveAlongPath(
            moving_dot, semikreis, rate_func=lambda t: 1 - (1 - t) ** 2, run_time=2.8
        )
    )
    scene.remove(line)
    scene.wait(1.5)
    scene.play(mn.Create(labelS))
    #scene.wait(4.5)
    #ANIMATION END 65,33s


class MainSketch(mn.Scene):
    def construct(self):
        construct_scene(self)
