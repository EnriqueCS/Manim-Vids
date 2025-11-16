from manim import *

class WhyCalls(Scene):
    def construct(self):

        # MAIN TITLE
        title = Text(
            "Then why is there Calls?",
            font_size=40,
            color=YELLOW,
            weight=BOLD
        ).to_edge(UP, buff=1)

        # SUBTITLE (subtle degen)
        subtitle = Text(
            "Because humans love the idea of unlimited upside\n"
            "and conveniently ignore the part where math exists.",
            font_size=28,
            color=WHITE,
            line_spacing=1.1
        ).next_to(title, DOWN, buff=1)

        # BIG PUNCHLINE AT BOTTOM
        punchline = Text(
            "So what can we do with calls? We sell them!",
            font_size=38,
            color=RED,
            weight=BOLD
        ).to_edge(DOWN, buff=0.7)

        # ANIMATION
        self.play(FadeIn(title, shift=UP))
        self.wait(0.4)
        self.play(FadeIn(subtitle, shift=DOWN))
        self.wait(0.5)
        self.play(FadeIn(punchline, shift=UP))
        self.wait(2)
