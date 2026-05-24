from helpers import *


def construct_scene(scene: mn.Scene, debug: bool = False):
    """
    Animation for strophe 4. Konstruktion QM.
    """
    geo = Geo()
    scene.add(
        geo.rightS,
        geo.qm,
        geo.am1,
        geo.construction,
        geo.gm,
        geo.N,
        geo.X,
        geo.S,
        geo.labelN,
        geo.labelX,
    )
    geo.GanzeSkizze.shift(2 * mn.LEFT)

    scene.wait(1)
    tex1 = mn.MathTex(
        r"HM(a,b) = \frac{2}{\frac{1}{a} + \frac{1}{b}}", color=HMCOL
    ).shift(mn.UP * 3 + mn.LEFT * 2)
    scene.play(mn.Write(tex1), run_time=2)

    scene.wait(2.56)
    scene.play(
        mn.Create(geo.lineSG),
        mn.Create(geo.G),
        mn.Create(geo.labelG),
        run_time=1,
    )
    scene.mobjects.insert(2, geo.hm)
    scene.play(mn.Create(geo.rightG), mn.Create(geo.hm), run_time=1)
    scene.play(mn.Create(geo.angleX), mn.Create(geo.angleXlabel), run_time=1)

    scene.wait(0.44)
    scene.play(mn.Wiggle(geo.angXl, scale_value=1.5), run_time=1.5)
    scene.play(
        mn.Wiggle(geo.rightG, scale_value=1.5),
        mn.Wiggle(geo.rightS, scale_value=1.5),
        run_time=2,
    )
    scene.play(mn.FadeOut(tex1), run_time=1)

    # scene.add(geo.sega, geo.angleX)  # zauberfunktionfix
    # zauberfunktion(scene, geo.GanzeSkizze, lambda m: m.shift(mn.LEFT * 3))

    scene.wait(1.3)
    scene.play(
        mn.Wiggle(
            geo.AMGMDreieck,
            scale_about_point=geo.AMGMDreieck.get_center_of_mass(),
            n_wiggles=4,
            run_time=1,
        )
    )
    scene.wait(0.5)
    scene.play(
        mn.Wiggle(
            geo.GMHMDreieck,
            scale_about_point=geo.GMHMDreieck.get_center_of_mass(),
            n_wiggles=4,
            run_time=1,
        )
    )

    # Equation manipulation

    term1 = mn.MathTex(
        r"{ {{|\overline{XG}|}} {{\over}} |\overline{XS}|} {{=}} {|\overline{XS}| {{\over}} |\overline{XM}|}",
        color=TXTCOL,
    ).move_to(mn.UP * 3)
    scene.play(mn.Write(term1), run_time=1.6)

    term2 = mn.MathTex(
        r"{ {{|\overline{XG}|}} {{\over}} \sqrt{ab} } {{=}} {\sqrt{ab} {{\over}}  {{ {a+b \over 2} }} }",
        color=TXTCOL,
    ).move_to(mn.UP * 3)
    scene.wait(0.38)
    scene.play(mn.TransformMatchingTex(term1, term2))

    term3 = mn.MathTex(
        r"{{|\overline{XG}|}} {{=}} { {{ab}} {{\over}}   {{ {a+b \over 2} }}   }",
        color=TXTCOL,
    ).move_to(mn.UP * 3)
    scene.play(mn.TransformMatchingTex(term2, term3))

    term4 = mn.MathTex(
        r"{{|\overline{XG}|}} {{=}} { {{ab}} \cdot \frac{2}{ab} {{\over}}   {{ {a+b \over 2} }}  \cdot \frac{2}{ab} }",
        color=TXTCOL,
    ).move_to(mn.UP * 3)
    scene.play(mn.TransformMatchingTex(term3, term4))

    term5 = mn.MathTex(
        r"{{|\overline{XG}|}} {{=}} { 2 {{\over}} {1 \over a} {{+}} {1 \over b}}",
        color=TXTCOL,
    ).move_to(mn.UP * 3)
    scene.play(mn.TransformMatchingTex(term4, term5))

    term6 = mn.MathTex(
        r"{{|\overline{XG}|}} {{=}} { 2 {{\over}} {1 \over a} {{+}} {1 \over b}} = HM(a,b)",
        color=HMCOL,
    ).move_to(mn.UP * 3)
    scene.play(mn.TransformMatchingShapes(term5, term6))

    scene.wait(2.8)
    scene.play(mn.Wiggle(geo.hm, scale_value=1.2, n_wiggles=8))

    scene.wait(3.2)

    # scene.play(term6.animate.move_to(mn.UP * 3))

    # Outro

    geo2 = Geo()
    triangle = geo2.GMHMDreieck

    group_move = mn.VGroup(
        geo2.qm,
        geo2.construction,
        geo2.N,
        geo2.labelN,
        geo2.X,
        geo2.labelX,
        geo2.labelG,
        geo2.AMGMDreieck,
        triangle,
        geo2.angXl,
    )

    group_move.shift(geo.construction.get_center() - geo2.construction.get_center())
    scene.add(group_move)

    for mobj in scene.mobjects:
        if mobj != term6:
            scene.remove(mobj)

    hypoangle = geo2.gm.get_angle()
    kathangle = geo2.hm.get_angle()

    hypolabel = mn.MathTex(r"\text{Hypothenuse}", color=GMCOL).scale(0.8)
    hypolabel.rotate(hypoangle).move_to(geo2.gm)
    hypolabel.shift(
        np.asarray(
            [
                0.25 * math.cos(mn.PI / 2 + hypoangle),
                0.25 * math.sin(mn.PI / 2 + hypoangle),
                0,
            ]
        )
    )

    kathlabel = mn.MathTex(r"\text{Kathete}", color=HMCOL).scale(0.8)
    kathlabel.rotate(kathangle).move_to(geo2.hm)
    kathlabel.shift(
        np.asarray(
            [
                0.2 * math.cos(mn.PI / 2 + kathangle),
                0.2 * math.sin(mn.PI / 2 + kathangle),
                0,
            ]
        )
    )

    move_dir = (
        Geo().construction.get_center() - geo2.construction.get_center() + 1.2 * mn.DOWN
    )
    fade_out_anims = [
        # Labels shift
        mn.FadeIn(hypolabel),
        mn.FadeIn(kathlabel),
        hypolabel.animate.shift(move_dir),
        kathlabel.animate.shift(move_dir),
    ]

    for mobj in group_move:
        if mobj == triangle:
            fade_out_anims.append(mobj.animate.shift(move_dir))
        else:
            fade_out_anims.append(mobj.animate.fade(0.8).shift(move_dir))

    scene.play(*fade_out_anims, run_time=1)

    geq = (
        mn.MathTex(r"\geq", color=TXTCOL)
        .scale(0.8)
        .next_to(geo2.X.get_center(), mn.UP, buff=0.4)
    )
    fullineq = (
        mn.MathTex(r"\text{Hypothenuse}", r"\geq", r"\text{Kathete}", color=TXTCOL)
        .scale(0.8)
        .next_to(geo2.X.get_center(), mn.UP, buff=0.4)
    )
    fullineq.move_to(
        fullineq.get_center() + geq.get_center() - fullineq[1].get_center()
    )
    fullineq[0].set_color(GMCOL)
    fullineq[2].set_color(HMCOL)

    scene.add(hypolabel, kathlabel)
    scene.wait(1)
    scene.play(
        hypolabel.animate.rotate(-hypoangle).move_to(fullineq[0]),
        kathlabel.animate.rotate(-kathangle).move_to(fullineq[2]),
        mn.FadeIn(geq),
    )

    # Fade out

    if not debug:
        scene.wait(Audio.refrain5 - scene.time - 1)
    else:
        scene.wait(Audio.refrain5 - Audio.strophe4 - scene.time - 1)

    anims = [group_move.animate.scale(FIGURE_SCALE, about_point=mn.ORIGIN)]

    add_objs = [geo2.am2, geo2.rightM]
    for mobj in add_objs:
        mobj.shift(1.2 * mn.DOWN)
        anims.append(mn.FadeIn(mobj))

    keep_objs = [
        geo2.construction,
        geo2.N,
        geo2.labelN,
        geo2.X,
        geo2.QMAMDreieck,
        geo2.AMGMDreieck,
        geo2.labelX,
        geo2.labelG,
    ]
    keep_family = set()
    for obj in keep_objs:
        keep_family.update(obj.get_family())

    for mobj in scene.mobjects:
        if mobj in keep_family:
            anims.append(mobj.animate.fade(-4))
        elif mobj != triangle:
            anims.append(mn.FadeOut(mobj))

    scene.mobjects.insert(1, geo2.am2)
    scene.mobjects.insert(1, geo2.rightM)
    scene.play(*anims, run_time=1)


class MainSketch(mn.Scene):
    def construct(self):
        START = int((Audio.strophe4 - 0.6) * 1000)
        STOP = int(Audio.refrain5 * 1000)
        if os.path.exists(Audio.path):
            self.renderer.file_writer.add_audio_segment(Audio.song[START:STOP])
        construct_scene(self, debug=True)
