from manim import *

class OptionPayoffScene(Scene):
    def construct(
        self,
        title_text: str,
        title_color: str,
        payoff_func,
        payoff_color: str,
        pros_or_cons_title: str,
        pros_or_cons_color: str,
        pros_or_cons_items: list[str],
    ):

        # --- AXES ---
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

        # --- AXIS LABELS ---
        x_label = Text("Stock Price", font_size=22)
        y_label = Text("Profit / Loss", font_size=22)
        y_label.rotate(90 * DEGREES)
        x_label.next_to(axes.x_axis, DOWN, buff=0.25)
        y_label.next_to(axes.y_axis, LEFT, buff=0.25)

        # --- P/L GRAPH ---
        graph = axes.plot(
            payoff_func,
            color=payoff_color,
            stroke_width=4
        )

        # --- TITLE ---
        title = Text(title_text, color=title_color, font_size=34)
        title.to_edge(UP, buff=0.5)

        # --- Pros / Cons group ---
        pc_title = Text(pros_or_cons_title, color=pros_or_cons_color, font_size=30).scale(1.15)
        pc_items = [Text(item, color=pros_or_cons_color, font_size=22) for item in pros_or_cons_items]
        pc_group = VGroup(pc_title, *pc_items).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        pc_group.next_to(axes, RIGHT, buff=1.3)

        # --- ANIMATION ---
        self.play(FadeIn(axes))
        self.play(FadeIn(x_label), FadeIn(y_label))
        self.play(Create(graph))
        self.play(FadeIn(title))

        # Fade in pros/cons line by line
        self.play(FadeIn(pc_title))
        for item in pc_items:
            self.wait(0.25)
            self.play(FadeIn(item))

        self.wait()
