from helpers import *


def construct_scene(scene: mn.Scene):
    """Konstruktion QM"""
    geo = Geo()

    # Part one

    geo.GanzeSkizze.shift(mn.DOWN + 2 * mn.LEFT)

    # Updaters for animation

    geo.labelN.next_to(geo.N, mn.UR, buff=0.05)
    geo.labelS.add_updater(lambda label: label.next_to(geo.S, mn.UL, buff=0.05))
    geo.labelX.add_updater(lambda label: label.next_to(geo.X, mn.UL, buff=0.05))

    geo.X.add_updater(
        lambda dot: dot.move_to(
            (
                geo.S.get_x(),
                geo.M.get_y()
                + math.sqrt(RADIUS**2 - (geo.M.get_x() - geo.S.get_x()) ** 2),
                0,
            )
        )
    )
    geo.G.add_updater(
        lambda dot: dot.move_to(geo.am1.get_projection(geo.S.get_center()))
    )

    geo.qm.add_updater(
        lambda line: line.put_start_and_end_on(geo.S.get_center(), geo.N.get_center())
    )
    geo.am1.add_updater(
        lambda line: line.put_start_and_end_on(geo.M.get_center(), geo.X.get_center())
    )
    geo.am2.add_updater(
        lambda line: line.put_start_and_end_on(geo.M.get_center(), geo.N.get_center())
    )
    geo.gm.add_updater(
        lambda line: line.put_start_and_end_on(geo.S.get_center(), geo.X.get_center())
    )
    geo.hm.add_updater(
        lambda line: line.put_start_and_end_on(geo.X.get_center(), geo.G.get_center())
    )
    geo.dashed1.add_updater(
        lambda line: line.put_start_and_end_on(geo.S.get_center(), geo.G.get_center())
    )

    geo.abr.add_updater(
        lambda brace: brace.become(
            mn.Brace(
                mn.Line(start=geo.A.get_center(), end=geo.S.get_center()),
                direction=geo.firsta.copy().rotate(3 * mn.PI / 2).get_unit_vector(),
                color=TXTCOL,
            )
        )
    )

    geo.abrtxt.add_updater(
        lambda mobj: mobj.become(geo.abr.get_tex("a").set_color(TXTCOL))
    )

    geo.bbr.add_updater(
        lambda brace: brace.become(
            mn.Brace(
                mn.Line(start=geo.S.get_center(), end=geo.B.get_center()),
                direction=geo.firsta.copy().rotate(3 * mn.PI / 2).get_unit_vector(),
                color=TXTCOL,
            )
        )
    )

    geo.bbrtxt.add_updater(
        lambda mobj: mobj.become(geo.bbr.get_tex("b").set_color(TXTCOL))
    )

    scene.add(
        geo.qm,
        geo.gm,
        geo.am1,
        geo.am2,
        geo.hm,
        geo.dashed1,
        geo.construction,
        geo.N,
        geo.X,
        geo.G,
        geo.labelN,
        geo.labelX,
        geo.labelG,
    )

    # Number line

    number_line = mn.NumberLine(
        x_range=[1, 5, 1],
        length=5,
        color=TXTCOL,
        rotation=mn.PI / 2,
    ).shift(4 * mn.RIGHT + 0.5 * mn.DOWN)

    dot_a = mn.Dot(number_line.n2p(A_VAL), color=TXTCOL)
    dot_b = mn.Dot(number_line.n2p(2 * RADIUS - A_VAL), color=TXTCOL)

    num_a = lambda: number_line.p2n(tuple(dot_a.get_center()))
    num_b = lambda: number_line.p2n(tuple(dot_b.get_center()))

    label_a = mn.MathTex(f"a = ", color=TXTCOL).scale(0.75)
    dec_a = CommaDecimalNumber(color=TXTCOL).scale(0.75).next_to(label_a, buff=0.15)
    dec_a.set_value(num_a())
    dec_a.add_updater(lambda dec: dec.set_value(num_a()))
    group_a = mn.VGroup(label_a, dec_a).next_to(dot_a, mn.LEFT)
    group_a.add_updater(lambda group: group.set_y(dot_a.get_y()))

    label_b = mn.MathTex(f"b = ", color=TXTCOL).scale(0.75)
    dec_b = CommaDecimalNumber(color=TXTCOL).scale(0.75).next_to(label_b, buff=0.15)
    dec_b.set_value(num_b())
    dec_b.add_updater(lambda dec: dec.set_value(num_b()))
    group_b = mn.VGroup(label_b, dec_b).next_to(dot_b, mn.RIGHT)
    group_b.add_updater(lambda group: group.set_y(dot_b.get_y()))

    num_qm = lambda: ((num_a() ** 2 + num_b() ** 2) / 2) ** 0.5
    num_am = lambda: (num_a() + num_b()) / 2
    num_gm = lambda: (num_a() * num_b()) ** 0.5
    num_hm = lambda: 2 / (1 / num_a() + 1 / num_b())

    dot_qm = mn.Dot(number_line.n2p(num_qm()), color=QMCOL)
    dot_qm.add_updater(lambda dot: dot.move_to(number_line.n2p(num_qm())))
    label_qm = mn.MathTex("QM", color=QMCOL).scale(0.5).next_to(dot_qm, mn.LEFT)

    dot_am = mn.Dot(number_line.n2p(num_am()), color=AMCOL)
    dot_am.add_updater(lambda dot: dot.move_to(number_line.n2p(num_am())))
    label_am = mn.MathTex("AM", color=AMCOL).scale(0.5).next_to(dot_am, mn.RIGHT)

    dot_gm = mn.Dot(number_line.n2p(num_gm()), color=GMCOL)
    dot_gm.add_updater(lambda dot: dot.move_to(number_line.n2p(num_gm())))
    label_gm = mn.MathTex("GM", color=GMCOL).scale(0.5).next_to(dot_gm, mn.LEFT)

    dot_hm = mn.Dot(number_line.n2p(num_hm()), color=HMCOL)
    dot_hm.add_updater(lambda dot: dot.move_to(number_line.n2p(num_hm())))
    label_hm = mn.MathTex("HM", color=HMCOL).scale(0.5).next_to(dot_hm, mn.RIGHT)

    scene.add(
        number_line,
        dot_qm,
        label_qm,
        dot_am,
        label_am,
        dot_gm,
        label_gm,
        dot_hm,
        label_hm,
        dot_a,
        group_a,
        dot_b,
        group_b,
    )

    # Equality animations

    eq_mean_equal = mn.MathTex(
        r"QM(a,b) \overset{?}{=} AM(a,b) \overset{?}{=} GM(a,b) \overset{?}{=} HM(a,b)",
        color=TXTCOL,
        tex_to_color_map={
            "QM(a,b)": QMCOL,
            "AM(a,b)": AMCOL,
            "GM(a,b)": GMCOL,
            "HM(a,b)": HMCOL,
        },
    ).shift(3 * mn.UP)

    scene.wait(1)

    scene.play(mn.Write(eq_mean_equal, run_time=3))
    scene.play(mn.FadeOut(label_qm, label_am, label_gm, label_hm), run_time=1)

    scene.play(
        geo.S.animate.move_to(geo.M.get_center()),
        geo.labelG.animate.next_to(geo.M, mn.UP, buff=0.05),
        dot_a.animate.move_to(number_line.n2p(RADIUS)),
        dot_b.animate.move_to(number_line.n2p(RADIUS)),
        rate_func=lambda t: 1 - (1 - t) ** 2,
        run_time=5,
    )

    eq_equal = mn.MathTex(r"\iff a", "=", "b", color=TXTCOL).shift(2 * mn.UP)
    eq_equal.shift(np.array([-eq_equal[1].get_x(), 0, 0]))
    scene.play(mn.Write(eq_equal), run_time=1.5)

    eq_mean_equal_2 = mn.MathTex(
        r"QM(a,b) = AM(a,b) = GM(a,b) = HM(a,b)",
        color=TXTCOL,
        tex_to_color_map={
            "QM(a,b)": QMCOL,
            "AM(a,b)": AMCOL,
            "GM(a,b)": GMCOL,
            "HM(a,b)": HMCOL,
        },
    ).shift(3 * mn.UP)

    scene.play(mn.Transform(eq_mean_equal, eq_mean_equal_2))

    scene.wait(1)

    # Part two

    # Two variable means
    eq_QM = mn.MathTex(r"\sqrt{ {{ {{ a^2 + b^2 }} \over {{ 2 }} }} }", color=QMCOL)
    eq_AM = mn.MathTex(r"{{ a + b }} \over {{ 2 }}", color=AMCOL)
    eq_GM = mn.MathTex(r"\sqrt[2]{ \hspace{0.1pt} {{ ab }} }", color=GMCOL)
    eq_HM = mn.MathTex(r"{{ 2 }} \over {{ \frac{1}{a} + \frac{1}{b} }}", color=HMCOL)

    group_eq = mn.VGroup(eq_QM, eq_AM, eq_HM, eq_GM).arrange_in_grid(
        rows=2, cols=2, buff=4
    )

    # Relations

    rel_QM_AM = mn.MathTex(r"\geq", color=TXTCOL).move_to(
        (eq_QM.get_right() + eq_AM.get_left()) / 2
    )
    rel_AM_GM = mn.MathTex(r"\leq", color=TXTCOL).move_to(
        (eq_AM.get_bottom() + eq_GM.get_top()) / 2
    )
    rel_AM_GM.rotate(mn.PI / 2)
    rel_GM_HM = mn.MathTex(r"\leq", color=TXTCOL).move_to(
        (eq_GM.get_left() + eq_HM.get_right()) / 2
    )

    group_rel = mn.VGroup(rel_QM_AM, rel_AM_GM, rel_GM_HM)

    anims = [
        mn.FadeOut(
            geo.abr, geo.bbr, geo.abrtxt, geo.bbrtxt, dec_a, dec_b
        ),  # cuz manim is buggy
        mn.FadeIn(group_eq, group_rel),
    ]

    for mobj in scene.mobjects:
        anims += [mn.FadeOut(submobj) for submobj in mobj.family_members_with_points()]

    scene.play(*anims)

    # Multi-variable means

    eq2_QM = mn.MathTex(
        r"\sqrt{ {{ {{ {a_1}^2 + {a_2}^2 + \dots + {a_n}^2 }} \over {{ n }} }} }",
        color=QMCOL,
    )
    eq2_AM = mn.MathTex(r"{{ a_1 + a_2 + \dots + a_n }} \over {{ n }}", color=AMCOL)
    eq2_GM = mn.MathTex(
        r"\sqrt[n]{ \hspace{0.1pt} {{ a_1 a_2 \ldots a_n }} }", color=GMCOL
    )
    eq2_HM = mn.MathTex(
        r"{{ n }} \over {{ \frac{1}{a_1} + \frac{1}{a_2} + \dots + \frac{1}{a_n} }}",
        color=HMCOL,
    )

    mn.VGroup(eq2_QM, eq2_AM, eq2_HM, eq2_GM).arrange_in_grid(rows=2, cols=2, buff=4)

    scene.wait(1)
    scene.play(
        mn.ReplacementTransform(eq_QM, eq2_QM),
        mn.ReplacementTransform(eq_AM, eq2_AM),
        mn.ReplacementTransform(eq_GM, eq2_GM),
        mn.ReplacementTransform(eq_HM, eq2_HM),
        rel_QM_AM.animate.move_to((eq2_QM.get_bottom() + eq2_AM.get_top()) / 2),
        rel_AM_GM.animate.move_to((eq2_AM.get_bottom() + eq2_GM.get_top()) / 2),
        rel_GM_HM.animate.move_to((eq2_GM.get_bottom() + eq2_HM.get_top()) / 2),
    )

    # Wiggle Relations
    scene.play(mn.Wiggle(group_rel), run_time=1.5)

    # Equation Relations
    rel2_QM_AM = mn.MathTex(r"=", color=TXTCOL).move_to(
        (eq_QM.get_right() + eq_AM.get_left()) / 2
    )
    rel2_AM_GM = mn.MathTex(r"=", color=TXTCOL).move_to(
        (eq_AM.get_bottom() + eq_GM.get_top()) / 2
    )
    rel2_AM_GM.rotate(mn.PI / 2)
    rel2_GM_HM = mn.MathTex(r"=", color=TXTCOL).move_to(
        (eq_GM.get_left() + eq_HM.get_right()) / 2
    )

    # Oskars krasse Gleichheitsfälle
    orel_QM_AM = rel_QM_AM.copy()
    orel_AM_GM = rel_AM_GM.copy()
    orel_GM_HM = rel_GM_HM.copy()

    scene.wait(1)

    scene.play(
        mn.Transform(rel_QM_AM, rel2_QM_AM),
        mn.Transform(rel_AM_GM, rel2_AM_GM),
        mn.Transform(rel_GM_HM, rel2_GM_HM),
        run_time=1,
    )

    scene.wait(0.75)

    eq_equality = mn.MathTex(r"\iff a_1 = a_2 = \dots = a_n", color=TXTCOL)
    scene.play(mn.Write(eq_equality), run_time=1.5)
    scene.wait(0.75)

    scene.play(
        mn.FadeOut(eq_equality),
        mn.Transform(rel_QM_AM, orel_QM_AM),
        mn.Transform(rel_AM_GM, orel_AM_GM),
        mn.Transform(rel_GM_HM, orel_GM_HM),
        run_time=1,
    )

    # Power means

    eq_PM = mn.MathTex(
        r"\sqrt[p]{ \frac{{a_1}^p + {a_2}^p + \dots + {a_n}^p}{n} }", color=TXTCOL
    )
    scene.play(mn.Write(eq_PM))

    eq_implies_QM = mn.MathTex(r"\implies", color=QMCOL)
    eq_p_QM = (
        mn.MathTex(r"p = 2", color=QMCOL).scale(-0.75).next_to(eq_implies_QM, mn.DOWN)
    )
    group_implies_QM = mn.VGroup(eq_implies_QM, eq_p_QM)
    group_implies_QM.move_to(eq_PM.get_corner(mn.UL)).shift(0.5 * mn.UL)
    group_implies_QM.rotate(3 / 4 * mn.PI)

    eq_implies_AM = mn.MathTex(r"\implies", color=AMCOL)
    eq_p_AM = (
        mn.MathTex(r"p = 1", color=AMCOL).scale(0.75).next_to(eq_implies_AM, mn.UP)
    )
    group_implies_AM = mn.VGroup(eq_implies_AM, eq_p_AM)
    group_implies_AM.move_to(eq_PM.get_corner(mn.UR)).shift(0.5 * mn.UR)
    group_implies_AM.rotate(1 / 4 * mn.PI)

    eq_implies_GM = mn.MathTex(r"\implies", color=GMCOL)
    eq_p_GM = (
        mn.MathTex(r"p \to 0", color=GMCOL).scale(0.75).next_to(eq_implies_GM, mn.UP)
    )
    group_implies_GM = mn.VGroup(eq_implies_GM, eq_p_GM)
    group_implies_GM.move_to(eq_PM.get_corner(mn.DR)).shift(0.5 * mn.DR)
    group_implies_GM.rotate(-1 / 4 * mn.PI)

    eq_implies_HM = mn.MathTex(r"\implies", color=HMCOL)
    eq_p_HM = (
        mn.MathTex(r"p = -1", color=HMCOL).scale(-0.75).next_to(eq_implies_HM, mn.DOWN)
    )
    group_implies_HM = mn.VGroup(eq_implies_HM, eq_p_HM)
    group_implies_HM.move_to(eq_PM.get_corner(mn.DL)).shift(0.5 * mn.DL)
    group_implies_HM.rotate(-3 / 4 * mn.PI)

    scene.wait(1)

    scene.play(mn.Write(group_implies_QM))
    scene.play(mn.Write(group_implies_AM))
    scene.play(mn.Write(group_implies_HM))
    scene.play(mn.Write(group_implies_GM))

    scene.wait(1)

    scene.play(
        eq2_QM.animate.scale(1.2),
        eq2_AM.animate.scale(1.2),
        eq2_GM.animate.scale(1.2),
        eq2_HM.animate.scale(1.2),
        rate_func=mn.rate_functions.there_and_back,
    )

    scene.play(
        mn.FadeOut(
            group_eq,
            group_rel,
            group_implies_QM,
            group_implies_AM,
            group_implies_GM,
            group_implies_HM,
        ),
        run_time=0.8,
    )

    # Power mean inequality

    text = mn.MathTex(
        r"\text{Für alle } {{ p }} \geq {{ q }} \text{ gilt:}",
        color=TXTCOL,
    ).shift(mn.UP)
    text[1].set_color(mn.RED)
    text[3].set_color(mn.DARK_BLUE)
    ineq_PM = mn.MathTex(
        r"\sqrt[p]{ \frac{{a_1}^p + {a_2}^p + \dots + {a_n}^p}{n} }",
        r"\geq",
        r"\sqrt[q]{ \frac{{a_1}^q + {a_2}^q + \dots + {a_n}^q}{n} }",
        color=TXTCOL,
    ).shift(0.5 * mn.DOWN)
    ineq_PM[0].set_color(mn.RED)
    ineq_PM[2].set_color(mn.DARK_BLUE)

    scene.play(
        mn.Write(text),
        eq_PM.animate.shift(0.5 * mn.DOWN),
        mn.TransformMatchingShapes(eq_PM, ineq_PM),
        run_time=1,
    )


class MainSketch(mn.Scene):
    def construct(self):
        START = int(Audio.strophe5 * 1000)
        STOP = int(Audio.refrain6 * 1000)
        if os.path.exists(Audio.path):
            self.renderer.file_writer.add_audio_segment(Audio.song[START:STOP])
        construct_scene(self)
