from helpers import *


def construct_scene(scene: mn.Scene):
    """
    Animation for strophe 1. Konstruktion Kreis + AM.
    """
    geo = Geo()

    ## Part one

    # Initial braces and segments

    firsta = mn.Line(
        geo.A.get_center() + (-0.25, 0.5, 0),
        geo.S.get_center() + (-0.25, 0.5, 0),
        color=TXTCOL,
    )
    firstb = mn.Line(
        geo.S.get_center() + (0.25, 0.5, 0),
        geo.B.get_center() + (0.25, 0.5, 0),
        color=TXTCOL,
    )

    b1 = mn.Brace(firsta, direction=mn.UP, color=TXTCOL)
    b1text = b1.get_tex("a")
    b1text.set_color(TXTCOL)

    b2 = mn.Brace(firstb, direction=mn.UP, color=TXTCOL)
    b2text = b2.get_tex("b")
    b2text.set_color(TXTCOL)
    labelAB = mn.VGroup(b1text, b2text)

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
        mn.ReplacementTransform(firsta, geo.sega),
        mn.ReplacementTransform(firstb, geo.segb),
        mn.FadeOut(b1),
        mn.FadeOut(b2),
        mn.TransformMatchingShapes(labelAB, term1),
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

    # whole radius moving animation thing
    scene.wait(1.47)
    term3 = mn.MathTex("r =", r"\frac{a + b}{2}", "= AM(a,b)", color=AMCOL).shift(
        mn.UP * 3
    )
    # bitte bite funktuniertre
    moving_dot = geo.B.copy().set_opacity(0)
    line = mn.always_redraw(
        lambda: mn.Line(geo.M.get_center(), moving_dot.get_center(), color=AMCOL)
    )
    scene.add(moving_dot)
    scene.mobjects.insert(1, line)
    scene.play(
        mn.TransformMatchingShapes(term2, term3[1]),  # morph fraction to new fraction
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

    scene.wait(2)
    scene.play(mn.Create(geo.labelS))

    ## Part two

    scene.wait(2.5)
    scene.play(mn.FadeOut(term3), geo.construction.animate.shift(mn.DOWN + 2 * mn.LEFT))

    # Construct chords in semicircle

    base_point = lambda val: geo.M.get_center() + [geo.RADIUS * (2 * val - 1), 0, 0]
    arc_point = lambda val: geo.M.get_center() + [
        -geo.RADIUS * math.cos(val * mn.PI),
        geo.RADIUS * math.sin(val * mn.PI),
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

    # Write mean equations

    eq_qm = mn.MathTex("QM(a, b)", color=QMCOL)
    eq_am = mn.MathTex("AM(a, b)", color=AMCOL)
    eq_gm = mn.MathTex("GM(a, b)", color=GMCOL)
    eq_hm = mn.MathTex("HM(a, b)", color=HMCOL)

    eq_group = mn.VGroup(eq_qm, eq_am, eq_gm, eq_hm).arrange(mn.DOWN)
    eq_group.move_to(RIGHT_HALF_CENTER)
    eq_group.align_to(geo.semikreis, mn.DOWN)

    scene.play(mn.Write(eq_group))

    # Map mean equations to semicircle

    chord_qm2 = chord_qm.copy().set_color(QMCOL)
    question_chord_qm = mn.Text("?", color=QMCOL).scale(0.5)
    question_chord_qm.next_to(chord_qm.get_center(), mn.DR, buff=0.15)

    chord_am2 = chord_am.copy().set_color(AMCOL)
    question_chord_am = mn.Text("?", color=AMCOL).scale(0.5)
    question_chord_am.next_to(chord_am.get_center(), buff=0.15)

    chord_gm2 = chord_gm.copy().set_color(GMCOL)
    question_chord_gm = mn.Text("?", color=GMCOL).scale(0.5)
    question_chord_gm.next_to(chord_gm.get_center(), mn.LEFT, buff=0.15)

    chord_hm2 = chord_hm.copy().set_color(HMCOL)
    question_chord_hm = mn.Text("?", color=HMCOL).scale(0.5)
    question_chord_hm.next_to(chord_hm.get_center(), buff=0.15)

    scene.play(
        mn.ReplacementTransform(eq_qm.copy(), chord_qm2),
        mn.ReplacementTransform(eq_am.copy(), chord_am2),
        mn.ReplacementTransform(eq_gm.copy(), chord_gm2),
        mn.ReplacementTransform(eq_hm.copy(), chord_hm2),
        mn.FadeIn(
            question_chord_qm, question_chord_am, question_chord_gm, question_chord_hm
        ),
        run_time=1,
    )
    scene.bring_to_front(geo.construction)
    scene.remove(chord_qm, chord_am, chord_gm, chord_hm)

    # Draw copies of AM and QM

    group_chord_am2 = mn.VGroup(chord_am2, question_chord_am)
    group_chord_qm2 = mn.VGroup(chord_qm2, question_chord_qm)

    chord_am3 = chord_am2.copy().rotate(-chord_am2.get_angle())
    question_chord_am3 = question_chord_am.copy().next_to(
        chord_am3.get_center(), mn.UP, buff=0.15
    )
    group_chord_am3 = mn.VGroup(chord_am3, question_chord_am3).move_to(
        3.5 * mn.UP + 1.7 * mn.LEFT
    )

    chord_qm3 = chord_qm2.copy().rotate(-chord_qm2.get_angle())
    question_chord_qm3 = question_chord_qm.copy().next_to(
        chord_qm3.get_center(), mn.DOWN, buff=0.2
    )
    group_chord_qm3 = (
        mn.VGroup(chord_qm3, question_chord_qm3)
        .next_to(group_chord_am3, mn.DOWN, buff=1.5)
        .align_to(group_chord_am3, mn.LEFT)
    )

    scene.wait(1)
    scene.play(mn.ReplacementTransform(group_chord_am2, group_chord_am3))
    scene.play(mn.ReplacementTransform(group_chord_qm2, group_chord_qm3))

    # Relation and mean anims

    eq_rel = mn.MathTex(r"\leq", color=TXTCOL).rotate(-mn.PI / 2)
    eq_rel.move_to((chord_am2.get_center() + chord_qm2.get_center()) / 2)
    scene.wait(1)
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

    ## Part 3

    # Triangle setup

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
    scene.bring_to_back(rightangle)

    label_a = mn.MathTex("k_1", color=TXTCOL).next_to(side_BC, mn.LEFT)
    label_b = mn.MathTex("k_2", color=TXTCOL).next_to(side_CA, mn.DOWN)
    label_c = mn.MathTex("h", color=TXTCOL).next_to(side_AB.get_center(), mn.UR)

    scene.play(
        mn.FadeIn(triangle),
        mn.FadeIn(rightangle),
        mn.FadeIn(label_a),
        mn.FadeIn(label_b),
        mn.FadeIn(label_c),
    )

    # Write theorem and equation step by step

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

    scene.play(
        mn.Write(typ.cast(mn.VMobject, eq_thm.chars[0])),
    )

    eq_ineq1 = mn.MathTex(r"h \geq k_1", color=TXTCOL)
    eq_ineq2 = mn.MathTex(r"h \geq k_2", color=TXTCOL)
    group_ineq = mn.VGroup(eq_ineq1, eq_ineq2).arrange(mn.DOWN)
    group_ineq.move_to(RIGHT_HALF_CENTER)

    scene.play(
        mn.Write(typ.cast(mn.VMobject, eq_thm.chars[1])),
        mn.Write(group_ineq),
        mn.Create(mn.SurroundingRectangle(group_ineq, color=TXTCOL)),
    )


class MainSketch(mn.Scene):
    def construct(self):
        START = int(Audio.strophe1 * 1000)
        STOP = int(Audio.refrain2 * 1000)
        if os.path.exists(Audio.path):
            self.renderer.file_writer.add_audio_segment(Audio.song[START:STOP])
        construct_scene(self)
