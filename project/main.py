import manim as mn
import einleitung, refrain1, refrain6, strophe1, strophe2, strophe3, strophe4, strophe5
from helpers import *


def fade_out(scene: mn.Scene, run_time=1):
    anims = []
    for mobj in scene.mobjects:
        anims.append(mn.FadeOut(mobj, run_time=run_time))

    if anims:
        scene.play(*anims)


class MainSketch(mn.Scene):
    def construct(self):
        fade_duration = 1

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

        # Refrain 1
        self.wait(26.9 - self.time - fade_duration)
        fade_out(self, run_time=fade_duration)
        refrain1.construct_scene(self)

        # Strophe 1 (AM)
        self.wait(44.69 - self.time - fade_duration)
        fade_out(self)
        strophe1.construct_scene(self)

        # Refrain 2
        self.wait(65.39 - self.time - fade_duration)
        fade_out(self)
        refrain1.construct_scene(self)

        return

        # Strophe 2 (QM)
        self.wait(26.9 - self.time)
        fade_out(self)
        strophe2.construct_scene(self)

        # Refrain 3
        self.wait(26.9 - self.time)
        fade_out(self)
        refrain1.construct_scene(
            self,
            mObjFade=mn.VGroup(constructionC.copy(), NC.copy(), labelNC.copy()),
            mObjsWiggle={0: QMAMDreieckC.copy()},
        )

        # Strophe 3 (GM)
        self.wait(26.9 - self.time)
        fade_out(self)
        strophe3.construct_scene(self)

        # Refrain 4
        self.wait(26.9 - self.time)
        fade_out(self)
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

        # Strophe 4 (HM)
        self.wait(26.9 - self.time)
        fade_out(self)
        strophe4.construct_scene(self)

        # Refrain 5
        self.wait(26.9 - self.time)
        fade_out(self)
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

        # Strophe 5 (Ausblick)
        self.wait(26.9 - self.time)
        fade_out(self)
        strophe5.construct_scene(self)

        # Refrain 6
        self.wait(26.9 - self.time)
        fade_out(self)
        refrain6.construct_scene(self)

        # Refrain 7
        self.wait(26.9 - self.time)
        refrain6.construct_scene(self, reverse=True)
