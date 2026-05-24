from helpers import *


def construct_scene(scene: mn.Scene, debug: bool = False):
    """
    Animation for strophe 3. Konstruktion GM.
    """
    geo = Geo()
    scene.add(geo.qm, geo.construction, geo.N)
    geo.GanzeSkizze.shift(2 * mn.LEFT)

    # Equation manipulation

    term1 = mn.MathTex(r"a \cdot b", color=TXTCOL).shift(mn.UP * 3 + mn.LEFT * 2)
    scene.wait(2.27)
    scene.play(mn.Write(term1), run_time=1.5)

    term2 = mn.MathTex(r"\sqrt{ab}", color=TXTCOL).shift(mn.UP * 3 + mn.LEFT * 2)
    scene.wait(1.62)
    scene.play(mn.TransformMatchingShapes(term1, term2), run_time=1)

    term3 = mn.MathTex(r"GM(a,b) =", r"\sqrt{ab}", color=GMCOL).shift(
        mn.UP * 3 + mn.LEFT * 2
    )
    scene.play(
        mn.FadeIn(term3[0]),
        term2.animate.move_to(term3[1].get_center()).set_color(GMCOL),
        run_time=1.5,
    )

    scene.wait(4.2)
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

    scene.play(
        mn.Create(geo.lineAX),
        mn.Create(geo.lineBX),
        mn.Create(geo.am1),
        run_time=1,
    )

    scene.wait(1.17)
    scene.mobjects.insert(4, geo.rightX)  # viel hacky aber klappt lmao
    scene.play(mn.Create(geo.rightX), run_time=1)

    # Write equation and wiggle wiggle

    term4 = mn.MathTex(r"|\overline{SX}|", r"^2", r"=", r"a", r"b", color=TXTCOL).shift(
        mn.UP * 3 + mn.LEFT * 2
    )
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
        mn.ReplacementTransform(geo.segb.copy(), term4[4]),
        # mn.Write(typ.cast(mn.VMobject, term4[4])),
        run_time=0.5,
    )

    term5 = mn.MathTex(r"|\overline{SX}|", r"=", r"\sqrt{ ab }", color=TXTCOL).shift(
        mn.UP * 3 + mn.LEFT * 2
    )
    scene.wait(0.1)
    scene.play(
        mn.TransformMatchingShapes(term4[0], term5[0]),
        mn.FadeOut(term4[1]),
        mn.TransformMatchingShapes(term4[2], term5[1]),
        mn.FadeIn(term5[2][0:2]),
        mn.TransformMatchingShapes(term4[3:], term5[2][2:]),
    )

    term6 = mn.MathTex(r"|\overline{SX}| = \sqrt{ab}", r"= GM(a,b)", color=GMCOL).shift(
        mn.UP * 3
    )

    # Outro Zeugs

    geo2 = Geo()
    triangle = geo2.AMGMDreieck

    group_move = mn.VGroup(
        geo2.qm,
        geo2.construction,
        geo2.N,
        geo2.X,
        geo2.labelX,
        triangle,
        geo2.rightX,
        geo2.lineAX,
        geo2.lineBX,
    )

    group_move.shift(geo.construction.get_center() - geo2.construction.get_center())
    scene.add(group_move)

    for mobj in scene.mobjects:
        if mobj not in (term6[1], term5):
            scene.remove(mobj)

    hypoangle = mn.PI + geo2.am1.get_angle()
    kathangle = geo2.gm.get_angle()

    hypolabel = mn.MathTex(r"\text{Hypothenuse}", color=AMCOL).scale(0.8)

    hypolabel.rotate(hypoangle).move_to(geo2.am1)
    hypolabel.shift(
        np.asarray(
            [
                0.25 * math.cos(mn.PI / 2 + hypoangle),
                0.25 * math.sin(mn.PI / 2 + hypoangle),
                0,
            ]
        )
    )

    kathlabel = mn.MathTex(r"\text{Kathete}", color=GMCOL).scale(0.8)
    kathlabel.rotate(kathangle).move_to(geo2.gm)
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
        # Other anims
        mn.FadeIn(term6[1]),
        term5.animate.move_to(term6[0]).set_color(GMCOL),
    ]

    for mobj in group_move:
        if mobj == triangle:
            fade_out_anims.append(mobj.animate.shift(move_dir))
        else:
            fade_out_anims.append(mobj.animate.fade(0.8).shift(move_dir))

    scene.play(*fade_out_anims, run_time=1)

    geq = (
        mn.MathTex(r"\leq", color=TXTCOL)
        .scale(0.8)
        .next_to(geo2.X.get_center(), mn.UP, buff=0.4)
    )
    fullineq = (
        mn.MathTex(r"\text{Kathete}", r"\leq", r"\text{Hypothenuse}", color=TXTCOL)
        .scale(0.8)
        .next_to(geo2.X.get_center(), mn.UP, buff=0.4)
    )
    fullineq.move_to(
        fullineq.get_center() + geq.get_center() - fullineq[1].get_center()
    )
    fullineq[0].set_color(GMCOL)
    fullineq[2].set_color(AMCOL)

    scene.wait(1)
    scene.play(
        hypolabel.animate.rotate(-hypoangle).move_to(fullineq[2]),
        kathlabel.animate.rotate(-kathangle).move_to(fullineq[0]),
        mn.FadeIn(geq),
    )

    # Fade out

    if not debug:
        scene.wait(Audio.refrain4 - scene.time - 1)
    else:
        scene.wait(Audio.refrain4 - Audio.strophe3 - scene.time - 1)

    anims = [group_move.animate.scale(FIGURE_SCALE, about_point=mn.ORIGIN)]

    add_objs = [geo2.am2, geo2.rightM, geo2.labelN]
    for mobj in add_objs:
        mobj.shift(1.2 * mn.DOWN)
        anims.append(mn.FadeIn(mobj))

    keep_objs = [
        geo2.construction,
        geo2.N,
        geo2.labelN,
        geo2.X,
        geo2.labelX,
        geo2.qm,
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
        START = int((Audio.strophe3 - 0.45) * 1000)
        STOP = int(Audio.refrain4 * 1000)
        if os.path.exists(Audio.path):
            self.renderer.file_writer.add_audio_segment(Audio.song[START:STOP])
        construct_scene(self, debug=True)
