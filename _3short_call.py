from _Xpayoff_scene import OptionPayoffScene
from manim import *

class ShortCall(OptionPayoffScene):
    def construct(self):
        super().construct(
            title_text="Simple Call",
            title_color=RED,
            payoff_func=lambda x: min(2 - max(x - 5, 0), 2),
            payoff_color=RED,
            pros_or_cons_title="Pros",
            pros_or_cons_color=GREEN,
            pros_or_cons_items=[
                "Not a speculative position",
                "Benefits from ongoing time decay",
                "High probability of expiring out-of-the-money"
            ]
        )