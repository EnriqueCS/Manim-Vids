# simple_call.py
from _Xpayoff_scene import OptionPayoffScene
from manim import *

class SimpleCall(OptionPayoffScene):
    def construct(self):
        super().construct(
            title_text="Simple Call",
            title_color=GREEN,
            payoff_func=lambda x: max(x - 5, -2),
            payoff_color=GREEN,
            pros_or_cons_title="Cons",
            pros_or_cons_color=RED,
            pros_or_cons_items=[
                "Largely a speculative position",
                "Susceptible to ongoing time decay",
                "Low probability of expiring in-the-money"
            ]
        )

