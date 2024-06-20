from manim import *

SCALE_FACTOR = 1

tmp_pixel_height = config.pixel_height
config.pixel_height = config.pixel_width
config.pixel_width = tmp_pixel_height

config.frame_height = config.frame_height / SCALE_FACTOR
config.frame_width = config.frame_height * 9 / 16

FRAME_HEIGHT = config.frame_height
FRAME_WIDTH = config.frame_width


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

    def setup_border(self, shows_border=True) -> None:
        if shows_border:
            border = Rectangle(width=FRAME_WIDTH, height=FRAME_HEIGHT, color=WHITE)
            self.play(Create(border))


class SetsOperations(CustomScene):
    def setup_title_and_watermark(self, title: str, watermark="@yan.rodriguescs"):
        title = MathTex(title, color=RED).set(width=1.5).to_corner(UP)

        watermark = (
            Text(watermark, color="#b2b2b2", font_size=16)
            .next_to(title, DOWN)
            .set(width=0.9)
        )

        return VGroup(title, watermark)

    def generate_set(self, label_text: str, color: str):
        set_circle = Circle(stroke_width=3, stroke_color=color)
        set_label = MathTex(label_text, color=color).next_to(set_circle, 1.25 * DOWN)
        return VGroup(set_circle, set_label)

    def construct(self):
        self.setup_border(shows_border=False)

        setup = self.setup_title_and_watermark(r"Conjuntos")

        self.play(Write(setup), run_time=1)

        set_a = self.generate_set("A", ORANGE)
        set_b = self.generate_set("B", BLUE_D)

        set_b.shift([1, 0, 0])

        group = VGroup(set_a, set_b).set_x(0)

        operations = [
            (r"A \cap B", PURE_GREEN),
            (r"A \cup B", PURE_RED),
            (r"A \setminus B", ORANGE),
            (r"B \setminus A", BLUE_D),
        ]

        animation_from_operation = [
            Intersection(set_a[0], set_b[0], color=PURE_GREEN, fill_opacity=0.5),
            Union(set_a[0], set_b[0], color=PURE_RED, fill_opacity=0.5),
            Difference(set_a[0], set_b[0], color=ORANGE, fill_opacity=0.5),
            Difference(set_b[0], set_a[0], color=BLUE_D, fill_opacity=0.5),
        ]

        self.play(Write(group))

        for (operation_text, color), animation in zip(
            operations, animation_from_operation
        ):
            operation = MathTex(operation_text, color=color).next_to(group, 2 * UP)

            self.play(LaggedStart(Write(operation)))
            self.small_pause()

            self.play(FadeIn(animation))
            self.play(Unwrite(operation), Unwrite(animation))

            self.small_pause()
