from helpers import *


class MainSketch(mn.Scene):
    def construct(self):
        # Equation and text objects

        self.add(RF.group_eq, RF.group_text)

        # Fade and scale animations

        fade_in = []

        for group_anim in [RF.group_QM_AM, RF.group_AM_GM, RF.group_GM_HM]:
            fade_out = [
                mobj
                for mobj in [*RF.group_eq, *RF.group_text]
                if mobj not in group_anim
            ]

            fade_out_anims = [
                mobj.animate.set_opacity(0.3)
                for mobj in fade_out
                if mobj not in fade_in
            ]
            fade_in_anims = [
                mobj.animate.set_opacity(1) for mobj in fade_in if mobj not in fade_out
            ]

            self.play(*(fade_out_anims + fade_in_anims))

            self.play(
                group_anim.animate.scale(1.5), rate_func=mn.rate_functions.rush_from
            )
            self.wait(0.5)
            self.play(
                group_anim.animate.scale(1 / 1.5), rate_func=mn.rate_functions.rush_into
            )

            fade_in = fade_out.copy()

            # self.wait(1)

        self.play(*[mobj.animate.set_opacity(1) for mobj in fade_in])

        # Final text

        self.play(mn.Write(RF.final_text), run_time=2)

        self.wait(3)
