import manim as mn
import einleitung, refrain1, refrain6, strophe1, strophe2, strophe3, strophe4, strophe5


def fade_out(scene):
    anims = []
    for mobj in scene.mobjects:
        anims.append(mn.FadeOut(mobj))

    if anims:
        scene.play(*anims)


class MainSketch(mn.Scene):
    def construct(self):

        # Einleitung
        einleitung.construct_scene(self)
        fade_out(self)

        # Refrain 1
        refrain1.construct_scene(self)
        fade_out(self)

        # Strophe 1 (AM)
        strophe1.construct_scene(self)
        fade_out(self)

        # Refrain 2
        refrain1.construct_scene(self)
        fade_out(self)

        # Strophe 2 (QM)
        strophe2.construct_scene(self)
        fade_out(self)

        # Refrain 3
        refrain1.construct_scene(
            self, shift=True, mObjs={0: mn.Square(2, color=mn.BLACK)}
        )
        fade_out(self)

        # Strophe 3 (GM)
        strophe3.construct_scene(self)
        fade_out(self)

        # Refrain 4
        refrain1.construct_scene(
            self, shift=True, mObjs={1: mn.Square(2, color=mn.BLACK)}
        )
        fade_out(self)

        # Strophe 4 (HM)
        strophe4.construct_scene(self)
        fade_out(self)

        # Refrain 5
        refrain1.construct_scene(
            self, shift=True, mObjs={2: mn.Square(2, color=mn.BLACK)}
        )
        fade_out(self)

        # Strophe 5 (Ausblick)
        strophe5.construct_scene(self)
        fade_out(self)

        # Refrain 6
        refrain6.construct_scene(self)
        fade_out(self)

        # Refrain 7
        refrain6.construct_scene(self, reverse=True)
