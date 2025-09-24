from manim import *
import math

def zauberfunktion(scene: Scene, group: VGroup, anim_fn):
    #please only use homogenous animations
    visible_parts = [m for m in group if m in scene.mobjects]
    hidden_parts = [m for m in group if m not in scene.mobjects]

    # Apply transformation instant to hidden parts
    for m in hidden_parts:
        anim_fn(m)  

    # Animate visible parts
    scene.play(*[anim_fn(m.animate) for m in visible_parts])





def TransformMatchingTexNoReplace(src, target, **kwargs):
    """
    Leave `src` in place. Animate a copy of it:
    1. Move the copy to `target`'s location,
    2. Morph it into `target`.
    """
    src_copy = src.copy()
    src_copy.generate_target()
    src_copy.target.move_to(target.get_center())

    # Phase 1: move copy to target location
    move = MoveToTarget(src_copy)

    # Phase 2: morph into target
    morph = TransformMatchingTex(
        src_copy,
        target,
        replace_mobject_with_target_in_scene=True,
        **kwargs
    )

    return AnimationGroup(move, morph, lag_ratio=1.0)






class Constram(Scene):
    def construct(self):
        # Variablen
        self.camera.background_color = WHITE
        TXTCOL = BLACK
        AMCOL = ORANGE
        GMCOL = GREEN_D
        QMCOL = BLUE_D
        HMCOL = PURPLE_D
        ACOL = RED
        BCOL = DARK_BLUE
        RIGHTANGLECOL = GREY
        r = 3
        
        # Punkte
        M = Dot([0, -1.5, 0], color=TXTCOL) #kinda variable
        A = Dot([-r, 0, 0] + M.get_center(), color=TXTCOL)
        B = Dot([r, 0, 0] + M.get_center(), color=TXTCOL)
        S = Dot([-1.3, 0, 0] + M.get_center(), color=TXTCOL)
        N = Dot([0,r,0] + M.get_center(), color=TXTCOL)
        cord = M.get_y() + math.sqrt(r**2-(S.get_x())**2)
        X = Dot([S.get_x(), cord, 0], color=TXTCOL)

        # Linienundso
        sega = Line(start=A.get_center(), end=S.get_center(), color=TXTCOL)
        segb = Line(start=S.get_center(), end=B.get_center(), color=TXTCOL)
        semikreis = Arc(radius=r, start_angle=0, angle=PI, arc_center=M.get_center(), color=TXTCOL)
        gm = Line(S,X, color=GMCOL)
        am1 = Line(M,X, color=AMCOL)
        am2 = Line(M,N, color=AMCOL)
        am3 = Line(M,A, color=AMCOL)
        qm = Line(S,N, color=QMCOL)
        G = Dot(am1.get_projection(S.get_center()), color=TXTCOL) #defintiv auch eine linie
        hm = Line(X,G, color=HMCOL)
        lineAX = Line(A.get_center(),X.get_center(), color=TXTCOL)
        lineBX = Line(B.get_center(),X.get_center(), color= TXTCOL)
        lineMS = Line(M,S, color=TXTCOL)
        dashed1 = DashedLine(S.get_center(),G.get_center(), color=TXTCOL, stroke_width=3)
        dashedam = DashedLine(M.get_center(),X.get_center(), color=AMCOL, stroke_width=2)

        # Labels
        labelM = MathTex("M", font_size=24, color=TXTCOL)
        labelM.next_to(M, UR, buff=0.05)
        labelS = MathTex("S", font_size=24, color=TXTCOL)
        labelS.next_to(S, UL, buff=0.05)
        labelN = MathTex("N", font_size=24, color=TXTCOL)
        labelN.next_to(N, UL, buff=0.05)
        labelX = MathTex("X", font_size=24, color=TXTCOL)
        labelX.next_to(X, UL, buff=0.05)
        labelG = MathTex("G", font_size=24, color=TXTCOL)
        labelG.next_to(G, UR, buff=0.05)

        # nur zum animieren (dont judge me als ich das geschrieben hat kannt ich manim seit 30minuten)
        firsta = Line(A.get_center() + [-0.25, 0.5, 0],
                      S.get_center() + [-0.25, 0.5, 0], color=TXTCOL)
        firstb = Line(S.get_center() + [0.25, 0.5, 0],
                      B.get_center() + [0.25, 0.5, 0], color=TXTCOL)

        

        # Braces
        b1 = Brace(firsta, direction=firsta.copy().rotate(PI / 2).get_unit_vector(), color=TXTCOL)
        b2 = Brace(firstb, direction=firstb.copy().rotate(PI / 2).get_unit_vector(), color=TXTCOL)
        b1text = b1.get_tex("a")
        b1text.set_color(TXTCOL)
        b2text = b2.get_tex("b")
        b2text.set_color(TXTCOL)
        labelAB = VGroup(b1text, b2text)
        abr = Brace(sega, direction=firsta.copy().rotate(3*PI / 2).get_unit_vector(), color=TXTCOL)
        bbr = Brace(segb, direction=firstb.copy().rotate(3*PI / 2).get_unit_vector(), color=TXTCOL)
        abrtxt = abr.get_tex("a")
        abrtxt.set_color(TXTCOL)
        bbrtxt = bbr.get_tex("b")
        bbrtxt.set_color(TXTCOL)

        

        #Winkel
        rightAXB = Angle(Line(X,A), Line(X,B), radius=0.5, other_angle=False, dot=True, dot_color=RIGHTANGLECOL, color=RIGHTANGLECOL)
        rightS = Angle(Line(S,M), Line(S,X), radius=0.3, other_angle=False, dot=True, dot_color=RIGHTANGLECOL, color=RIGHTANGLECOL)
        rightM = Angle(Line(M,N), Line(M,S), radius=0.3, other_angle=False, dot=True, dot_color=RIGHTANGLECOL, color=RIGHTANGLECOL)
        rightG = Angle(Line(G.get_center(),S.get_center()), Line(G.get_center(),X.get_center()), radius=0.3, other_angle=True, dot=True, dot_color=RIGHTANGLECOL, color=RIGHTANGLECOL)
        angleX = Angle(Line(X,S),Line(X,M), radius=0.5, color = PINK, stroke_width=3)
        angleXlabel = MathTex(r"\alpha", color=PINK, font_size=24).move_to(
            Angle(
                Line(X,S),Line(X,M), radius=0.5 + 3 * SMALL_BUFF
            ).point_from_proportion(0.5)
        )

        
        

        #Dreiecke und Grops
        QMAMDreieck = Group(qm, am2, lineMS, S, M, N, rightM)
        AMGMDreieck = Group(gm, am1, lineMS, S, M, X, rightS) #auch Dreieck für Ähnlichkeit
        GMHMDreieck = Group(hm, gm, dashed1, S, G, X, rightG)
        angXl = Group(angleX, angleXlabel)
        GanzeSkizze = VGroup(
        #    Punkte
        M, A, B, S, N, X, G,

        # Linien
        sega, segb, semikreis, gm, am1, am2, am3, qm,
        hm, lineAX, lineBX, lineMS, dashed1, dashedam,

        # Labels
        labelM, labelS, labelN, labelX, labelG,

        # nur zum animieren
        firsta, firstb,

        # Braces + brace texts
        b1, b2, b1text, b2text, labelAB,
        abr, bbr, abrtxt, bbrtxt,

        # Winkel + Winkel-Labels
        rightAXB, rightS, rightM, rightG,
        angleX, angleXlabel
        )

        #positions
        right_half_center = (ORIGIN + RIGHT * config["frame_x_radius"] / 2)
        left_half_center = (ORIGIN + LEFT * config["frame_x_radius"] / 2)

        

        # Konstruktion Kreis + AM
        self.play(FadeIn(firsta), FadeIn(firstb), FadeIn(b1), FadeIn(labelAB), FadeIn(b2))
        term1 = MathTex(r"a + b", color=TXTCOL).shift(UP*3)
        self.play(Transform(firsta, sega), FadeOut(b1), FadeOut(b2), TransformMatchingShapes(labelAB, term1), Transform(firstb, segb))
        term2 = MathTex(r"\frac{a + b}{2}", color=TXTCOL).shift(UP*3)
        self.play(Create(S), FadeIn(abr), FadeIn(bbr), FadeIn(abrtxt), FadeIn(bbrtxt))
        self.play(Create(M), Create(labelM), TransformMatchingShapes(term1, term2))
        self.play(Create(semikreis))
        term3 = MathTex(r"r =", r"\frac{a + b}{2}", r"= AM(a,b)", color=AMCOL).shift(UP*3)
        term2.generate_target()
        term2.target.move_to(term3[1].get_center())  # move into place
        term2.target.set_color(AMCOL) 
        self.play(
            MoveToTarget(term2),  # morph fraction to new fraction
            FadeIn(term3[0]),  # r =
            FadeIn(term3[2])   # = AM(a,b)
        )
        #bitte bite funktuniertre
        moving_dot = Dot(semikreis.point_from_proportion(0), color=RED)
        moving_dot.set_opacity(0)
        line = always_redraw(lambda: Line(M.get_center(), moving_dot.get_center(), color=AMCOL))
        self.add(moving_dot)
        self.add(line)
        self.play(
            MoveAlongPath(moving_dot,semikreis,rate_func=lambda t: 1 - (1-t)**2, run_time=3)
        )
        self.remove(line)
        self.play(Create(labelS))
        self.wait(1)
        self.play(FadeOut(term3),FadeOut(term2))

        #qm visualisieren
        #vorbereitung
        self.add(lineMS)
        tex1 = MathTex(r"QM(a,b) = \sqrt{\frac{a^2+b^2}{2}}", color = QMCOL).shift(UP*3)
        self.play(Write(tex1))
        self.play(FadeIn(am2), FadeIn(N))
        self.play(Create(qm))
        self.play(Create(labelN))
        self.play(Create(rightM))
        self.play(Wiggle(QMAMDreieck))
        self.add(am2) # sieht zwar fett dumm aus aber is nötig, weil das anwenden von Gruppen Daten komisch umformatiert (und man das iwie wieder auflösen muss) und deswegen meine hex hex funktion nd funktioniert.
        self.play(FadeOut(tex1))
        zauberfunktion(self, GanzeSkizze, lambda m: m.shift(LEFT*3))
        term10 = MathTex(r"{{\frac{a+b}{2}}}", color = TXTCOL).move_to(right_half_center).shift(LEFT*1.5)
        term11 = MathTex(r"\frac{a+b}{2} - a", color = TXTCOL).move_to(right_half_center).shift(RIGHT*1.5)
        term12 = MathTex(r"{{\frac{b-a}{2}}}", color = TXTCOL).move_to(right_half_center).shift(RIGHT*1.5)
        term13 = MathTex(r"{{|\overline{SM}|}}{{^2}} {{=}} ({{\frac{a+b}{2}}})^2 + ({{\frac{b-a}{2}}})^2 ", color = TXTCOL).move_to(right_half_center).shift(UP*1.5)
        term14 = MathTex(r"{{|\overline{SM}|}}{{^2}} {{=}} \frac{(a+b)^2 + (b-a)^2}{2^2}", color = TXTCOL).move_to(right_half_center).shift(UP*15)
        term15 = MathTex(r"{{|\overline{SM}|}}{{^2}} {{=}} \frac{a^2 + 2ab + b^2 + a^2 - 2ab + b^2}{2^2}", color = TXTCOL, font_size=28).move_to(right_half_center)
        term16 = MathTex(r"{{|\overline{SM}|}}{{^2}} {{=}} \frac{2a^2 + 2b^2}{2^2}", color = TXTCOL).move_to(right_half_center)
        term17 = MathTex(r"{{|\overline{SM}|}}{{^2}} {{=}} \frac{a^2 + b^2}{2^2}", color = TXTCOL).move_to(right_half_center)
        term18 = MathTex(r"{{|\overline{SM}|}} {{=}} \sqrt{\frac{a^2 + b^2}{2^2}}", color = TXTCOL).move_to(right_half_center).shift(DOWN*1.5)
        term19 = MathTex(r"{{|\overline{SM}|}} {{=}} \sqrt{\frac{a^2 + b^2}{2^2}} = QM(a,b)", color = QMCOL).move_to(right_half_center)
        self.play(Wiggle(am2), Write(term10))
        self.remove(lineMS)
        lineMS.color = RED
        self.play(FadeIn(am3), run_time=0.5)
        self.play(ReplacementTransform(am3,lineMS), Write(term11)) 
        self.play(Wiggle(lineMS))
        self.play(lineMS.animate.set_color(TXTCOL))
        self.play(TransformMatchingShapes(term11, term12))
        self.play(TransformMatchingTex(Group(term12,term10), term13))
        self.wait(1)
        self.play(TransformMatchingTex(term13, term14))
        self.play(TransformMatchingTexNoReplace(term14, term15))
        self.play(TransformMatchingTex(term15, term16))
        self.play(TransformMatchingTex(term16, term17))
        self.play(TransformMatchingTexNoReplace(term17, term18))
        self.play(TransformMatchingTex(term18, term19), FadeOut(term17), FadeOut(term14))
        self.wait(1)
        self.play(FadeOut(term19))
        zauberfunktion(self, GanzeSkizze, lambda m: m.shift(RIGHT*3))

        #gm visualisierung
        term4 = MathTex(r"a \cdot b", color=TXTCOL).shift(UP*3)
        term5 = MathTex(r"\sqrt{ab}", color=TXTCOL).shift(UP*3)
        term6 = MathTex(r"GM(a,b) =", r"\sqrt{ab}", color=GMCOL).shift(UP*3)
        term5.generate_target()
        term5.target.move_to(term6[1].get_center())  # move into place
        term5.target.set_color(GMCOL) 
        self.play(Write(term4))
        self.play(TransformMatchingShapes(term4, term5))
        self.play(FadeIn(term6[0]), MoveToTarget(term5))
        self.wait(1)
        self.play(FadeOut(term6), FadeOut(term5))
        self.play(Create(gm), Create(rightS))
        self.play(Create(X))
        self.play(Create(labelX))
        self.play(AnimationGroup(Create(lineAX), Create(lineBX)))
        self.play(AnimationGroup(Create(rightAXB)))
        term7 = MathTex(r"{{|\overline{SX}|}}", r"^2 {{=}}", r"{{a}} \cdot", r"{{b}}", color=TXTCOL).shift(UP*3)
        self.play(Write(term7[0]), Wiggle(gm))
        self.play(Write(term7[1]), Wiggle(gm))
        self.play(Write(term7[2]), Wiggle(sega))
        self.play(Write(term7[3]), Wiggle(segb))
        self.wait(1)
        term8 = MathTex(r"{{|\overline{SX}|}} {{=}} \sqrt{{{a}}{{b}}}", color = TXTCOL).shift(UP*3)
        term9 = MathTex(r"|\overline{SX}| = \sqrt{ab}", r"= GM(a,b)", color = GMCOL).shift(UP*3)
        self.play(TransformMatchingTex(term7,term8))
        term8.generate_target()
        term8.target.move_to(term9[0].get_center())  # move into place
        term8.target.set_color(GMCOL) 
        self.play(FadeIn(term9[1]), MoveToTarget(term8))
        self.wait(1)
        self.play(FadeOut(term8), FadeOut(term9), FadeOut(lineAX), FadeOut(lineBX), FadeOut(rightAXB))

        self.play(ReplacementTransform(am2,am1))
        self.wait(1)


        #hm visualisieren
        self.play(ReplacementTransform(am1,dashedam))
        self.play(Create(dashed1))
        self.play(Create(G), Create(labelG))
        self.play(Create(hm), Create(rightG))
        self.play(Create(angleX), Create(angleXlabel))
        self.play(Wiggle(angXl))
        self.play(Wiggle(rightG), Wiggle(rightS))
        self.play(Wiggle(AMGMDreieck))
        self.play(Wiggle(GMHMDreieck))


        self.wait(1)

        







 
