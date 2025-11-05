from helpers import *


def construct_scene(scene: mn.Scene):
    """
    Animation for strophe 3. Konstruktion GM.
    """
    geo = Geo()
    scene.add(geo.qm, geo.construction, geo.N)

    # Equation manipulation

    term1 = mn.MathTex(r"a \cdot b", color=TXTCOL).shift(mn.UP * 3)
    scene.wait(1.77)
    scene.play(mn.Write(term1), run_time=1.5)

    term2 = mn.MathTex(r"\sqrt{ab}", color=TXTCOL).shift(mn.UP * 3)
    scene.wait(1.62)
    scene.play(mn.TransformMatchingShapes(term1, term2), run_time=1)

    term3 = mn.MathTex(r"GM(a,b) =", r"\sqrt{ab}", color=GMCOL).shift(mn.UP * 3)
    scene.play(
        mn.FadeIn(term3[0]),
        term2.animate.move_to(term3[1].get_center()).set_color(GMCOL),
        run_time=1.5,
    )

    scene.wait(4.7)
    scene.play(mn.FadeOut(term3), mn.FadeOut(term2), run_time=1)

    # Geometric construction

    scene.wait(6.14)
    scene.mobjects.insert(1, geo.rightS)
    scene.mobjects.insert(1, geo.gm)
    scene.play(mn.Create(geo.gm), mn.Create(geo.rightS), run_time=1)

    scene.wait(2.48)
    scene.play(mn.Create(geo.X), run_time=1)
    scene.play(mn.Create(geo.labelX), run_time=1)
    scene.mobjects.insert(1, geo.am1)

    lineAX = mn.Line(geo.A.get_center(), geo.X.get_center(), color=TXTCOL)
    lineBX = mn.Line(geo.B.get_center(), geo.X.get_center(), color=TXTCOL)
    scene.play(
        mn.Create(lineAX),
        mn.Create(lineBX),
        mn.Create(geo.am1),
        run_time=1,
    )

    scene.wait(1.17)
    scene.mobjects.insert(4, geo.rightX)  # viel hacky aber klappt lmao
    scene.play(mn.Create(geo.rightX), run_time=1)

    # Write equation and wiggle wiggle

    term4 = mn.MathTex(
        r"|\overline{SX}|", r"^2", r"=", r"a", r"\cdot", r"b", color=TXTCOL
    ).shift(mn.UP * 3)
    scene.wait(2.72)
    scene.play(mn.Wiggle(geo.gm), run_time=0.5)
    scene.play(mn.ReplacementTransform(geo.gm.copy(), term4[0]), run_time=0.5)

    scene.play(mn.Wiggle(geo.gm), run_time=0.5)
    scene.play(
        mn.ReplacementTransform(geo.gm.copy(), term4[1]),
        mn.Write(typ.cast(mn.VMobject, term4[2])),
        run_time=0.5,
    )

    scene.play(mn.Wiggle(geo.sega), run_time=0.5)
    scene.play(mn.ReplacementTransform(geo.sega.copy(), term4[3]), run_time=0.5)

    scene.play(mn.Wiggle(geo.segb), run_time=0.5)
    scene.play(
        mn.ReplacementTransform(geo.segb.copy(), term4[5]),
        mn.Write(typ.cast(mn.VMobject, term4[4])),
        run_time=0.5,
    )

    term5 = mn.MathTex(
        r"{{|\overline{SX}|}}{{=}}\sqrt{{{a}}{{b}}}", color=TXTCOL
    ).shift(mn.UP * 3)
    scene.wait(0.1)
    scene.play(mn.TransformMatchingTex(term4, term5))

    term6 = mn.MathTex(r"|\overline{SX}| = \sqrt{ab}", r"= GM(a,b)", color=GMCOL).shift(
        mn.UP * 3
    )
    scene.play(mn.FadeIn(term6[1]), term5.animate.move_to(term6[0]).set_color(GMCOL))

    anims = []
    for mobj in scene.mobjects:
        if mobj != term6[1] and mobj != term5:
            anims.append(mn.FadeOut(mobj))

    scene.play(*anims, run_time=0.5)
    geo2 = Geo()

    geo2.AMGMDreieck.move_to(geo2.AMGMDreieck.get_center() - geo2.AMGMDreieck.get_center_of_mass())
    geo2.AMGMDreieck.shift(2*mn.DOWN)
    scene.add(geo2.AMGMDreieck)

    geq = mn.MathTex(r"\leq", color = TXTCOL).next_to(geo2.X.get_center(), mn.UP, buff=0.3).set_x(0)
    fulluneq = mn.MathTex(r"\text{Kathete}",r"\leq", r"\text{Hypothenuse}", color = TXTCOL).next_to(geo2.X.get_center(), mn.UP, buff=0.3)
    fulluneq.move_to(fulluneq.get_center() +geq.get_center() -fulluneq[1].get_center())
    fulluneq[0].set_color(GMCOL)
    fulluneq[2].set_color(AMCOL)

    hypolabel = mn.Text("Hypothenuse", font_size=24, color = AMCOL).move_to(geo2.am1)
    hypolabel.rotate(geo2.am1.get_angle()).shift( (0.3*math.cos(mn.PI/2 - geo2.am1.get_angle()), 0.3*math.sin(mn.PI/2 - geo2.am1.get_angle()), 0) ).rotate(mn.PI)
    kathlabel = mn.Text("Kathete", font_size=24, color = GMCOL).move_to(geo2.gm)
    kathlabel.rotate(geo2.gm.get_angle()).shift( (0.2*math.cos(mn.PI/2 + geo2.gm.get_angle()), 0.2*math.sin(mn.PI/2 + geo2.gm.get_angle()), 0) )
    scene.add(hypolabel, kathlabel)
    scene.wait(1)
    scene.play(mn.Transform(hypolabel, fulluneq[2]), mn.Transform(kathlabel, fulluneq[0]), mn.FadeIn(geq))


class MainSketch(mn.Scene):
    def construct(self):
        START = int(Audio.strophe3 * 1000)
        STOP = int(Audio.refrain4 * 1000)
        if os.path.exists(Audio.path):
            self.renderer.file_writer.add_audio_segment(Audio.song[START:STOP])
        construct_scene(self)
