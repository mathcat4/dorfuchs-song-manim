from helpers import *


def construct_scene(scene: mn.Scene):
    """Konstruktion GM"""
    geo = Geo()

    geo.qm.set_opacity(0.5)
    scene.add(geo.qm, geo.construction, geo.N)

    term4 = mn.MathTex(r"a \cdot b", color=TXTCOL).shift(mn.UP * 3)
    term5 = mn.MathTex(r"\sqrt{ab}", color=TXTCOL).shift(mn.UP * 3)
    term6 = mn.MathTex(r"GM(a,b) =", r"\sqrt{ab}", color=GMCOL).shift(mn.UP * 3)
    term5.generate_target()
    assert term5.target is not None
    term5.target.move_to(term6[1].get_center())  # move into place
    term5.target.set_color(GMCOL)
    # ANIMATION START 2:24,97
    scene.wait(1.77)
    # 26:74
    scene.play(mn.Write(term4), run_time=1.5)
    scene.wait(1.62)
    # 29,86
    scene.play(mn.TransformMatchingShapes(term4, term5), run_time=1)
    scene.play(mn.FadeIn(term6[0]), mn.MoveToTarget(term5), run_time=1.5)
    scene.wait(4.7)
    # 37,06
    scene.play(mn.FadeOut(term6), mn.FadeOut(term5), run_time=1)
    scene.wait(6.14)
    # 44,2
    scene.bring_to_back(geo.gm, geo.rightS)
    scene.play(mn.Create(geo.gm), mn.Create(geo.rightS), run_time=1)
    scene.wait(2.48)
    # 47,68
    scene.play(mn.Create(geo.X), run_time=1)
    scene.play(mn.Create(geo.labelX), run_time=1)
    scene.bring_to_back(geo.am1)
    scene.play(
        mn.Create(geo.lineAX),
        mn.Create(geo.lineBX),
        mn.Create(geo.am1),
        run_time=1,
    )
    scene.wait(1.17)
    # 51,85
    scene.bring_to_front(geo.construction)
    scene.mobjects.insert(4, geo.rightAXB)  # viel hacky aber klappt lmao
    print(scene.mobjects)
    scene.play(mn.Create(geo.rightAXB), run_time=1)
    scene.wait(2.72)
    # 55,57
    term7 = mn.MathTex(
        r"{{ |\overline{SX}| }}", r"^2 {{=}}", r"{{a}} \cdot", r"{{b}}", color=TXTCOL
    ).shift(mn.UP * 3)

    # einfach ignorieren aber sonst errort alles
    term70 = typing.cast(mn.VMobject, term7[0])
    term71 = typing.cast(mn.VMobject, term7[1])
    term72 = typing.cast(mn.VMobject, term7[2])
    term73 = typing.cast(mn.VMobject, term7[3])
    term74 = typing.cast(mn.VMobject, term7[4])
    term75 = typing.cast(mn.VMobject, term7[5])

    scene.play(mn.Write(term70), mn.Wiggle(geo.gm), run_time=0.9)
    scene.play(mn.Write(term71), mn.Wiggle(geo.gm), run_time=0.9)
    scene.play(mn.Write(term72), mn.Write(term73), mn.Wiggle(geo.sega), run_time=0.9)
    scene.play(mn.Write(term74), mn.Write(term75), mn.Wiggle(geo.segb), run_time=0.9)
    scene.wait(0.5)
    term8 = mn.MathTex(
        r"{{|\overline{SX}|}} {{=}} \sqrt{{{a}}{{b}}}", color=TXTCOL
    ).shift(mn.UP * 3)
    term9 = mn.MathTex(r"|\overline{SX}| = \sqrt{ab}", r"= GM(a,b)", color=GMCOL).shift(
        mn.UP * 3
    )
    scene.play(mn.TransformMatchingTex(term7, term8))
    term8.generate_target()
    assert term8.target is not None
    term8.target.move_to(term9[0].get_center())  # move into place
    term8.target.set_color(GMCOL)
    scene.play(mn.FadeIn(term9[1]), mn.MoveToTarget(term8))


class MainSketch(mn.Scene):
    def construct(self):
        START = int(Audio.strophe3 * 1000)
        STOP = int(Audio.refrain4 * 1000)
        self.renderer.file_writer.add_audio_segment(Audio.song[START:STOP])
        construct_scene(self)
