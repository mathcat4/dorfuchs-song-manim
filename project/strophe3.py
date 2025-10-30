from helpers import *


def construct_scene(scene: mn.Scene):
    """Konstruktion GM"""
    geo = Geo()

    scene.add(geo.qm, geo.construction, geo.N)

    term4 = mn.MathTex(r"a \cdot b", color=TXTCOL).shift(mn.UP * 3)
    term5 = mn.MathTex(r"\sqrt{ab}", color=TXTCOL).shift(mn.UP * 3)
    term6 = mn.MathTex(r"GM(a,b) =", r"\sqrt{ab}", color=GMCOL).shift(mn.UP * 3)
    # ANIMATION START 2:24,97
    scene.wait(1.77)
    # 26:74
    scene.play(mn.Write(term4), run_time=1.5)
    scene.wait(1.62)
    # 29,86
    scene.play(mn.TransformMatchingShapes(term4, term5), run_time=1)
    scene.play(
        mn.FadeIn(term6[0]),
        term5.animate.move_to(term6[1].get_center()).set_color(GMCOL),
        run_time=1.5,
    )
    scene.wait(4.7)
    # 37,06
    scene.play(mn.FadeOut(term6), mn.FadeOut(term5), run_time=1)
    scene.wait(6.14)
    # 44,2
    scene.mobjects.insert(1, geo.rightS)
    scene.mobjects.insert(1, geo.gm)
    scene.play(mn.Create(geo.gm), mn.Create(geo.rightS), run_time=1)
    scene.wait(2.48)
    # 47,68
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
    # 51,85
    scene.mobjects.insert(4, geo.rightX)  # viel hacky aber klappt lmao
    scene.play(mn.Create(geo.rightX), run_time=1)
    scene.wait(2.72)
    # 55,57
    term7 = mn.MathTex(
        r"|\overline{SX}|", r"^2", r"=", r"a", r"\cdot", r"b", color=TXTCOL
    ).shift(mn.UP * 3)

    # ZEITEN ÄNDERN WENN MICHAEL RAP FIXT
    scene.play(mn.Wiggle(geo.gm), run_time=0.5)
    scene.play(mn.ReplacementTransform(geo.gm.copy(), term7[0]), run_time=0.5)
    scene.play(mn.Wiggle(geo.gm), run_time=0.5)
    scene.play(
        mn.ReplacementTransform(geo.gm.copy(), term7[1]),
        mn.Write(typ.cast(mn.VMobject, term7[2])),
        run_time=0.5,
    )
    scene.play(mn.Wiggle(geo.sega), run_time=0.5)
    scene.play(mn.ReplacementTransform(geo.sega.copy(), term7[3]), run_time=0.5)
    scene.play(mn.Wiggle(geo.segb), run_time=0.5)
    scene.play(
        mn.ReplacementTransform(geo.segb.copy(), term7[5]),
        mn.Write(typ.cast(mn.VMobject, term7[4])),
        run_time=0.5,
    )

    scene.wait(0.1)

    term8 = mn.MathTex(
        r"{{|\overline{SX}|}}{{=}}\sqrt{{{a}}{{b}}}", color=TXTCOL
    ).shift(mn.UP * 3)
    term9 = mn.MathTex(r"|\overline{SX}| = \sqrt{ab}", r"= GM(a,b)", color=GMCOL).shift(
        mn.UP * 3
    )
    scene.play(mn.TransformMatchingTex(term7, term8))
    scene.play(mn.FadeIn(term9[1]), term8.animate.move_to(term9[0]).set_color(GMCOL))


class MainSketch(mn.Scene):
    def construct(self):
        START = int(Audio.strophe3 * 1000)
        STOP = int(Audio.refrain4 * 1000)
        if os.path.exists(Audio.path):
            self.renderer.file_writer.add_audio_segment(Audio.song[START:STOP])
        construct_scene(self)
