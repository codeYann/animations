# 2024/06/18

from manim import *


class DealingWithMobjects(Scene):
    def construct(self):

        bits = [0, 1, 0, 1, 0, 1, 0, 0, 0]
        boxes = [
            Square()
            .set(width=0.5, color=WHITE, stroke=RED)
            .add(Text(f"{i}").set(width=0.1))
            for i in bits
        ]

        group = VGroup(*boxes).set_x(0).arrange(buff=0)
        self.play(Write(group))

        for i in range(len(group)):
            self.play(group[i].animate.set(color=RED))

        for i in range(len(group) - 1, -1, -1):
            self.play(group[i].animate.set(color=WHITE))


class WorkingWithGraphs(Scene):
    def construct(self):

        ax = Axes(x_range=[-3, 3], y_range=[-3, 3])
        self.play(Write(ax))

        graph = ax.plot(lambda x: 3 * x**2, color=RED)

        self.play(Create(graph))

        area = ax.get_area(graph, x_range=[-1, 0])

        self.play(Create(area))
        self.play(area.animate.set_color(WHITE))
