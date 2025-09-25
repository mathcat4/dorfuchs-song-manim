import manim as mn
import numpy as np
import math
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


# Punkte
M = mn.Dot(np.array([0, -1.5, 0]), color=TXTCOL)  # kinda variable
A = mn.Dot([-r, 0, 0] + M.get_center(), color=TXTCOL)
B = mn.Dot([r, 0, 0] + M.get_center(), color=TXTCOL)
S = mn.Dot([-1.3, 0, 0] + M.get_center(), color=TXTCOL)
N = mn.Dot([0, r, 0] + M.get_center(), color=TXTCOL)
cord = M.get_y() + math.sqrt(r**2 - (S.get_x()) ** 2)
X = mn.Dot(np.array([S.get_x(), cord, 0]), color=TXTCOL)

# Linienundso
sega = mn.Line(start=A.get_center(), end=S.get_center(), color=TXTCOL)
segb = mn.Line(start=S.get_center(), end=B.get_center(), color=TXTCOL)
semikreis = mn.Arc(
    radius=r, start_angle=0, angle=mn.PI, arc_center=M.get_center(), color=TXTCOL
)
gm = mn.Line(S, X, color=GMCOL)
am1 = mn.Line(M, X, color=AMCOL)
am2 = mn.Line(M, N, color=AMCOL)
am3 = mn.Line(M, A, color=AMCOL)
qm = mn.Line(S, N, color=QMCOL)
G = mn.Dot(am1.get_projection(S.get_center()), color=TXTCOL)  # defintiv auch eine linie
hm = mn.Line(X, G.get_center(), color=HMCOL)
lineAX = mn.Line(A.get_center(), X.get_center(), color=TXTCOL)
lineBX = mn.Line(B.get_center(), X.get_center(), color=TXTCOL)
lineMS = mn.Line(M, S, color=TXTCOL)
dashed1 = mn.DashedLine(S.get_center(), G.get_center(), color=TXTCOL, stroke_width=3)
dashedam = mn.DashedLine(M.get_center(), X.get_center(), color=AMCOL, stroke_width=2)

# Labels
labelM = mn.MathTex("M", font_size=24, color=TXTCOL)
labelM.next_to(M, mn.UR, buff=0.05)
labelS = mn.MathTex("S", font_size=24, color=TXTCOL)
labelS.next_to(S, mn.UL, buff=0.05)
labelN = mn.MathTex("N", font_size=24, color=TXTCOL)
labelN.next_to(N, mn.UL, buff=0.05)
labelX = mn.MathTex("X", font_size=24, color=TXTCOL)
labelX.next_to(X, mn.UL, buff=0.05)
labelG = mn.MathTex("G", font_size=24, color=TXTCOL)
labelG.next_to(G, mn.UR, buff=0.05)

# nur zum animieren (dont judge me als ich das geschrieben hat kannt ich manim seit 30minuten)
firsta = mn.Line(
    A.get_center() + [-0.25, 0.5, 0],
    S.get_center() + [-0.25, 0.5, 0],
    color=TXTCOL,
)
firstb = mn.Line(
    S.get_center() + [0.25, 0.5, 0],
    B.get_center() + [0.25, 0.5, 0],
    color=TXTCOL,
)

# Braces
b1 = mn.Brace(
    firsta,
    direction=firsta.copy().rotate(mn.PI / 2).get_unit_vector(),
    color=TXTCOL,
)
b2 = mn.Brace(
    firstb,
    direction=firstb.copy().rotate(mn.PI / 2).get_unit_vector(),
    color=TXTCOL,
)
b1text = b1.get_tex("a")
b1text.set_color(TXTCOL)
b2text = b2.get_tex("b")
b2text.set_color(TXTCOL)
labelAB = mn.VGroup(b1text, b2text)
abr = mn.Brace(
    sega,
    direction=firsta.copy().rotate(3 * mn.PI / 2).get_unit_vector(),
    color=TXTCOL,
)
bbr = mn.Brace(
    segb,
    direction=firstb.copy().rotate(3 * mn.PI / 2).get_unit_vector(),
    color=TXTCOL,
)
abrtxt = abr.get_tex("a")
abrtxt.set_color(TXTCOL)
bbrtxt = bbr.get_tex("b")
bbrtxt.set_color(TXTCOL)

# Winkel
rightAXB = mn.Angle(
    mn.Line(X, A),
    mn.Line(X, B),
    radius=0.5,
    other_angle=False,
    dot=True,
    dot_color=RIGHTANGLECOL,
    color=RIGHTANGLECOL,
)
rightS = mn.Angle(
    mn.Line(S, M),
    mn.Line(S, X),
    radius=0.3,
    other_angle=False,
    dot=True,
    dot_color=RIGHTANGLECOL,
    color=RIGHTANGLECOL,
)
rightM = mn.Angle(
    mn.Line(M, N),
    mn.Line(M, S),
    radius=0.3,
    other_angle=False,
    dot=True,
    dot_color=RIGHTANGLECOL,
    color=RIGHTANGLECOL,
)
rightG = mn.Angle(
    mn.Line(G.get_center(), S.get_center()),
    mn.Line(G.get_center(), X.get_center()),
    radius=0.3,
    other_angle=True,
    dot=True,
    dot_color=RIGHTANGLECOL,
    color=RIGHTANGLECOL,
)
angleX = mn.Angle(
    mn.Line(X, S), mn.Line(X, M), radius=0.5, color=mn.PINK, stroke_width=3
)
angleXlabel = mn.MathTex(r"\alpha", color=mn.PINK, font_size=24).move_to(
    mn.Angle(
        mn.Line(X, S), mn.Line(X, M), radius=0.5 + 3 * mn.SMALL_BUFF
    ).point_from_proportion(0.5)
)

# Dreiecke und Grops
QMAMDreieck = mn.Group(qm, am2, lineMS, S, M, N, rightM)
AMGMDreieck = mn.Group(gm, am1, lineMS, S, M, X, rightS)  # auch Dreieck für Ähnlichkeit
GMHMDreieck = mn.Group(hm, gm, dashed1, S, G, X, rightG)
angXl = mn.Group(angleX, angleXlabel)
GanzeSkizze = mn.VGroup(
    #    Punkte
    M,
    A,
    B,
    S,
    N,
    X,
    G,
    # Linien
    sega,
    segb,
    semikreis,
    gm,
    am1,
    am2,
    am3,
    qm,
    hm,
    lineAX,
    lineBX,
    lineMS,
    dashed1,
    dashedam,
    # Labels
    labelM,
    labelS,
    labelN,
    labelX,
    labelG,
    # nur zum animieren
    firsta,
    firstb,
    # Braces + brace texts
    b1,
    b2,
    b1text,
    b2text,
    labelAB,
    abr,
    bbr,
    abrtxt,
    bbrtxt,
    # Winkel + Winkel-Labels
    rightAXB,
    rightS,
    rightM,
    rightG,
    angleX,
    angleXlabel,
)

# positions
right_half_center = mn.ORIGIN + mn.RIGHT * mn.config.frame_x_radius / 2
left_half_center = mn.ORIGIN + mn.LEFT * mn.config.frame_x_radius / 2
