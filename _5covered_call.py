from _Xpayoff_scene import OptionPayoffScene
from manim import *

class CoveredCall(OptionPayoffScene):
    def construct(self):
        super().construct(
            title_text="Covered Call",
            title_color=GREEN,
            payoff_func=lambda x: min((x - 5) + 2, 2),  # 100 shares with $2 premium
            payoff_color=GREEN,
            pros_or_cons_title="Pros",
            pros_or_cons_color=GREEN,
            pros_or_cons_items=[
                "Risk limited by owning 100 shares",
                "Benefits from ongoing time decay",
                "Higher probability of stable income"
            ]
        )
