from manim import *


class CustomScene(Scene):
    def small_pause(self, n=0.5) -> None:
        self.wait(n)

    def pause(self, n=1.5) -> None:
        self.wait(n)

    def medium_pause(self, n=3) -> None:
        self.wait(n)

    def long_pause(self, n=5) -> None:
        self.wait(n)

    def setup_title_and_watermark(self, title: str, watermark="@yan.rodriguescs"):
        title = Text(title, color=RED).set(width=4).to_edge(UP)

        watermark = Text(watermark, color="#b2b2b2").next_to(title, DOWN).set(width=2)

        return VGroup(title, watermark)
