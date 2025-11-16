from manim import *

class TextScene(Scene):
    def __init__(
        self,
        title_text: str,
        subtitle_text: str,
        punchline_text: str,
        title_color=YELLOW,
        subtitle_color=WHITE,
        punchline_color=RED,
        title_size=40,
        subtitle_size=28,
        punchline_size=38,
        subtitle_line_spacing=1.1,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.title_text = title_text
        self.subtitle_text = subtitle_text
        self.punchline_text = punchline_text
        self.title_color = title_color
        self.subtitle_color = subtitle_color
        self.punchline_color = punchline_color
        self.title_size = title_size
        self.subtitle_size = subtitle_size
        self.punchline_size = punchline_size
        self.subtitle_line_spacing = subtitle_line_spacing

    def construct(self):
        # MAIN TITLE
        title = Text(
            self.title_text,
            font_size=self.title_size,
            color=self.title_color,
            weight=BOLD
        ).to_edge(UP, buff=1)

        # SUBTITLE
        subtitle = Text(
            self.subtitle_text,
            font_size=self.subtitle_size,
            color=self.subtitle_color,
            line_spacing=self.subtitle_line_spacing
        ).next_to(title, DOWN, buff=1)

        # PUNCHLINE
        punchline = Text(
            self.punchline_text,
            font_size=self.punchline_size,
            color=self.punchline_color,
            weight=BOLD
        ).to_edge(DOWN, buff=0.7)

        # ANIMATION
        self.play(FadeIn(title, shift=UP))
        self.wait(0.4)
        self.play(FadeIn(subtitle, shift=DOWN))
        self.wait(0.5)
        self.play(FadeIn(punchline, shift=UP))
        self.wait(2)


# Example usage: recreating your two original scenes

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
