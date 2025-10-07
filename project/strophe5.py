from helpers import *


def construct_scene(scene: mn.Scene):
    """Konstruktion QM"""
    geo = Geo()

    # Part one

    scene.add(
        geo.qm,
        geo.gm,
        geo.am1,
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

    geo.GanzeSkizze.shift(mn.DOWN)

    # Updaters for animation

    geo.labelN.next_to(geo.N, mn.UR, buff=0.05)
    geo.labelS.add_updater(lambda label: label.next_to(geo.S, mn.UL, buff=0.05))
    geo.labelX.add_updater(lambda label: label.next_to(geo.X, mn.UL, buff=0.05))
    # geo.labelG.add_updater(lambda label: label.next_to(geo.G, mn.UR, buff=0.05))

    geo.X.add_updater(
        lambda dot: dot.move_to(
            np.array(
                [
                    geo.S.get_x(),
                    geo.M.get_y() + math.sqrt(r**2 - (geo.S.get_x()) ** 2),
                    0,
                ]
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

    scene.wait(1)

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

    scene.play(mn.Write(eq_mean_equal, run_time=3))
    scene.wait(1)

    scene.play(
        geo.S.animate.move_to(geo.M.get_center()),
        geo.labelG.animate.next_to(geo.M, mn.UP, buff=0.05),
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

    anims = [
        mn.FadeOut(geo.abr),
        mn.FadeOut(geo.bbr),
        mn.FadeOut(geo.abrtxt),
        mn.FadeOut(geo.bbrtxt),
    ]
    for mobj in scene.mobjects:
        anims.append(mn.FadeOut(mobj))

    if anims:
        scene.play(*anims)

    scene.clear()

    # Part two

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
        if mean != eq_GM:
            scene.play(mn.ReplacementTransform(eq_PM, PM_mean))
        else:
            scene.play(mn.TransformMatchingShapes(eq_PM, PM_mean))
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
        START = int(Audio.strophe5 * 1000)
        STOP = int(Audio.refrain6 * 1000)
        self.renderer.file_writer.add_audio_segment(Audio.song[START:STOP])
        construct_scene(self)
