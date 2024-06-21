# Made 2024/06/20

from manim import *


class CustomScene(Scene):
    """
    CustomScene defines a bunch of utilitary functions such as pauses and many others.
    """

    def small_pause(self, n=0.5) -> None:
        self.wait(n)

    def pause(self, n=1.5) -> None:
        self.wait(n)

    def medium_pause(self, n=3) -> None:
        self.wait(n)

    def long_pause(self, n=5) -> None:
        self.wait(n)

    def setup_title_and_watermark(self, title: str, watermark="@yan.rodriguescs"):
        title = Text(title, color=RED).set(width=3).to_corner(UP)

        watermark = (
            Text(watermark, color="#b2b2b2", font_size=24)
            .next_to(title, DOWN)
            .set(width=1.4)
        )

        return VGroup(title, watermark)


plane_config = {
    "x_range": np.array([-2.5, 2.5, 1]),
    "y_range": np.array([-2.5, 2.5, 1]),
    "axis_config": {
        "unit_size": 3,
        "include_numbers": True,
        "numbers_to_include": np.array([-1, 1]),
    },
}

circle_config = {"radius": 3, "color": BLUE}
dot_config = {"color": RED}
hypo_config = {"color": RED}
arc_config = {
    "radius": 0.5,
    "stroke_width": 2,
    "color": RED,
}

oppo_config = {"color": RED}

graph_plane_config = {
    "x_range": np.array([0, 4.3 * PI, 1]),
    "y_range": np.array([-2, 2, 1]),
    # "number_line_config": {
    #     "include_tip": True,
    # },
    "x_axis_config": {
        "unit_size": 1.5 / PI,
        # "tick_frequency": PI,
        "include_tip": True,
    },
    "y_axis_config": {"unit_size": 1},
}


def toward(angle):
    return np.array([np.cos(angle), np.sin(angle), 0])


class Cosine(CustomScene):
    theta = None
    plane = None
    circle = None
    point = None
    graph_plane = None

    def show_up_cosine(self):
        self.theta = ValueTracker(PI / 3)
        self.plane = NumberPlane(**plane_config)
        self.circle = Circle(**circle_config)

        self.play(Create(self.plane), Create(self.circle))

        self.small_pause()

        brace = BraceLabel(
            Line(self.circle.get_center(), RIGHT * self.circle.width / 2), "1"
        )

        self.play(Create(brace))
        self.play(FadeOut(brace))

        dot = Dot(
            self.circle.point_at_angle(np.mod(self.theta.get_value(), TAU)),
            **dot_config
        )

        hypo = always_redraw(
            lambda: Line(
                self.circle.get_center(),
                self.circle.point_at_angle(np.mod(self.theta.get_value(), TAU)),
                **hypo_config
            ),
        )

        arc = always_redraw(
            lambda: Arc(
                arc_center=self.circle.get_center(),
                angle=self.theta.get_value(),
                **arc_config
            ),
        )

        label = MathTex(r"\theta")
        label.add_updater(
            lambda l: l.move_to(
                self.circle.get_center() + 0.75 * toward(self.theta.get_value() / 2)
            )
        )

        angle_label = VGroup(arc, label)

        self.play(Create(dot))
        self.play(Create(hypo))
        self.play(Create(angle_label))
        self.small_pause()

        oppo = always_redraw(
            lambda: Line(
                self.circle.point_at_angle(
                    np.mod(self.theta.get_value(), TAU),
                ),
                self.circle.get_center()
                + UP * self.circle.width / 2 * np.sin(self.theta.get_value()),
                **oppo_config
            )
        )

        self.play(Create(oppo))
        self.small_pause()

        dot.add_updater(
            lambda d: d.move_to(
                self.circle.point_at_angle(np.mod(self.theta.get_value(), TAU))
            )
        )

        self.point = VGroup(dot, hypo, oppo)

        cos_equation = MathTex(r"\cos\theta")

        brace = always_redraw(
            lambda: Brace(
                oppo, UP * np.sign(np.sin(self.theta.get_value()))
            ).put_at_tip(cos_equation)
        )

        self.play(GrowFromCenter(brace), Write(cos_equation))
        self.pause()

        self.play(self.theta.animate.set_value(4 * PI / 5))
        self.small_pause()

        self.play(self.theta.animate.set_value(0.8 * PI))
        self.small_pause()

        self.play(self.theta.animate.set_value(-1))
        self.pause()

        self.play(self.theta.animate.set_value(PI / 6))

        self.play(FadeOut(brace), FadeOut(cos_equation), FadeOut(angle_label))

        self.play(ApplyMethod(self.theta.set_value, 0))

    def show_graph(self):
        all_objects = VGroup(self.plane, self.circle)
        self.play(ApplyMethod(all_objects.scale, 1 / 6))

        wrap = Square(side_length=all_objects.width + 0.5, fill_color=DARK_GREY)
        self.play(DrawBorderThenFill(wrap))

        all_objects.add(wrap)

        self.play(all_objects.animate.to_edge(UP).set_x(0))

        self.bring_to_back(self.plane, self.circle)

        self.graph_plane = Axes(**graph_plane_config).to_edge(DOWN * -5)

        numbers = VGroup()

        for i in range(1, 4):
            label = (
                MathTex(str(i), r"\pi")
                .move_to(self.graph_plane.coords_to_point(i * PI, -0.3))
                .scale(0.5)
            )
            numbers.add(label)

        numbers.add(
            MathTex(r"\theta")
            .move_to(self.graph_plane.coords_to_point(4.2 * PI, -0.5))
            .scale(0.75)
        )

        cos_equation = MathTex(r"\cos\theta").next_to(self.graph_plane, DOWN)

        self.play(Create(self.graph_plane), Write(numbers), Write(cos_equation))

    def draw_graph(self):
        cosine_graph = ParametricFunction(
            lambda t: self.graph_plane.coords_to_point(t, np.cos(t)),
            t_range=[-0.001, 3.9 * PI],
            color=GOLD,
        )

        dot = Dot(**dot_config)
        dot.add_updater(
            lambda d: d.move_to(
                self.graph_plane.coords_to_point(
                    self.theta.get_value(), np.cos(self.theta.get_value())
                )
            )
        )

        perpend = always_redraw(
            lambda: Line(
                self.graph_plane.coords_to_point(
                    self.theta.get_value(), np.cos(self.theta.get_value())
                ),
                self.graph_plane.coords_to_point(self.theta.get_value(), 0),
                **oppo_config
            )
        )

        self.add(cosine_graph, perpend, dot)
        cosine_graph.save_state()

        self.play(
            Create(cosine_graph, rate_func=linear, run_time=10),
            ApplyMethod(self.theta.set_value, 3.9 * PI, rate_func=linear, run_time=10),
        )
        self.pause()

    def construct(self):
        title = self.setup_title_and_watermark(r"Função cos x")

        self.play(Write(title))
        self.wait(0.5)
        self.play(Unwrite(title))

        self.show_up_cosine()
        self.show_graph()
        self.draw_graph()
