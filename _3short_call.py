from manim import *

class ShortCall(Scene):
    def construct(self):

        # AXES (minimal ticks, no numbers)
        axes = Axes(
            x_range=[0, 10],
            y_range=[-5, 10],
            x_length=4.5,
            y_length=5.5,
            axis_config={
                "include_numbers": False,
                "include_ticks": True,
                "tick_size": 0.05,
            },
            x_axis_config={"unit_size": 0.6},
            y_axis_config={"unit_size": 0.7},
        ).to_edge(LEFT, buff=1)

        # AXIS LABELS
        x_label = Text("Stock Price", font_size=22)
        y_label = Text("Profit / Loss", font_size=22)
        y_label.rotate(90 * DEGREES)

        x_label.next_to(axes.x_axis, DOWN, buff=0.25)
        y_label.next_to(axes.y_axis, LEFT, buff=0.25)

        # SHORT CALL PAYOFF (flipped, red)
        graph = axes.plot(
            lambda x: min(2 - max(x - 5, 0), 2),
            color=RED,
            stroke_width=4,
        )

        # TITLE — stays "Simple Call" but red
        title = Text("Simple Call", color=RED, font_size=34)
        title.to_edge(UP, buff=0.5)

        # PROS TITLE
        pros_title = Text("Pros", color=GREEN, font_size=30)
        pros_title.scale(1.15)

        # PROS (exact inverted meaning of previous Cons)
        pro1 = Text("Not a speculative position", color=GREEN, font_size=22)
        pro2 = Text("Benefits from ongoing time decay", color=GREEN, font_size=22)
        pro3 = Text("High probability of expiring out-of-the-money", color=GREEN, font_size=22)

        pros_group = VGroup(pros_title, pro1, pro2, pro3).arrange(
            DOWN, aligned_edge=LEFT, buff=0.35
        )

        pros_group.next_to(axes, RIGHT, buff=1.3)

        # --- ANIMATION ---
        self.play(FadeIn(axes))
        self.play(FadeIn(x_label), FadeIn(y_label))
        self.play(Create(graph))
        self.play(FadeIn(title))

        # Fade in Pros one by one
        self.play(FadeIn(pros_title))
        self.wait(0.25)
        self.play(FadeIn(pro1))
        self.wait(0.25)
        self.play(FadeIn(pro2))
        self.wait(0.25)
        self.play(FadeIn(pro3))

        self.wait()
