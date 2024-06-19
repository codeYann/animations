from manim import *


class Positions(Scene):
    def construct(self):
        plane = NumberPlane()
        self.play(Create(plane))

        circle = Circle(radius=1, fill_opacity=0.5)
        dot = Dot(color=BLUE).set(width=0.45)

        self.play(Write(circle))
        self.play(circle.animate.set(width=0.5))
        self.play(ReplacementTransform(circle, dot))

        self.play(dot.animate.shift([-3, 2, 0]))
        self.play(dot.animate.move_to([3, 2, 0]))
        self.play(dot.animate.move_to(ORIGIN))

        square = Square(color=PURPLE_B).move_to([4, 2, 0])
        # self.play(dot.animate().shift([4, 2, 0]))
        self.play(ReplacementTransform(dot, square))

        self.wait(1)


class CriticalPoints(Scene):
    def construct(self):
        plane = NumberPlane()

        circle = Circle(color=GREEN, fill_opacity=0.5)

        self.play(Write(plane), Create(circle))

        directions = [ORIGIN, UP, UR, RIGHT, DR, DOWN, DL, LEFT, UL]

        group = VGroup()

        group.add(circle)

        for direction in directions:
            cross = Cross(scale_factor=0.2).move_to(
                circle.get_critical_point(direction)
            )
            group.add(cross)
            self.play(Create(cross))

        
        self.play(group.animate.to_corner(UL))
        self.play(group.animate.arrange(RIGHT))



