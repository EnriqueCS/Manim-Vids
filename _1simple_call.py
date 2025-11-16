from manim import *

class SimpleCall(Scene):
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
            x_axis_config={
                "unit_size": 0.6,   # larger spacing between ticks → fewer ticks
            },
            y_axis_config={
                "unit_size": 0.7,
            }
        ).to_edge(LEFT, buff=1)

        # AXIS LABELS
        x_label = Text("Stock Price", font_size=22)
        y_label = Text("Profit / Loss", font_size=22)
        y_label.rotate(90 * DEGREES)

        x_label.next_to(axes.x_axis, DOWN, buff=0.25)
        y_label.next_to(axes.y_axis, LEFT, buff=0.25)

        # P/L GRAPH (simple call payoff)
        graph = axes.plot(
            lambda x: max(x - 5, -2),
            color=GREEN,
            stroke_width=4,
        )

        # TITLE
        title = Text("Simple Call", color=GREEN, font_size=34)
        title.to_edge(UP, buff=0.5)

        # CONS TITLE
        cons_title = Text("Cons", color=RED, font_size=30)
        cons_title.scale(1.15)

        # CONS ITEMS (formal phrasing)
        con1 = Text("Largely a speculative position", color=RED, font_size=22)
        con2 = Text("Susceptible to ongoing time decay", color=RED, font_size=22)
        con3 = Text("Low probability of expiring in-the-money", color=RED, font_size=22)

        cons_group = VGroup(cons_title, con1, con2, con3).arrange(
            DOWN, aligned_edge=LEFT, buff=0.35
        )

        cons_group.next_to(axes, RIGHT, buff=1.3)

        # --- ANIMATION ---
        self.play(FadeIn(axes))
        self.play(FadeIn(x_label), FadeIn(y_label))
        self.play(Create(graph))
        self.play(FadeIn(title))

        # Animate cons line by line
        self.play(FadeIn(cons_title))
        self.wait(0.25)
        self.play(FadeIn(con1))
        self.wait(0.25)
        self.play(FadeIn(con2))
        self.wait(0.25)
        self.play(FadeIn(con3))

        self.wait()
