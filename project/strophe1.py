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

    # Part two

    scene.wait(4)
    scene.play(mn.FadeOut(term2, term3), geo.construction.animate.shift(mn.DL))

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
    eq_group.shift(4 * mn.RIGHT + mn.DOWN)

    scene.play(mn.Write(eq_group))

    chord1_copy = chord1.copy().set_color(QMCOL)
    question_chord1 = mn.Text("?", color=QMCOL).scale(0.5)
    question_chord1.next_to(chord1.get_center(), mn.LEFT, buff=0.2)

    chord2_copy = chord2.copy().set_color(AMCOL)
    question_chord2 = mn.Text("?", color=AMCOL).scale(0.5)
    question_chord2.next_to(chord2.get_center(), buff=0.2)
    group_chord2 = mn.VGroup(chord2, question_chord2)

    chord3_copy = chord3.copy().set_color(GMCOL)
    question_chord3 = mn.Text("?", color=GMCOL).scale(0.5)
    question_chord3.next_to(chord3.get_center(), buff=0.2)
    group_chord3 = mn.VGroup(chord3, question_chord3)

    chord4_copy = chord4.copy().set_color(HMCOL)
    question_chord4 = mn.Text("?", color=HMCOL).scale(0.5)
    question_chord4.next_to(chord4.get_center(), buff=0.2)

    scene.play(
        mn.ReplacementTransform(eq_qm.copy(), chord1_copy),
        mn.ReplacementTransform(eq_am.copy(), chord2_copy),
        mn.ReplacementTransform(eq_gm.copy(), chord3_copy),
        mn.ReplacementTransform(eq_hm.copy(), chord4_copy),
        mn.FadeIn(question_chord1, question_chord2, question_chord3, question_chord4),
        run_time=1,
    )
    scene.remove(chord1_copy, chord2_copy, chord3_copy, chord4_copy)

    chord1.set_color(QMCOL)
    chord2.set_color(AMCOL)
    chord3.set_color(GMCOL)
    chord4.set_color(HMCOL)

    scene.wait(1)

    chord2_v2 = chord2.copy().rotate(-chord2.get_angle())
    question_chord2_v2 = question_chord2.copy().next_to(
        chord2_v2.get_center(), mn.UP, buff=0.2
    )
    group_chord2_v2 = mn.VGroup(chord2_v2, question_chord2_v2).move_to(
        3 * mn.UP + 2 * mn.LEFT
    )

    chord3_v2 = chord3.copy().rotate(-chord3.get_angle())
    question_chord3_v2 = question_chord3.copy().next_to(
        chord3_v2.get_center(), mn.DOWN, buff=0.2
    )
    group_chord3_v2 = (
        mn.VGroup(chord3_v2, question_chord3_v2)
        .move_to(1 * mn.UP)
        .align_to(group_chord2_v2, mn.LEFT)
    )

    scene.play(mn.ReplacementTransform(group_chord2.copy(), group_chord2_v2))
    scene.play(mn.ReplacementTransform(group_chord3.copy(), group_chord3_v2))

    scene.wait(1)

    eq_rel = mn.MathTex(r"\geq", color=TXTCOL).rotate(mn.PI / 2)
    eq_rel.move_to((chord2_v2.get_center() + chord3_v2.get_center()) / 2)

    scene.play(mn.Write(eq_rel))

    eq_gm_copy = mn.MathTex("GM(a, b)?", color=GMCOL).next_to(chord3_v2, buff=1)
    eq_am_copy = (
        mn.MathTex("AM(a, b)?", color=AMCOL)
        .next_to(chord2_v2)
        .set_x(eq_gm_copy.get_x())
    )

    eq_rel_copy = eq_rel.copy()
    eq_rel_copy.move_to((eq_am_copy.get_center() + eq_gm_copy.get_center()) / 2)

    scene.wait(2)

    scene.play(
        mn.ReplacementTransform(chord2_v2.copy(), eq_am_copy),
        mn.ReplacementTransform(eq_rel.copy(), eq_rel_copy),
        mn.ReplacementTransform(chord3_v2.copy(), eq_gm_copy),
    )

    scene.wait(3)

    fadeout_all(scene)

    point_C = mn.Dot(mn.ORIGIN, color=TXTCOL)
    point_A = mn.Dot(3 * mn.RIGHT, color=TXTCOL)
    point_B = mn.Dot(4 * mn.UP, color=TXTCOL)

    side_AB = mn.Line(point_A.get_center(), point_B.get_center(), color=TXTCOL)
    side_BC = mn.Line(point_B.get_center(), point_C.get_center(), color=TXTCOL)
    side_CA = mn.Line(point_C.get_center(), point_A.get_center(), color=TXTCOL)

    triangle = mn.VGroup(point_A, point_B, point_C, side_AB, side_BC, side_CA)
    triangle.center().shift(mn.DOWN)
    scene.play(mn.FadeIn(triangle))

    rightangle = mn.Angle(
        mn.Line(point_C, point_A),
        mn.Line(point_C, point_B),
        radius=0.5,
        other_angle=False,
        dot=True,
        dot_color=RIGHTANGLECOL,
        color=RIGHTANGLECOL,
    )

    label_a = mn.MathTex("a", color=TXTCOL).next_to(side_BC, mn.LEFT)
    label_b = mn.MathTex("b", color=TXTCOL).next_to(side_CA, mn.DOWN)
    label_c = mn.MathTex("c", color=TXTCOL).next_to(side_AB.get_center(), mn.UR)

    scene.wait(0.5)
    scene.bring_to_back(rightangle)
    scene.play(
        mn.Create(rightangle), mn.Write(label_a), mn.Write(label_b), mn.Write(label_c)
    )

    term1 = mn.MathTex("c^2 = a^2 + b^2", color=TXTCOL).next_to(triangle).shift(mn.UP)
    term2 = mn.MathTex(r"c^2 \geq a^2", color=TXTCOL).next_to(term1, 2 * mn.DOWN)
    term3 = mn.MathTex(r"c^2 \geq b^2", color=TXTCOL).next_to(term2, 2 * mn.DOWN)

    term2_v2 = mn.MathTex(r"c \geq a", color=TXTCOL).next_to(term1, 2 * mn.DOWN)
    term3_v2 = mn.MathTex(r"c \geq b", color=TXTCOL).next_to(term2, 2 * mn.DOWN)
    group_v2 = mn.VGroup(term2_v2, term3_v2)

    eq_thm = mn.Text("Satz im rechtwinkligen Dreieck:", font_size=28, color=TXTCOL)

    eq_thm2 = mn.Text(
        "Die Hypotenuse ist stets länger als eine Kathete.", font_size=28, color=TXTCOL
    )

    group_thm = mn.VGroup(eq_thm, eq_thm2).arrange(mn.DOWN).shift(3 * mn.UP)

    scene.play(
        mn.Succession(
            mn.Write(term1),
            mn.TransformMatchingShapes(term1.copy(), term2),
            mn.TransformMatchingShapes(term1.copy(), term3),
        ),
        mn.Write(group_thm),
    )

    scene.play(
        mn.Transform(term2, term2_v2),
        mn.Transform(term3, term3_v2),
        mn.Create(mn.SurroundingRectangle(group_v2, color=TXTCOL)),
    )


class MainSketch(mn.Scene):
    def construct(self):
        START = int(Audio.strophe1 * 1000)
        STOP = int(Audio.refrain2 * 1000)
        if os.path.exists(Audio.path):
            self.renderer.file_writer.add_audio_segment(Audio.song[START:STOP])
        construct_scene(self)
