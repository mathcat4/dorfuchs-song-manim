import manim as mn
import numpy as np
import math
import pydub
import typing

# Constants

mn.config.background_color = mn.WHITE
TXTCOL = mn.BLACK
AMCOL = mn.ORANGE
GMCOL = mn.GREEN_D
QMCOL = mn.BLUE_D
HMCOL = mn.PURPLE_D
RIGHTANGLECOL = mn.GREY
r = 3
right_half_center = mn.ORIGIN + mn.RIGHT * mn.config.frame_x_radius / 2
left_half_center = mn.ORIGIN + mn.LEFT * mn.config.frame_x_radius / 2


def fade_out(scene: mn.Scene, run_time=1):
    anims = []
    for mobj in scene.mobjects:
        anims.append(mn.FadeOut(mobj, run_time=run_time))

    if anims:
        scene.play(*anims)


def zauberfunktion(scene: mn.Scene, group: mn.VGroup, anim_fn):
    # please only use homogenous animations
    visible_parts = [m for m in group if m in scene.mobjects]
    hidden_parts = [m for m in group if m not in scene.mobjects]

    # Apply transformation instant to hidden parts
    for m in hidden_parts:
        anim_fn(m)

    # Animate visible parts
    scene.play(*[anim_fn(m.animate) for m in visible_parts])


def TransformMatchingTexNoReplace(src, target, **kwargs):
    """
    Transform a *copy* of `src` into `target`, leaving `src` unchanged.
    """
    src_copy = src.copy()
    return mn.TransformMatchingTex(src_copy, target, **kwargs)


def TransformMatchingShapesNoReplace(src, target, **kwargs):
    """
    Transform a *copy* of `src` into `target`, leaving `src` unchanged.
    """
    src_copy = src.copy()
    return mn.TransformMatchingShapes(src_copy, target, **kwargs)


class Geo:
    def __init__(self):
        # Wrapping construct in a function is necessary, otherweise vars get overwritten in main.py

        # Punkte
        self.M = mn.Dot(np.array([0, -1.5, 0]), color=TXTCOL)  # kinda variable
        self.A = mn.Dot([-r, 0, 0] + self.M.get_center(), color=TXTCOL)
        self.B = mn.Dot([r, 0, 0] + self.M.get_center(), color=TXTCOL)
        self.S = mn.Dot([-1.3, 0, 0] + self.M.get_center(), color=TXTCOL)
        self.N = mn.Dot([0, r, 0] + self.M.get_center(), color=TXTCOL)
        cord = self.M.get_y() + math.sqrt(r**2 - (self.S.get_x()) ** 2)
        self.X = mn.Dot(np.array([self.S.get_x(), cord, 0]), color=TXTCOL)

        # Linienundso
        self.sega = mn.Line(
            start=self.A.get_center(), end=self.S.get_center(), color=TXTCOL
        )
        self.segb = mn.Line(
            start=self.S.get_center(), end=self.B.get_center(), color=TXTCOL
        )
        self.semikreis = mn.Arc(
            radius=r,
            start_angle=0,
            angle=mn.PI,
            arc_center=self.M.get_center(),
            color=TXTCOL,
        )

        self.gm = mn.Line(self.S, self.X, color=GMCOL)
        self.am1 = mn.Line(self.M, self.X, color=AMCOL)
        self.am2 = mn.Line(self.M, self.N, color=AMCOL)
        self.am3 = mn.Line(self.M, self.A, color=AMCOL)
        self.qm = mn.Line(self.S, self.N, color=QMCOL)
        self.G = mn.Dot(
            self.am1.get_projection(self.S.get_center()), color=TXTCOL
        )  # defintiv auch eine linie
        self.hm = mn.Line(self.X, self.G.get_center(), color=HMCOL)

        self.lineAX = mn.Line(self.A.get_center(), self.X.get_center(), color=TXTCOL)
        self.lineBX = mn.Line(self.B.get_center(), self.X.get_center(), color=TXTCOL)
        self.lineMS = mn.Line(self.M, self.S, color=TXTCOL)
        self.dashed1 = mn.DashedLine(
            self.S.get_center(), self.G.get_center(), color=TXTCOL, stroke_width=3
        )
        self.dashedam = mn.DashedLine(
            self.M.get_center(), self.X.get_center(), color=AMCOL, stroke_width=2
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

        # nur zum animieren (dont judge me als ich das geschrieben hat kannt ich manim seit 30minuten)
        self.firsta = mn.Line(
            self.A.get_center() + [-0.25, 0.5, 0],
            self.S.get_center() + [-0.25, 0.5, 0],
            color=TXTCOL,
        )
        self.firstb = mn.Line(
            self.S.get_center() + [0.25, 0.5, 0],
            self.B.get_center() + [0.25, 0.5, 0],
            color=TXTCOL,
        )

        # Braces
        self.b1 = mn.Brace(
            self.firsta,
            direction=self.firsta.copy().rotate(mn.PI / 2).get_unit_vector(),
            color=TXTCOL,
        )
        b1text = self.b1.get_tex("a")
        b1text.set_color(TXTCOL)

        self.b2 = mn.Brace(
            self.firstb,
            direction=self.firstb.copy().rotate(mn.PI / 2).get_unit_vector(),
            color=TXTCOL,
        )
        b2text = self.b2.get_tex("b")
        b2text.set_color(TXTCOL)

        self.labelAB = mn.VGroup(b1text, b2text)
        self.abr = mn.Brace(
            self.sega,
            direction=self.firsta.copy().rotate(3 * mn.PI / 2).get_unit_vector(),
            color=TXTCOL,
        )
        self.abrtxt = self.abr.get_tex("a")
        self.abrtxt.set_color(TXTCOL)

        self.bbr = mn.Brace(
            self.segb,
            direction=self.firstb.copy().rotate(3 * mn.PI / 2).get_unit_vector(),
            color=TXTCOL,
        )
        self.bbrtxt = self.bbr.get_tex("b")
        self.bbrtxt.set_color(TXTCOL)

        self.bquestion = mn.Brace(
            self.qm,
            direction=self.qm.copy().rotate(mn.PI / 2).get_unit_vector(),
            color=TXTCOL,
        )
        self.bqtext = self.bquestion.get_tex("?")
        self.bqtext.set_color(TXTCOL)

        # Winkel
        self.rightAXB = mn.Angle(
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
            color=mn.PINK,
            stroke_width=3,
        )
        self.angleXlabel = mn.MathTex(r"\alpha", color=mn.PINK, font_size=24).move_to(
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
            self.hm, self.gm, self.dashed1, self.S, self.G, self.X, self.rightG
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
                self.lineAX,
                self.lineBX,
                self.lineMS,
                self.dashed1,
                self.dashedam,
            ],
            # Labels
            *[self.labelM, self.labelS, self.labelN, self.labelX, self.labelG],
            # nur zum animieren
            *[self.firsta, self.firstb],
            # Braces + brace texts
            *[
                self.b1,
                self.b2,
                b1text,
                b2text,
                self.labelAB,
                self.abr,
                self.bbr,
                self.abrtxt,
                self.bbrtxt,
            ],
            # Winkel + Winkel-Labels
            [
                self.rightAXB,
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
    path = "media/Audio/audio.wav"
    song = pydub.AudioSegment.from_file(path)

    refrain1 = 26.9
    strophe1 = 44.69
    refrain2 = 1 * 60 + 5.39
    strophe2 = 1 * 60 + 22.97
    refrain3 = 2 * 60 + 7
    strophe3 = 2 * 60 + 24.97
    refrain4 = 3 * 60 + 6.5
    strophe4 = 3 * 60 + 24.04
    refrain5 = 4 * 60 + 4
    strophe5 = 4 * 60 + 22.33
    refrain6 = 5 * 60 + 00.58
    refrain7 = 5 * 60 + 16.6
