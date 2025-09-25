import manim as mn
import einleitung, refrain1, refrain6, strophe1, strophe2, strophe3, strophe4, strophe5
from helpers import *


def fade_out(scene: mn.Scene):
    anims = []
    for mobj in scene.mobjects:
        anims.append(mn.FadeOut(mobj))

    if anims:
        scene.play(*anims)


class MainSketch(mn.Scene):
    def construct(self):
        # Some var
        constructionC = construction.copy()
        NC, XC, GC = N.copy(), X.copy(), G.copy()
        labelNC, labelXC = labelN.copy(), labelX.copy()
        labelGC = labelG.copy().next_to(G, mn.UP, buff=0.05).shift(0.1 * mn.RIGHT)
        QMAMDreieckC, AMGMDreieckC, GMHMDreieckC = (
            QMAMDreieck.copy(),
            AMGMDreieck.copy(),
            GMHMDreieck.copy(),
        )

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
            self,
            mObjFade=mn.VGroup(constructionC.copy(), NC.copy(), labelNC.copy()),
            mObjsWiggle={0: QMAMDreieckC.copy()},
        )
        fade_out(self)

        # Strophe 3 (GM)
        strophe3.construct_scene(self)
        fade_out(self)

        # Refrain 4
        refrain1.construct_scene(
            self,
            mObjFade=mn.VGroup(
                constructionC.copy(),
                NC.copy(),
                labelNC.copy(),
                XC.copy(),
                labelXC.copy(),
            ),
            mObjsWiggle={0: QMAMDreieckC.copy(), 1: AMGMDreieckC.copy()},
        )
        fade_out(self)

        # Strophe 4 (HM)
        strophe4.construct_scene(self)
        fade_out(self)

        # Refrain 5
        refrain1.construct_scene(
            self,
            mObjFade=mn.VGroup(
                constructionC.copy(),
                NC.copy(),
                labelNC.copy(),
                XC.copy(),
                labelXC.copy(),
                GC.copy(),
                labelGC.copy(),
            ),
            mObjsWiggle={
                0: QMAMDreieckC.copy(),
                1: AMGMDreieckC.copy(),
                2: GMHMDreieckC.copy(),
            },
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
