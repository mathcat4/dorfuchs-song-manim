import manim as mn
import numpy as np

mn.config.background_color = mn.WHITE
TXTCOL = mn.BLACK
AMCOL = mn.ORANGE
GMCOL = mn.GREEN_D
QMCOL = mn.BLUE_D
HMCOL = mn.PURPLE_D
RIGHTANGLECOL = mn.GREY


class RF:
    """Objects reused for the refrain"""

    # Equation and Relation objects

    eq_QM = mn.MathTex(r"\sqrt{\frac{a^2+b^2}{2}}", color=TXTCOL)
    rel_QM_AM = mn.MathTex(r"\geq", color=TXTCOL)

    eq_AM = mn.MathTex(r"\frac{a+b}{2}", color=TXTCOL)
    rel_AM_GM = mn.MathTex(r"\geq", color=TXTCOL)

    eq_GM = mn.MathTex(r"\sqrt{ab}", color=TXTCOL)
    rel_GM_HM = mn.MathTex(r"\geq", color=TXTCOL)

    eq_HM = mn.MathTex(r"\frac{2}{\frac{1}{a} + \frac{1}{b}}", color=TXTCOL)

    group_eq = mn.VGroup(
        eq_QM, rel_QM_AM, eq_AM, rel_AM_GM, eq_GM, rel_GM_HM, eq_HM
    ).arrange(mn.RIGHT, buff=0.5)

    # Text Objects

    text_QM = mn.Text("QM", color=QMCOL).scale(0.75)
    text_QM.move_to(eq_QM).align_to(group_eq.get_top() + mn.UP, mn.UP)
    group_QM = mn.VGroup(eq_QM, text_QM)

    text_AM = mn.Text("AM", color=AMCOL).scale(0.75)
    text_AM.move_to(eq_AM).align_to(group_eq.get_top() + mn.UP, mn.UP)
    group_AM = mn.VGroup(eq_AM, text_AM)

    text_GM = mn.Text("GM", color=GMCOL).scale(0.75)
    text_GM.move_to(eq_GM).align_to(group_eq.get_top() + mn.UP, mn.UP)
    group_GM = mn.VGroup(eq_GM, text_GM)

    text_HM = mn.Text("HM", color=HMCOL).scale(0.75)
    text_HM.move_to(eq_HM).align_to(group_eq.get_top() + mn.UP, mn.UP)
    group_HM = mn.VGroup(eq_HM, text_HM)

    group_text = mn.VGroup(text_QM, text_AM, text_GM, text_HM)

    group_QM_AM = mn.VGroup(*group_QM, rel_QM_AM, *group_AM)
    group_AM_GM = mn.VGroup(*group_AM, rel_AM_GM, *group_GM)
    group_GM_HM = mn.VGroup(*group_GM, rel_GM_HM, *group_HM)

    # Final text

    final_text = mn.Text("Das sind die Mittelungleichungen!", color=TXTCOL).scale(0.75)
    final_text.next_to(group_eq, mn.DOWN, buff=1)


class RF6:
    """Multi-variable mean layout reused for refrain 6"""

    # Multi-variable means

    eq_QM = mn.MathTex(
        r"\sqrt{ {{ {{ {a_1}^2 + {a_2}^2 + \dots + {a_n}^2 }} \over {{ n }} }} }",
        color=mn.BLUE_D,
    )
    eq_AM = mn.MathTex(r"{{ a_1 + a_2 + \dots + a_n }} \over {{ n }}", color=mn.ORANGE)
    eq_GM = mn.MathTex(
        r"\sqrt[n]{ \hspace{0.1pt} {{ a_1 a_2 \ldots a_n }} }", color=mn.GREEN_D
    )
    eq_HM = mn.MathTex(
        r"{{ n }} \over {{ \frac{1}{a_1} + \frac{1}{a_2} + \dots + \frac{1}{a_n} }}",
        color=mn.PURPLE_D,
    )

    group_eq = mn.VGroup(eq_QM, eq_AM, eq_HM, eq_GM).arrange_in_grid(
        rows=2, cols=2, buff=4
    )
