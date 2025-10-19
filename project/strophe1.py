from helpers import *


def construct_scene(scene: mn.Scene):
    """Konstruktion Kreis + AM"""
    geo = Geo()

    # ANIMATIONSSTART 44,69s
    scene.play(
        mn.FadeIn(geo.firsta),
        mn.FadeIn(geo.firstb),
        mn.FadeIn(geo.b1),
        mn.FadeIn(geo.labelAB),
        mn.FadeIn(geo.b2),
    )
    scene.wait(4.13)
    term1 = mn.MathTex(r"a + b", color=TXTCOL).shift(mn.UP * 3)
    scene.play(
        mn.Transform(geo.firsta, geo.sega),
        mn.FadeOut(geo.b1),
        mn.FadeOut(geo.b2),
        mn.TransformMatchingShapes(geo.labelAB, term1),
        mn.Transform(geo.firstb, geo.segb),
    )
    term2 = mn.MathTex(r"\frac{a + b}{2}", color=TXTCOL).shift(mn.UP * 3)
    scene.play(
        mn.Create(geo.S),
        mn.FadeIn(geo.abr),
        mn.FadeIn(geo.bbr),
        mn.FadeIn(geo.abrtxt),
        mn.FadeIn(geo.bbrtxt),
    )
    scene.play(
        mn.Create(geo.M),
        mn.Create(geo.labelM),
        mn.TransformMatchingShapes(term1, term2),
    )
    scene.wait(1.74)
    scene.play(mn.Create(geo.semikreis))
    scene.wait(0.47)
    term3 = mn.MathTex(r"r =", r"\frac{a + b}{2}", r"= AM(a,b)", color=AMCOL).shift(
        mn.UP * 3
    )
    term2.generate_target()
    assert term2.target is not None
    term2.target.move_to(term3[1].get_center())  # move into place
    term2.target.set_color(AMCOL)
    # scene.play()
    # bitte bite funktuniertre
    moving_dot = mn.Dot(geo.semikreis.point_from_proportion(0), color=mn.RED)
    moving_dot.set_opacity(0)
    line = mn.always_redraw(
        lambda: mn.Line(geo.M.get_center(), moving_dot.get_center(), color=AMCOL)
    )
    scene.add(moving_dot)
    scene.add(line)
    scene.play(
        mn.MoveToTarget(term2),  # morph fraction to new fraction
        mn.FadeIn(term3[0]),  # r =
        mn.FadeIn(term3[2]),  # = AM(a,b)
        mn.MoveAlongPath(
            moving_dot,
            geo.semikreis,
            rate_func=lambda t: 1 - (1 - t) ** 2,
            run_time=2.8,
        ),
    )
    scene.remove(line)
    scene.wait(1.5)
    scene.play(mn.Create(geo.labelS))


class MainSketch(mn.Scene):
    def construct(self):
        START = int(Audio.strophe1 * 1000)
        STOP = int(Audio.refrain2 * 1000)
        if os.path.exists(Audio.path):
            self.renderer.file_writer.add_audio_segment(Audio.song[START:STOP])
        construct_scene(self)
