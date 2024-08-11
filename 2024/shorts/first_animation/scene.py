# 2024/06/17

# from manim import *
from manim import (
    Scene,
    Circle,
    Triangle,
    RED,
    BLUE,
    Transform,
    Create,
    GREEN,
    UL,
    UR,
    DR,
    DL,
    Square,
    Line,
    FadeOut,
    Dot,
)


class CreateCircle(Scene):
    """
    This scene create a circle turns it into a square and then into a triangle. After that it shifts
    the triangle on the corner directions
    """

    def construct(self):
        circle = Circle()

        self.play(Create(circle))
        self.play(circle.animate.set_fill(GREEN, opacity=0.5))
        self.play(circle.animate.set_color(GREEN))

        square = {
            "mobject": Square(),
            "color": BLUE,
            "opacity": 0.5,
        }

        triangle = {"mobject": Triangle(), "color": RED, "opacity": 0.5}

        for shape in [square, triangle]:
            self.play(Transform(circle, shape["mobject"]))
            self.play(circle.animate.set_fill(shape["color"], opacity=shape["opacity"]))
            self.play(circle.animate.set_color(shape["color"]))
            self.wait(0.5)

        for direction in [UL, UR, DR, DL]:
            self.play(circle.animate.to_corner(direction), run_time=2)

        self.play(FadeOut(circle))
        self.wait(1)


class CreatePoints(Scene):
    """Creating a triangle :)"""

    def construct(self):
        A = [-1, -1, 0]
        B = [0, 2, 0]
        C = [2, 1, 0]

        a = Line(A, B)
        b = Line(B, C)
        c = Line(C, A)

        b.append_points(c.points)
        c.append_points(a.points)

        self.play(Create(Dot(A)), Create(Dot(B)), Create(Dot(C)))

        self.play(Create(a))
        self.play(a.animate.append_points(b.points))
        self.wait(0.5)

        self.play(Create(b))
        self.play(b.animate.append_points(c.points))
        self.wait(0.5)

        self.play(Create(c))
        self.play(c.animate.append_points(a.points))
        self.wait(0.5)
