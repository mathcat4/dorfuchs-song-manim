from helpers import *


def construct_scene(scene: mn.Scene):
    scene.add(construction, qm, gm, N, X, S, labelN, labelX, am1)

    labelN.next_to(N, mn.UR, buff=0.05)
    labelS.add_updater(lambda label: label.next_to(S, mn.UL, buff=0.05))
    labelX.add_updater(lambda label: label.next_to(X, mn.UL, buff=0.05))

    X.add_updater(
        lambda dot: dot.move_to(
            np.array([S.get_x(), M.get_y() + math.sqrt(r**2 - (S.get_x()) ** 2), 0])
        )
    )

    qm.add_updater(
        lambda line: line.put_start_and_end_on(S.get_center(), N.get_center())
    )
    gm.add_updater(
        lambda line: line.put_start_and_end_on(S.get_center(), X.get_center())
    )
    am1.add_updater(
        lambda line: line.put_start_and_end_on(M.get_center(), X.get_center())
    )

    abr.add_updater(
        lambda brace: brace.become(
            mn.Brace(
                mn.Line(start=A.get_center(), end=S.get_center()),
                direction=firsta.copy().rotate(3 * mn.PI / 2).get_unit_vector(),
                color=TXTCOL,
            )
        )
    )

    abrtxt.add_updater(lambda mobj: mobj.become(abr.get_tex("a").set_color(TXTCOL)))

    bbr.add_updater(
        lambda brace: brace.become(
            mn.Brace(
                mn.Line(start=S.get_center(), end=B.get_center()),
                direction=firsta.copy().rotate(3 * mn.PI / 2).get_unit_vector(),
                color=TXTCOL,
            )
        )
    )

    bbrtxt.add_updater(lambda mobj: mobj.become(bbr.get_tex("b").set_color(TXTCOL)))

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

    scene.play(
        S.animate.move_to(M.get_center()),
        rate_func=lambda t: 1 - (1 - t) ** 2,
        run_time=5,
    )

    eq_equal = (
        mn.MathTex(r"\implies a = b", color=TXTCOL)
        .scale(1.5)
        .shift(3 * mn.DOWN)
        .shift(0.75 * mn.LEFT)
    )
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

    fade_out(scene)

    scene.clear()

    # Two variable means
    # 4:22,33
    eq_QM = mn.MathTex(r"\sqrt{ {{ {{ a^2 + b^2 }} \over {{ 2 }} }} }", color=QMCOL)
    eq_AM = mn.MathTex(r"{{ a + b }} \over {{ 2 }}", color=AMCOL)
    eq_GM = mn.MathTex(r"\sqrt[2]{ \hspace{0.1pt} {{ ab }} }", color=GMCOL)
    eq_HM = mn.MathTex(r"{{ 2 }} \over {{ \frac{1}{a} + \frac{1}{b} }}", color=HMCOL)

    group_eq = mn.VGroup(eq_QM, eq_AM, eq_HM, eq_GM).arrange_in_grid(
        rows=2, cols=2, buff=4
    )

    # Relations

    rel_QM_AM = mn.MathTex(r"\geq", color=mn.BLACK).move_to(
        (eq_QM.get_right() + eq_AM.get_left()) / 2
    )
    rel_AM_GM = mn.MathTex(r"\leq", color=mn.BLACK).move_to(
        (eq_AM.get_bottom() + eq_GM.get_top()) / 2
    )
    rel_AM_GM.rotate(mn.PI / 2)
    rel_GM_HM = mn.MathTex(r"\leq", color=mn.BLACK).move_to(
        (eq_GM.get_left() + eq_HM.get_right()) / 2
    )

    group_rel = mn.VGroup(rel_QM_AM, rel_AM_GM, rel_GM_HM)

    scene.add(group_eq, group_rel)
    scene.wait(1)

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
    # scene.wait(13.77)
    # 36,1
    scene.play(
        mn.Transform(eq_QM, eq2_QM),
        mn.Transform(eq_AM, eq2_AM),
        mn.Transform(eq_GM, eq2_GM),
        mn.Transform(eq_HM, eq2_HM),
        rel_QM_AM.animate.move_to((eq2_QM.get_bottom() + eq2_AM.get_top()) / 2),
        rel_AM_GM.animate.move_to((eq2_AM.get_bottom() + eq2_GM.get_top()) / 2),
        rel_GM_HM.animate.move_to((eq2_GM.get_bottom() + eq2_HM.get_top()) / 2),
    )

    # 4:41,14

    # Wiggle Relations
    scene.play(mn.Wiggle(group_rel), run_time=1.5)

    # Equation Relations
    rel2_QM_AM = mn.MathTex(r"=", color=mn.BLACK).move_to(
        (eq_QM.get_right() + eq_AM.get_left()) / 2
    )
    rel2_AM_GM = mn.MathTex(r"=", color=mn.BLACK).move_to(
        (eq_AM.get_bottom() + eq_GM.get_top()) / 2
    )
    rel2_AM_GM.rotate(mn.PI / 2)
    rel2_GM_HM = mn.MathTex(r"=", color=mn.BLACK).move_to(
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

    eq_equality = mn.MathTex(r"\implies a_1 = a_2 = \dots = a_n", color=TXTCOL)
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

    # 4:46,0

    eq_PM = mn.MathTex(
        r"\sqrt[p]{ \frac{{a_1}^p + {a_2}^p + \dots + {a_n}^p}{n} }", color=mn.BLACK
    )
    eq_PM_original = eq_PM.copy()
    scene.play(mn.Write(eq_PM))

    eq_PM_QM = mn.MathTex(
        r"\sqrt[2]{ \frac{{a_1}^2 + {a_2}^2 + \dots + {a_n}^2}{n} }",
        color=QMCOL,
    )
    eq_PM_AM = mn.MathTex(
        r"\sqrt[1]{ \frac{{a_1}^1 + {a_2}^1 + \dots + {a_n}^1}{n} }",
        color=AMCOL,
    )
    eq_PM_GM = mn.MathTex(
        r"\lim_{p \to 0} {{ \sqrt[p]{ \frac{{a_1}^p + {a_2}^p + \dots + {a_n}^p}{n} } }}",
        color=GMCOL,
    )
    eq_PM_HM = mn.MathTex(
        r"\sqrt[-1]{ \frac{{a_1}^{-1} + {a_2}^{-1} + \dots + {a_n}^{-1} }{n} }",
        color=HMCOL,
    )

    for mean, PM_mean in [
        (eq_QM, eq_PM_QM),
        (eq_AM, eq_PM_AM),
        (eq_HM, eq_PM_HM),
        (eq_GM, eq_PM_GM),
    ]:
        scene.play(mn.ReplacementTransform(eq_PM, PM_mean))
        eq_PM = eq_PM_original.copy()
        scene.play(mn.Transform(PM_mean, mean), mn.FadeIn(eq_PM), run_time=0.7)
        scene.remove(PM_mean)

    scene.play(mn.FadeOut(group_eq), mn.FadeOut(group_rel))

    # Power mean inequality

    text = mn.MathTex(r"\text{Für alle } p \geq q \text{ gilt:}", color=mn.BLACK).shift(
        mn.UP
    )
    ineq_PM = mn.MathTex(
        r"\sqrt[p]{ \frac{{a_1}^p + {a_2}^p + \dots + {a_n}^p}{n} } \geq \sqrt[q]{ \frac{{a_1}^q + {a_2}^q + \dots + {a_n}^q}{n} }",
        color=mn.BLACK,
    ).shift(mn.DOWN)

    scene.play(mn.Write(text), eq_PM.animate.shift(mn.DOWN))
    scene.play(mn.TransformMatchingShapes(eq_PM, ineq_PM))


class MainSketch(mn.Scene):
    def construct(self):
        construct_scene(self)
