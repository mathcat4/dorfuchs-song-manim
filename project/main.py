import manim as mn
import einleitung, refrain1, refrain6, strophe1, strophe2, strophe3, strophe4, strophe5
from helpers import *
import os


def fade_out(scene: mn.Scene, run_time=1):
    anims = []
    for mobj in scene.mobjects:
        anims.append(mn.FadeOut(mobj, run_time=run_time))

    if anims:
        scene.play(*anims)


refrain1_start = 26.9
strophe1_start = 44.69
refrain2_start = 1 * 60 + 5.39
strophe2_start = 1 * 60 + 22.97
refrain3_start = 2 * 60 + 7
strophe3_start = 2 * 60 + 24.97
refrain4_start = 3 * 60 + 6.5
strophe4_start = 3 * 60 + 24.04
refrain5_start = 4 * 60 + 4
strophe5_start = 4 * 60 + 22.33
refrain6_start = 5 * 60 + 00.58
refrain7_start = 5 * 60 + 16.6


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
        AUDIO_PATH = "media/Audio/finalpremix.wav"
        if os.path.exists(AUDIO_PATH):
            self.add_sound(AUDIO_PATH, time_offset=0)


        # Einleitung
        einleitung.construct_scene(self)

        # Refrain 1
        self.wait(refrain1_start - self.time - fade_duration)
        fade_out(self, run_time=fade_duration)
        refrain1.construct_scene(self)

        # Strophe 1 (AM)
        self.wait(strophe1_start - self.time - fade_duration)
        fade_out(self)
        strophe1.construct_scene(self)

        # Refrain 2
        self.wait(refrain2_start - self.time - fade_duration)
        fade_out(self)
        refrain1.construct_scene(self)

        # return

        # Strophe 2 (QM)
        self.wait(strophe2_start - self.time - fade_duration)
        fade_out(self)
        strophe2.construct_scene(self)

        # Refrain 3
        self.wait(refrain3_start - self.time - fade_duration)
        fade_out(self)
        refrain1.construct_scene(
            self,
            mObjFade=mn.VGroup(constructionC.copy(), NC.copy(), labelNC.copy()),
            mObjsWiggle={0: QMAMDreieckC.copy()},
        )

        # Strophe 3 (GM)
        self.wait(strophe3_start - self.time - fade_duration)
        fade_out(self)
        strophe3.construct_scene(self)

        # Refrain 4
        self.wait(refrain4_start - self.time - fade_duration)
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
        self.wait(strophe4_start - self.time - fade_duration)
        fade_out(self)
        strophe4.construct_scene(self)

        # Refrain 5
        self.wait(refrain5_start - self.time - fade_duration)
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
        self.wait(strophe5_start - self.time - fade_duration)
        fade_out(self)
        strophe5.construct_scene(self)

        # Refrain 6
        self.wait(refrain6_start - self.time - fade_duration)
        fade_out(self)
        refrain6.construct_scene(self)

        # Refrain 7
        self.wait(refrain7_start - self.time)
        refrain6.construct_scene(self, reverse=True)
