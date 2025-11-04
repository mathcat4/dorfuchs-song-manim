import manim as mn
import numpy as np
import typing as typ
import math
import pydub
import warnings
import os

# Settings and constants

mn.config.background_color = mn.WHITE
TXTCOL = mn.BLACK
AMCOL = mn.ORANGE
GMCOL = mn.GREEN_D
QMCOL = mn.BLUE_D
HMCOL = mn.PURPLE_D
RIGHTANGLECOL = mn.GREY
ANGLECOL = mn.PINK
RIGHT_HALF_CENTER = mn.ORIGIN + mn.RIGHT * mn.config.frame_x_radius / 2
LEFT_HALF_CENTER = mn.ORIGIN + mn.LEFT * mn.config.frame_x_radius / 2

# Helper functions and classes


def fadeout_all(scene: mn.Scene, run_time: float = 1):
    """
    Fadeout all objects in the scene.
    """
    anims = []
    for mobj in scene.mobjects:
        anims.append(mn.FadeOut(mobj))

    if anims:
        scene.play(*anims, run_time=run_time)


def zauberfunktion(scene: mn.Scene, group: mn.VGroup, anim_fn: typ.Callable):
    """
    Apply a function to a group, but like cooler and works.
    Please only use homogenous animations.
    """
    visible_parts = [m for m in group if m in scene.mobjects]
    hidden_parts = [m for m in group if m not in scene.mobjects]

    # Apply transformation instant to hidden parts
    for m in hidden_parts:
        anim_fn(m)

    # Animate visible parts
    scene.play(*[anim_fn(m.animate) for m in visible_parts])


def TransformMatchingTexNoReplace(src: mn.Mobject, target: mn.Mobject, **kwargs):
    """
    Transform a *copy* of `src` into `target`, leaving `src` unchanged.
    """
    src_copy = src.copy()
    return mn.TransformMatchingTex(src_copy, target, **kwargs)


def TransformMatchingShapesNoReplace(src: mn.Mobject, target: mn.Mobject, **kwargs):
    """
    Transform a *copy* of `src` into `target`, leaving `src` unchanged.
    """
    src_copy = src.copy()
    return mn.TransformMatchingShapes(src_copy, target, **kwargs)


class CommaDecimalNumber(mn.DecimalNumber):
    """
    A DecimalNumber mobject but using a comma.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _get_num_string(self, number):
        return super()._get_num_string(number).replace(".", ",")


class Geo:
    """
    Generates the main construction used in the animation.
    """

    RADIUS = 3
    A_VAL = 1.3
    X_SHIFT = 0
    Y_SHIFT = -1.5

    def __init__(self):
        # Punkte
        self.M = mn.Dot((self.X_SHIFT, self.Y_SHIFT, 0), color=TXTCOL)
        self.A = mn.Dot((-self.RADIUS, 0, 0) + self.M.get_center(), color=TXTCOL)
        self.B = mn.Dot((self.RADIUS, 0, 0) + self.M.get_center(), color=TXTCOL)
        self.S = mn.Dot((-self.A_VAL, 0, 0) + self.M.get_center(), color=TXTCOL)
        self.N = mn.Dot((0, self.RADIUS, 0) + self.M.get_center(), color=TXTCOL)
        cord = self.M.get_y() + math.sqrt(
            self.RADIUS**2 - (self.M.get_x() - self.S.get_x()) ** 2
        )
        self.X = mn.Dot((self.S.get_x(), cord, 0), color=TXTCOL)
        self.G = mn.Dot(
            mn.Line(self.M.get_center(), self.X.get_center()).get_projection(
                self.S.get_center()
            ),
            color=TXTCOL,
        )

        # Linien und so
        self.sega = mn.Line(
            start=self.A.get_center(), end=self.S.get_center(), color=TXTCOL
        )
        self.segb = mn.Line(
            start=self.S.get_center(), end=self.B.get_center(), color=TXTCOL
        )
        self.semikreis = mn.Arc(
            radius=self.RADIUS,
            start_angle=0,
            angle=mn.PI,
            arc_center=self.M.get_center(),
            color=TXTCOL,
        )

        self.gm = mn.Line(self.S.get_center(), self.X.get_center(), color=GMCOL)
        self.am1 = mn.Line(self.M.get_center(), self.X.get_center(), color=AMCOL)
        self.am2 = mn.Line(self.M.get_center(), self.N.get_center(), color=AMCOL)
        self.am3 = mn.Line(self.M.get_center(), self.A.get_center(), color=AMCOL)
        self.qm = mn.Line(self.S.get_center(), self.N.get_center(), color=QMCOL)
        self.hm = mn.Line(self.X.get_center(), self.G.get_center(), color=HMCOL)

        self.lineMS = mn.Line(self.M.get_center(), self.S.get_center(), color=TXTCOL)
        self.lineSG = mn.DashedLine(
            self.S.get_center(), self.G.get_center(), color=TXTCOL, stroke_width=3
        )

        # Labels
        self.labelM = mn.MathTex("M", font_size=24, color=TXTCOL)
        self.labelM.next_to(self.M, mn.UR, buff=0.05)

        self.labelS = mn.MathTex("S", font_size=24, color=TXTCOL)
        self.labelS.next_to(self.S, mn.UL, buff=0.05)

        self.labelN = mn.MathTex("N", font_size=24, color=TXTCOL)
        self.labelN.next_to(self.N, mn.UL, buff=0.05)

        self.labelX = mn.MathTex("X", font_size=24, color=TXTCOL)
        self.labelX.next_to(self.X, mn.UL, buff=0.05)

        self.labelG = mn.MathTex("G", font_size=24, color=TXTCOL)
        self.labelG.next_to(self.G, mn.UR, buff=0.05)

        # Braces
        self.abr = mn.Brace(self.sega, direction=mn.DOWN, color=TXTCOL)
        self.abrtxt = self.abr.get_tex("a")
        self.abrtxt.set_color(TXTCOL)

        self.bbr = mn.Brace(self.segb, direction=mn.DOWN, color=TXTCOL)
        self.bbrtxt = self.bbr.get_tex("b")
        self.bbrtxt.set_color(TXTCOL)

        # Winkel
        self.rightX = mn.Angle(
            mn.Line(self.X, self.A),
            mn.Line(self.X, self.B),
            radius=0.5,
            other_angle=False,
            dot=True,
            dot_color=RIGHTANGLECOL,
            color=RIGHTANGLECOL,
        )
        self.rightS = mn.Angle(
            mn.Line(self.S, self.M),
            mn.Line(self.S, self.X),
            radius=0.3,
            other_angle=False,
            dot=True,
            dot_color=RIGHTANGLECOL,
            color=RIGHTANGLECOL,
        )
        self.rightM = mn.Angle(
            mn.Line(self.M, self.N),
            mn.Line(self.M, self.S),
            radius=0.3,
            other_angle=False,
            dot=True,
            dot_color=RIGHTANGLECOL,
            color=RIGHTANGLECOL,
        )
        self.rightG = mn.Angle(
            mn.Line(self.G.get_center(), self.S.get_center()),
            mn.Line(self.G.get_center(), self.X.get_center()),
            radius=0.3,
            other_angle=True,
            dot=True,
            dot_color=RIGHTANGLECOL,
            color=RIGHTANGLECOL,
        )
        self.angleX = mn.Angle(
            mn.Line(self.X, self.S),
            mn.Line(self.X, self.M),
            radius=0.5,
            color=ANGLECOL,
            stroke_width=3,
        )
        self.angleXlabel = mn.MathTex(r"\alpha", color=ANGLECOL, font_size=24).move_to(
            mn.Angle(
                mn.Line(self.X, self.S),
                mn.Line(self.X, self.M),
                radius=0.5 + 3 * mn.SMALL_BUFF,
            ).point_from_proportion(0.5)
        )

        # Dreiecke und Groups
        self.QMAMDreieck = mn.VGroup(
            self.qm, self.am2, self.lineMS, self.S, self.M, self.N, self.rightM
        )
        self.AMGMDreieck = mn.VGroup(
            self.gm, self.am1, self.lineMS, self.S, self.M, self.X, self.rightS
        )  # auch Dreieck für Ähnlichkeit
        self.GMHMDreieck = mn.VGroup(
            self.hm, self.gm, self.lineSG, self.S, self.G, self.X, self.rightG
        )
        self.angXl = mn.VGroup(self.angleX, self.angleXlabel)
        self.GanzeSkizze = mn.VGroup(
            # Punkte
            *[self.M, self.A, self.B, self.S, self.N, self.X, self.G],
            # Linien
            *[
                self.sega,
                self.segb,
                self.semikreis,
                self.gm,
                self.am1,
                self.am2,
                self.am3,
                self.qm,
                self.hm,
                self.lineMS,
                self.lineSG,
            ],
            # Labels
            *[self.labelM, self.labelS, self.labelN, self.labelX, self.labelG],
            # Braces + Brace Labels
            *[
                self.abr,
                self.bbr,
                self.abrtxt,
                self.bbrtxt,
            ],
            # Winkel + Winkel Labels
            [
                self.rightX,
                self.rightS,
                self.rightM,
                self.rightG,
                self.angleX,
                self.angleXlabel,
            ],
        )

        # Base construction
        self.construction = mn.VGroup(
            self.semikreis,
            self.sega,
            self.segb,
            self.S,
            self.M,
            self.labelS,
            self.labelM,
            self.abr,
            self.bbr,
            self.abrtxt,
            self.bbrtxt,
        )


class Audio:
    """
    Audio file and properties
    """

    path = "media/Audio/audio.wav"
    if os.path.exists(path):
        song = pydub.AudioSegment.from_file(path)
    else:
        warnings.warn(f"\033[1;33m{path} not found. Rendering without Audio.\033[0m")

    taktnull = 10.95  # ein Takt vor Anfang
    takt = 2.4  # 100 bpm

    einleitung = 0.75 * takt + taktnull  # Stell dir vor
    refrain1 = 14 * takt + taktnull  # Auf "QM"
    strophe1 = 22 * takt + taktnull  # Ende letzte Note vom 1. Refrain
    refrain2 = 38 * takt + taktnull  # Schlag auf "un-gemein"
    strophe2 = 46 * takt + taktnull  # Ende letzte Note vom 2. Refrain
    refrain3 = 63 * takt + taktnull  # Schlag auf "da-nn"
    strophe3 = 71 * takt + taktnull  # Ende letzte Note vom 3 Refrain
    refrain4 = 88 * takt + taktnull  # Schlag auf "da-nn"
    strophe4 = 96 * takt + taktnull  # Ende letzte Note vom 4. Refrain
    refrain5 = 112 * takt + taktnull  # Schlag auf "da-nn"
    strophe5 = 120 * takt + taktnull  # Ende letzte Note vom 5. Refrain
    refrain6 = 137 * takt + taktnull  # Schlag auf "al-lem"
    refrain7 = 145 * takt + taktnull  # Auf und-3-und-4 letzter Takt vom 6. Refrain
