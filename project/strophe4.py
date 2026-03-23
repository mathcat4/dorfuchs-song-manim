from helpers import *


def construct_scene(scene: mn.Scene):
    """
    Animation for strophe 4. Konstruktion QM.
    """
    geo = Geo()
    scene.add(
        geo.qm,
        geo.am1,
        geo.construction,
        geo.gm,
        geo.N,
        geo.X,
        geo.S,
        geo.labelN,
        geo.labelX,
        geo.rightS,
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

    scene.wait(0.64)
    scene.play(
        mn.Wiggle(
            geo.AMGMDreieck,
            scale_about_point=geo.AMGMDreieck.get_center_of_mass(),
            run_time=1.33,
        )
    )
    scene.wait(0.5)
    scene.play(
        mn.Wiggle(
            geo.GMHMDreieck,
            scale_about_point=geo.GMHMDreieck.get_center_of_mass(),
            run_time=1.33,
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

    scene.wait(2)
    scene.play(mn.Wiggle(geo.hm, scale_value=1.2))

    scene.wait(4)

    # scene.play(term6.animate.move_to(mn.UP * 3))

    # Outro

    fade_out_anims = [mobj.animate.fade(1) for mobj in scene.mobjects if mobj != term6]

    geo2 = Geo()
    geo2.GMHMDreieck.shift(
        geo.construction.get_center() - geo2.construction.get_center()
    )
    scene.add(geo2.GMHMDreieck)

    hypolabel = mn.Text("Hypothenuse", font_size=24, color=GMCOL).move_to(geo2.gm)
    hypolabel.rotate(mn.PI + geo2.gm.get_angle()).shift(
        np.asarray(
            [
                -0.3 * math.cos(mn.PI / 2 - geo2.gm.get_angle()),
                -0.3 * math.sin(mn.PI / 2 - geo2.gm.get_angle()),
                0,
            ]
        )
    ).rotate(mn.PI)
    kathlabel = mn.Text("Kathete", font_size=24, color=HMCOL).move_to(geo2.hm)
    kathlabel.rotate(geo2.hm.get_angle()).shift(
        np.asarray(
            [
                0.2 * math.cos(mn.PI / 2 + geo2.hm.get_angle()),
                0.2 * math.sin(mn.PI / 2 + geo2.hm.get_angle()),
                0,
            ]
        )
    )

    move_dir = (
        Geo().GMHMDreieck.get_center() - geo2.GMHMDreieck.get_center() + 1.2 * mn.DOWN
    )
    fade_out_anims += [
        # Triangle and Label shift
        geo2.GMHMDreieck.animate.shift(move_dir),
        mn.FadeIn(hypolabel),
        mn.FadeIn(kathlabel),
        hypolabel.animate.shift(move_dir),
        kathlabel.animate.shift(move_dir),
    ]
    scene.play(*fade_out_anims, run_time=1)

    geq = (
        mn.MathTex(r"\geq", color=TXTCOL)
        .scale(0.8)
        .next_to(geo2.X.get_center(), mn.UP, buff=0.3)
    )
    fulluneq = (
        mn.MathTex(r"\text{Hypothenuse}", r"\geq", r"\text{Kathete}", color=TXTCOL)
        .scale(0.8)
        .next_to(geo2.X.get_center(), mn.UP, buff=0.3)
    )
    fulluneq.move_to(
        fulluneq.get_center() + geq.get_center() - fulluneq[1].get_center()
    )
    fulluneq[0].set_color(GMCOL)
    fulluneq[2].set_color(HMCOL)

    scene.add(hypolabel, kathlabel)
    scene.wait(1)
    scene.play(
        mn.Transform(hypolabel, fulluneq[0]),
        mn.Transform(kathlabel, fulluneq[2]),
        mn.FadeIn(geq),
    )

    # Fade out

    if __name__ == "__main__":
        scene.wait(Audio.refrain5 - Audio.strophe4 - scene.time - 1)
    else:
        scene.wait(Audio.refrain5 - scene.time - 1)

    anims = [geo2.GMHMDreieck.animate.scale(0.8, about_point=mn.ORIGIN)]
    for mobj in scene.mobjects:
        if mobj != geo2.GMHMDreieck:
            anims.append(mn.FadeOut(mobj))

    if anims:
        scene.play(*anims, run_time=1)


class MainSketch(mn.Scene):
    def construct(self):
        START = int(Audio.strophe4 * 1000)
        STOP = int(Audio.refrain5 * 1000)
        if os.path.exists(Audio.path):
            self.renderer.file_writer.add_audio_segment(Audio.song[START:STOP])
        construct_scene(self)
