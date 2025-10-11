import manim as mn
import einleitung, refrain1, refrain6, strophe1, strophe2, strophe3, strophe4, strophe5
from helpers import *
import os


class MainSketch(mn.Scene):
    def construct(self):
        fade_duration = 1

        # manim kinda doesn't cook otherwise
        self.renderer.file_writer.add_audio_segment(Audio.song)

        # Einleitung
        einleitung.construct_scene(self)

        # Refrain 1
        self.wait(Audio.refrain1 - self.time - fade_duration)
        fade_out(self, run_time=fade_duration)
        refrain1.construct_scene(self)

        # Strophe 1 (AM)
        self.wait(Audio.strophe1 - self.time - fade_duration)
        fade_out(self, run_time=fade_duration)
        strophe1.construct_scene(self)

        # Refrain 2
        self.wait(Audio.refrain2 - self.time - fade_duration)
        fade_out(self, run_time=fade_duration)
        refrain1.construct_scene(self)

        # return

        # Strophe 2 (QM)
        self.wait(Audio.strophe2 - self.time - fade_duration)
        fade_out(self, run_time=fade_duration)
        strophe2.construct_scene(self)

        # Refrain 3
        self.wait(Audio.refrain3 - self.time - fade_duration)
        fade_out(self, run_time=fade_duration)
        geo = Geo()
        refrain1.construct_scene(
            self,
            ext_objs=mn.VGroup(geo.construction, geo.N, geo.labelN, geo.QMAMDreieck),
            mObjsFocus={0: geo.QMAMDreieck},
        )

        # Strophe 3 (GM)
        self.wait(Audio.strophe3 - self.time - fade_duration)
        fade_out(self, run_time=fade_duration)
        strophe3.construct_scene(self)

        # Refrain 4
        self.wait(Audio.refrain4 - self.time - fade_duration)
        fade_out(self, run_time=fade_duration)
        geo = Geo()
        refrain1.construct_scene(
            self,
            ext_objs=mn.VGroup(
                geo.construction,
                geo.N,
                geo.labelN,
                geo.X,
                geo.labelX,
                geo.QMAMDreieck,
                geo.AMGMDreieck,
            ),
            mObjsFocus={0: geo.QMAMDreieck, 1: geo.AMGMDreieck},
        )

        # Strophe 4 (HM)
        self.wait(Audio.strophe4 - self.time - fade_duration)
        fade_out(self, run_time=fade_duration)
        strophe4.construct_scene(self)

        # Refrain 5
        self.wait(Audio.refrain5 - self.time - fade_duration)
        fade_out(self, run_time=fade_duration)
        geo = Geo()
        refrain1.construct_scene(
            self,
            ext_objs=mn.VGroup(
                geo.construction,
                geo.N,
                geo.labelN,
                geo.X,
                geo.labelX,
                geo.G,
                geo.labelG,
                geo.QMAMDreieck,
                geo.AMGMDreieck,
                geo.GMHMDreieck,
            ),
            mObjsFocus={
                0: geo.QMAMDreieck,
                1: geo.AMGMDreieck,
                2: geo.GMHMDreieck,
            },
        )

        # Strophe 5 (Ausblick)
        self.wait(Audio.strophe5 - self.time - fade_duration)
        fade_out(self, run_time=fade_duration)
        strophe5.construct_scene(self)

        # Refrain 6
        self.wait(Audio.refrain6 - self.time - fade_duration)
        fade_out(self, run_time=fade_duration)
        refrain6.construct_scene(self)

        # Refrain 7
        self.wait(Audio.refrain7 - self.time - fade_duration)
        fade_out(self, run_time=fade_duration)
        refrain6.construct_scene(self, reverse=True)
