from manim import *

class NoNaked(Scene):
    def construct(self):

        # MAIN TITLE
        title = Text(
            "So… naked calls?",
            font_size=40,
            color=YELLOW,
            weight=BOLD
        ).to_edge(UP, buff=1)

        # SUBTITLE — subtle humor / warning
        subtitle = Text(
            "Unlimited loss is unrealistic.\n"
            "We hate infinities and always want something concrete.",
            font_size=28,
            color=WHITE,
            line_spacing=1.1
        ).next_to(title, DOWN, buff=1)

        # BIG PUNCHLINE AT BOTTOM — transition to covered calls
        punchline = Text(
            "The solution? Covered calls!",
            font_size=38,
            color=GREEN,
            weight=BOLD
        ).to_edge(DOWN, buff=0.7)

        # ANIMATION
        self.play(FadeIn(title, shift=UP))
        self.wait(0.4)
        self.play(FadeIn(subtitle, shift=DOWN))
        self.wait(0.5)
        self.play(FadeIn(punchline, shift=UP))
        self.wait(2)
