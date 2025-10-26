from helpers import *


def construct_scene(scene: mn.Scene):
    """Konstruktion Kreis + AM"""
    geo = Geo()

    # ANIMATIONSSTART 44,69s

    ## Part one

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
    scene.wait(3)
    scene.play(mn.Create(geo.labelS))

    ## Part two

    scene.wait(2.5)
    scene.play(
        mn.FadeOut(term2, term3), geo.construction.animate.shift(mn.DOWN + 2 * mn.LEFT)
    )

    base_point = lambda val: geo.M.get_center() + [RADIUS * (2 * val - 1), 0, 0]
    arc_point = lambda val: geo.M.get_center() + [
        -RADIUS * math.cos(val * mn.PI),
        RADIUS * math.sin(val * mn.PI),
        0,
    ]

    chord_qm = mn.Line(base_point(0.35), arc_point(0.75), color=TXTCOL)
    chord_am = mn.Line(base_point(0.1), arc_point(0.4), color=TXTCOL)
    chord_gm = mn.Line(base_point(0.4), arc_point(0.45), color=TXTCOL)
    chord_hm = mn.Line(base_point(0.9), arc_point(0.7), color=TXTCOL)

    scene.play(mn.FadeIn(chord_gm))
    scene.play(mn.ReplacementTransform(chord_gm.copy(), chord_hm))
    scene.play(mn.ReplacementTransform(chord_hm.copy(), chord_qm))
    scene.play(mn.ReplacementTransform(chord_qm.copy(), chord_am))

    eq_qm = mn.MathTex("QM(a, b)", color=QMCOL)
    eq_am = mn.MathTex("AM(a, b)", color=AMCOL)
    eq_gm = mn.MathTex("GM(a, b)", color=GMCOL)
    eq_hm = mn.MathTex("HM(a, b)", color=HMCOL)

    eq_group = mn.VGroup(eq_qm, eq_am, eq_gm, eq_hm).arrange(mn.DOWN)
    eq_group.shift(4 * mn.RIGHT + mn.DOWN)

    scene.play(mn.Write(eq_group))

    chord_qm_copy = chord_qm.copy().set_color(QMCOL)
    question_chord_qm = mn.Text("?", color=QMCOL).scale(0.5)
    question_chord_qm.next_to(chord_qm.get_center(), mn.DR, buff=0.15)
    group_chord_qm = mn.VGroup(chord_qm, question_chord_qm)

    chord_am_copy = chord_am.copy().set_color(AMCOL)
    question_chord_am = mn.Text("?", color=AMCOL).scale(0.5)
    question_chord_am.next_to(chord_am.get_center(), buff=0.15)
    group_chord_am = mn.VGroup(chord_am, question_chord_am)

    chord_gm_copy = chord_gm.copy().set_color(GMCOL)
    question_chord_gm = mn.Text("?", color=GMCOL).scale(0.5)
    question_chord_gm.next_to(chord_gm.get_center(), mn.LEFT, buff=0.15)

    chord_hm_copy = chord_hm.copy().set_color(HMCOL)
    question_chord_hm = mn.Text("?", color=HMCOL).scale(0.5)
    question_chord_hm.next_to(chord_hm.get_center(), buff=0.15)

    scene.play(
        mn.ReplacementTransform(eq_qm.copy(), chord_qm_copy),
        mn.ReplacementTransform(eq_am.copy(), chord_am_copy),
        mn.ReplacementTransform(eq_gm.copy(), chord_gm_copy),
        mn.ReplacementTransform(eq_hm.copy(), chord_hm_copy),
        mn.FadeIn(
            question_chord_qm, question_chord_am, question_chord_gm, question_chord_hm
        ),
        run_time=1,
    )
    scene.bring_to_front(geo.construction)
    scene.remove(chord_qm_copy, chord_am_copy, chord_gm_copy, chord_hm_copy)

    chord_qm.set_color(QMCOL)
    chord_am.set_color(AMCOL)
    chord_gm.set_color(GMCOL)
    chord_hm.set_color(HMCOL)

    scene.wait(1)

    chord_am2 = chord_am.copy().rotate(-chord_am.get_angle())
    question_chord_am2 = question_chord_am.copy().next_to(
        chord_am2.get_center(), mn.UP, buff=0.15
    )
    group_chord_am2 = mn.VGroup(chord_am2, question_chord_am2).move_to(
        3.5 * mn.UP + 2 * mn.LEFT
    )

    chord_qm2 = chord_qm.copy().rotate(-chord_qm.get_angle())
    question_chord_qm2 = question_chord_qm.copy().next_to(
        chord_qm2.get_center(), mn.DOWN, buff=0.2
    )
    group_chord_qm2 = (
        mn.VGroup(chord_qm2, question_chord_qm2)
        .next_to(group_chord_am2, mn.DOWN, buff=1.5)
        .align_to(group_chord_am2, mn.LEFT)
    )

    scene.play(mn.ReplacementTransform(group_chord_am.copy(), group_chord_am2))
    scene.play(mn.ReplacementTransform(group_chord_qm.copy(), group_chord_qm2))

    scene.wait(1)

    eq_rel = mn.MathTex(r"\leq", color=TXTCOL).rotate(-mn.PI / 2)
    eq_rel.move_to((chord_am2.get_center() + chord_qm2.get_center()) / 2)

    scene.play(mn.Write(eq_rel))

    eq_qm_copy = mn.MathTex("QM(a, b)?", color=QMCOL).next_to(chord_qm2, buff=1)
    eq_am_copy = (
        mn.MathTex("AM(a, b)?", color=AMCOL)
        .next_to(chord_am2)
        .set_x(eq_qm_copy.get_x())
    )

    eq_rel_copy = eq_rel.copy()
    eq_rel_copy.move_to((eq_am_copy.get_center() + eq_qm_copy.get_center()) / 2)

    scene.wait(2)

    scene.play(
        mn.ReplacementTransform(chord_am2.copy(), eq_am_copy),
        mn.ReplacementTransform(eq_rel.copy(), eq_rel_copy),
        mn.ReplacementTransform(chord_qm2.copy(), eq_qm_copy),
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

    rightangle = mn.Angle(
        mn.Line(point_C, point_A),
        mn.Line(point_C, point_B),
        radius=0.5,
        other_angle=False,
        dot=True,
        dot_color=RIGHTANGLECOL,
        color=RIGHTANGLECOL,
    )

    label_a = mn.MathTex("k_1", color=TXTCOL).next_to(side_BC, mn.LEFT)
    label_b = mn.MathTex("k_2", color=TXTCOL).next_to(side_CA, mn.DOWN)
    label_c = mn.MathTex("h", color=TXTCOL).next_to(side_AB.get_center(), mn.UR)

    eq_thm = (
        mn.Paragraph(
            "Satz im rechtwinkligen Dreieck:",
            "Die Hypotenuse ist stets länger als eine Kathete.",
            alignment="center",
            line_spacing=1,
            color=mn.RED,
        )
        .scale(0.6)
        .shift(3 * mn.UP)
    )

    scene.bring_to_back(rightangle)
    scene.play(
        mn.FadeIn(triangle),
        mn.FadeIn(rightangle),
        mn.FadeIn(label_a),
        mn.FadeIn(label_b),
        mn.FadeIn(label_c),
    )

    scene.wait(0.5)
    scene.play(
        mn.Write(typ.cast(mn.VMobject, eq_thm.chars[0])),
    )

    scene.play(mn.Write(typ.cast(mn.VMobject, eq_thm.chars[1])))


class MainSketch(mn.Scene):
    def construct(self):
        START = int(Audio.strophe1 * 1000)
        STOP = int(Audio.refrain2 * 1000)
        if os.path.exists(Audio.path):
            self.renderer.file_writer.add_audio_segment(Audio.song[START:STOP])
        construct_scene(self)
