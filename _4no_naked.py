from manim import *
from _Xtransition_scene import TextScene

class NoNaked(TextScene):
    def __init__(self, **kwargs):
        super().__init__(
            title_text="So… naked calls?",
            subtitle_text="Unlimited loss is unrealistic.\n"
                          "We hate infinities and always want something concrete.",
            punchline_text="The solution? Covered calls!",
            title_color=YELLOW,
            subtitle_color=WHITE,
            punchline_color=GREEN,
            **kwargs
        )