from manim import *
from _Xtransition_scene import TextScene

class WhyCalls(TextScene):
    def __init__(self, **kwargs):
        super().__init__(
            title_text="Then why is there Calls?",
            subtitle_text="Because humans love the idea of unlimited upside\n"
                          "and conveniently ignore the part where math exists.",
            punchline_text="So what can we do with calls? We sell them!",
            title_color=YELLOW,
            subtitle_color=WHITE,
            punchline_color=RED,
            **kwargs
        )