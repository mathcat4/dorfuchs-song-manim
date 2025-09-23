import manim as mn
import refrain1 as rf1

class MainSketch(mn.Scene):
    def construct(self):
        pass
        
        #!TODO: Think of a better scene
        # # Power mean equation and Relation objects
            
        # eq_PM_QM = mn.MathTex(r"\sqrt[2]{ \frac{{a_1}^2 + {a_2}^2 + \dots + {a_n}^2}{n} }", color = mn.BLUE_D) 
        # eq_PM_AM = mn.MathTex(r"\sqrt[1]{ \frac{{a_1}^1 + {a_2}^1 + \dots + {a_n}^1}{n} }", color = mn.ORANGE) 
        # eq_PM_GM = mn.MathTex(r"\lim_{p \to 0} {{ \sqrt[p]{ \frac{{a_1}^p + {a_2}^p + \dots + {a_n}^p}{n} } }}", color = mn.GREEN_D) 
        # eq_PM_HM = mn.MathTex(r"\sqrt[-1]{ \frac{{a_1}^{-1} + {a_2}^{-1} + \dots + {a_n}^{-1} }{n} }", color = mn.PURPLE_D) 

        # group_PM_eq = mn.VGroup(eq_PM_QM, rf1.mObjs.rel_QM_AM, eq_PM_AM, rf1.mObjs.rel_AM_GM, eq_PM_GM, rf1.mObjs.rel_GM_HM, eq_PM_HM).arrange(mn.RIGHT, buff=0.5)

        # self.add(group_PM_eq, rf1.mObjs.group_text)

        # # Fade and scale animations

        # fade_in_anims = []

        # for group_anim in [rf1.mObjs.group_QM_AM, rf1.mObjs.group_AM_GM, rf1.mObjs.group_GM_HM]:
        #     fade_out_anims = []
        #     for mobj in [*rf1.mObjs.group_eq, *rf1.mObjs.group_text]:
        #         if mobj not in group_anim:
        #             fade_out_anims.append(mobj.animate.set_opacity(0.3))
            
        #     self.play(*(fade_out_anims + fade_in_anims))

        #     self.play(group_anim.animate.scale(1.5))
        #     self.wait(0.5)
        #     self.play(group_anim.animate.scale(1/1.5))

        #     fade_in_anims = [mobj.animate.set_opacity(1) for mobj in [*rf1.mObjs.group_eq, *rf1.mObjs.group_text]]

        #     self.wait(1)
        
        # self.play(*fade_in_anims)

        # self.play(mn.Write(rf1.mObjs.final_text), run_time=2)

        # self.wait(3)