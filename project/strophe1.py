from helpers import *


def construct_scene(scene: mn.Scene):
    """Konstruktion Kreis + AM"""
    geo = Geo()

    # ANIMATIONSSTART 44,69s

    # Part one

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
        mn.ReplacementTransform(geo.firsta, geo.sega),
        mn.FadeOut(geo.b1),
        mn.FadeOut(geo.b2),
        mn.TransformMatchingShapes(geo.labelAB, term1),
        mn.ReplacementTransform(geo.firstb, geo.segb),
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

    # bitte bite funktuniertre
    moving_dot = mn.Dot(geo.semikreis.point_from_proportion(0), color=mn.RED)
    moving_dot.set_opacity(0)
    line = mn.always_redraw(
        lambda: mn.Line(geo.M.get_center(), moving_dot.get_center(), color=AMCOL)
    )
    scene.add(moving_dot)
    scene.mobjects.insert(1, line)
    scene.play(
        term2.animate.move_to(term3[1].get_center()).set_color(
            AMCOL
        ),  # morph fraction to new fraction
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
    # scene.remove(geo.sega, geo.segb)

    # Part two

    scene.wait(1)
    scene.play(mn.FadeOut(term2, term3), geo.construction.animate.shift(mn.LEFT))

    base_point = lambda val: geo.M.get_center() + [RADIUS * (2 * val - 1), 0, 0]
    arc_point = lambda val: geo.M.get_center() + [
        -RADIUS * math.cos(val * mn.PI),
        RADIUS * math.sin(val * mn.PI),
        0,
    ]

    chord1 = mn.Line(base_point(0.5), arc_point(0.5), color=TXTCOL)
    chord2 = mn.Line(base_point(0.9), arc_point(0.7), color=TXTCOL)
    chord3 = mn.Line(base_point(0.4), arc_point(0.65), color=TXTCOL)
    chord4 = mn.Line(base_point(0.1), arc_point(0.4), color=TXTCOL)
    scene.play(mn.FadeIn(chord1))
    scene.play(mn.ReplacementTransform(chord1.copy(), chord2))
    scene.play(mn.ReplacementTransform(chord2.copy(), chord3))
    scene.play(mn.ReplacementTransform(chord3.copy(), chord4))
    scene.bring_to_front(geo.construction)

    eq_qm = mn.MathTex("QM(a, b)", color=QMCOL)
    eq_am = mn.MathTex("AM(a, b)", color=AMCOL)
    eq_gm = mn.MathTex("GM(a, b)", color=GMCOL)
    eq_hm = mn.MathTex("HM(a, b)", color=HMCOL)

    eq_group = mn.VGroup(eq_qm, eq_am, eq_gm, eq_hm).arrange(mn.DOWN)
    eq_group.shift(4 * mn.RIGHT)

    scene.play(mn.Write(eq_group))

    chord1_copy = chord1.copy().set_color(QMCOL)
    chord2_copy = chord2.copy().set_color(AMCOL)
    chord3_copy = chord3.copy().set_color(GMCOL)
    chord4_copy = chord4.copy().set_color(HMCOL)

    scene.play(mn.ReplacementTransform(eq_qm.copy(), chord1_copy))
    scene.remove(chord1_copy)
    chord1.set_color(QMCOL)

    scene.play(mn.ReplacementTransform(eq_am.copy(), chord2_copy))
    scene.remove(chord2_copy)
    chord2.set_color(AMCOL)

    scene.play(mn.ReplacementTransform(eq_gm.copy(), chord3_copy))
    scene.remove(chord3_copy)
    chord3.set_color(GMCOL)

    scene.play(mn.ReplacementTransform(eq_hm.copy(), chord4_copy))
    scene.remove(chord4_copy)
    chord4.set_color(HMCOL)

    scene.wait(1)

    chord2_v2 = chord2.copy().rotate(-chord2.get_angle()).move_to(3 * mn.UP + mn.LEFT)
    chord3_v2 = chord3.copy().rotate(-chord3.get_angle())
    chord3_v2.move_to(2 * mn.UP).align_to(chord2_v2, mn.LEFT)

    scene.play(mn.ReplacementTransform(chord2.copy(), chord2_v2))
    scene.play(mn.ReplacementTransform(chord3.copy(), chord3_v2))

    scene.wait(1)

    eq_rel = mn.MathTex(r"\geq", color=TXTCOL).rotate(mn.PI).move_to(2.5 * mn.UP)
    eq_rel.next_to(mn.UP, chord3_v2.get_center())

    scene.play(mn.Write(eq_rel))


class MainSketch(mn.Scene):
    def construct(self):
        START = int(Audio.strophe1 * 1000)
        STOP = int(Audio.refrain2 * 1000)
        # if os.path.exists(Audio.path):
        # self.renderer.file_writer.add_audio_segment(Audio.song[START:STOP])
        construct_scene(self)
