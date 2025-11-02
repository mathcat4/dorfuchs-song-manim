from helpers import *


def construct_scene(scene: mn.Scene):
    """
    Animation for einleitung.
    """

    # Number line

    number_line = mn.NumberLine(
        x_range=[0, 10, 1], include_numbers=True, color=TXTCOL
    ).shift(mn.DOWN)
    for num in number_line.numbers:
        num.set_color(TXTCOL)

    scene.add(number_line)

    num_a = 1.5
    num_b = 8.5

    # Draw a and b

    dot_a = mn.Dot(number_line.n2p(num_a), color=TXTCOL)
    label_a = mn.MathTex("a", color=TXTCOL).next_to(dot_a, mn.UP)

    dot_b = mn.Dot(number_line.n2p(num_b), color=TXTCOL)
    label_b = mn.MathTex("b", color=TXTCOL).next_to(dot_b, mn.UP)

    scene.wait(1.5)
    scene.play(mn.Create(dot_a), mn.Write(label_a))
    scene.wait(1)
    scene.play(mn.Create(dot_b), mn.Write(label_b))

    # Draw moving mean Dot

    dot_mean = mn.Dot(number_line.n2p((num_a + num_b) / 2), color=AMCOL)
    label_mean = mn.MathTex("M", color=AMCOL).next_to(dot_mean, mn.UP)
    label_mean.add_updater(lambda label: label.next_to(dot_mean, mn.UP))

    scene.wait(3.5)

    scene.play(mn.FadeIn(dot_mean), mn.FadeIn(label_mean))
    scene.play(
        dot_mean.animate.move_to(number_line.n2p(0.2 * num_a + 0.8 * num_b)),
        run_time=1.5,
    )
    scene.play(
        dot_mean.animate.move_to(number_line.n2p(0.8 * num_a + 0.2 * num_b)),
        run_time=1.5,
    )
    scene.play(
        dot_mean.animate.move_to(number_line.n2p((num_a + num_b) / 2)), run_time=1.5
    )

    label_mean.clear_updaters()

    # Draw the four mean dots

    dot_am = mn.Dot(number_line.n2p((num_a + num_b) / 2), color=AMCOL)
    label_am = mn.MathTex("AM", color=AMCOL).scale(0.75).next_to(dot_mean, mn.UP)

    dot_gm = mn.Dot(number_line.n2p((num_a * num_b) ** 0.5), color=GMCOL)
    label_gm = (
        mn.MathTex("GM", color=GMCOL)
        .scale(0.75)
        .next_to(dot_gm, mn.UP)
        .align_to(label_am, mn.UP)
    )

    dot_qm = mn.Dot(number_line.n2p(((num_a**2 + num_b**2) / 2) ** 0.5), color=QMCOL)
    label_qm = (
        mn.MathTex("QM", color=QMCOL)
        .scale(0.75)
        .next_to(dot_qm, mn.UP)
        .align_to(label_am, mn.UP)
    )

    dot_hm = mn.Dot(number_line.n2p((2 * num_a * num_b) / (num_a + num_b)), color=HMCOL)
    label_hm = (
        mn.MathTex("HM", color=HMCOL)
        .scale(0.75)
        .next_to(dot_hm, mn.UP)
        .align_to(label_am, mn.UP)
    )

    # Write mean descriptions

    desc_am = mn.Text("AM: Arithmetisches Mittel", color=AMCOL)
    desc_gm = mn.Text("GM: Geometrisches Mittel", color=GMCOL)
    desc_qm = mn.Text("QM: Quadratisches Mittel", color=QMCOL)
    desc_hm = mn.Text("HM: Harmonisches Mittel", color=HMCOL)

    group_desc = mn.VGroup(desc_am, desc_gm, desc_qm, desc_hm).arrange_in_grid(
        rows=2, cols=2, buff=2
    )
    group_desc.scale(0.5).shift(2 * mn.UP)

    scene.wait(0.5)
    scene.play(
        mn.Transform(dot_mean, dot_am),
        mn.Transform(label_mean, label_am),
        mn.Write(desc_am),
    )
    scene.wait(1)
    scene.play(mn.FadeIn(dot_gm), mn.FadeIn(label_gm), mn.Write(desc_gm))
    scene.wait(1)
    scene.play(mn.FadeIn(dot_qm), mn.FadeIn(label_qm), mn.Write(desc_qm))
    scene.wait(1)
    scene.play(mn.FadeIn(dot_hm), mn.FadeIn(label_hm), mn.Write(desc_hm))


class MainSketch(mn.Scene):
    def construct(self):
        START = 0
        STOP = int(Audio.refrain1 * 1000)
        if os.path.exists(Audio.path):
            self.renderer.file_writer.add_audio_segment(Audio.song[START:STOP])
        construct_scene(self)
