from manim import *
import math
import random

class OptionsIntro(Scene):
    def construct(self):

        # --- AXES (slightly smaller) ---
        axes = Axes(
            x_range=[0, 12, 1],
            y_range=[0, 80, 10],
            x_length=7,      # slightly smaller
            y_length=5.3,    # slightly smaller
            axis_config={"include_numbers": False},
        ).to_edge(DOWN)

        x_label = Text("Time", font_size=26).next_to(axes.x_axis, DOWN)
        y_label = Text("Price", font_size=26).next_to(axes.y_axis, LEFT)

        # --- SLOWER EXPONENTIAL WITH NOISE ---
        def curve_points():
            pts = []
            for x in [i * 0.2 for i in range(61)]:
                base = 12 * math.exp(x * 0.16)   # slower exponential
                noise = random.uniform(-2, 2)
                y = base + noise
                pts.append(axes.coords_to_point(x, y))
            return pts

        curve = VMobject(color=GREEN, stroke_width=4)
        curve.set_points_smoothly(curve_points())

        # --- TITLE ---
        title = Text(
            "Making Smarter Options",
            font_size=46,
            weight=BOLD
        ).to_edge(UP)

        # --- ANIMATION ---
        self.play(Create(axes))
        self.play(FadeIn(x_label), FadeIn(y_label))
        self.play(Create(curve), run_time=2.5)
        self.play(FadeIn(title, shift=UP*0.3))
        self.wait(1)
