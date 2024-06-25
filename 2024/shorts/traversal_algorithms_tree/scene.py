from manim import *
import networkx as nx
from src.tree import Tree, Node
from src.scene import CustomScene
from typing import Tuple, List


class TraversalAlgorithmsTree(CustomScene):
    graph: Graph = None
    graph_group = None

    def generate_graph_components(self) -> Tuple[List[int], List[Tuple[int, int]]]:
        vertices = [45, 25, 68, 12, 35, 55, 100, 39, 99]

        edges = [
            (45, 68),
            (45, 25),
            (25, 35),
            (25, 12),
            (35, 39),
            (68, 100),
            (68, 55),
            (100, 99),
        ]

        return (vertices, edges)

    def fill_graph(
        self, G: nx.Graph, vertices: List[int], edges: List[Tuple[int, int]]
    ) -> None:
        for v in vertices:
            G.add_node(str(v))

        for u, v in edges:
            G.add_edge(str(u), str(v))

    def visited_callback(self, root: Node) -> None:
        v = self.graph.vertices.get(root.key)

        self.play(
            Indicate(self.graph_group[0], color=GREEN),
            v.animate.set(stroke_color=GREEN, run_time=1.2),
        )

        self.small_pause()

    def processed_callback(self, root: Node) -> None:
        v = self.graph.vertices.get(root.key)

        self.play(
            Indicate(self.graph_group[1], color=ORANGE),
            v.animate.set(stroke_color=ORANGE),
        )

        self.small_pause()

    def generate_tree(self) -> None:
        vertices, edges = self.generate_graph_components()

        G = nx.Graph()

        self.fill_graph(G, vertices, edges)

        vertex_config = {
            str(v): {
                "radius": 0.45,
                "color": 0,
                "stroke_color": WHITE,
                "stroke_width": 4,
            }
            for v in vertices
        }

        graph_config = {
            "labels": True,
            "layout": "tree",
            "layout_scale": (2.5, 3),
            "label_fill_color": WHITE,
            "vertex_config": vertex_config,
            "root_vertex": str(vertices[0]),
        }

        self.graph = Graph(
            vertices=list(G.nodes),
            edges=list(G.edges),
            **graph_config,
        )

        tree = Tree()

        for v in vertices:
            tree.insert(str(v))

        processed = Circle(color=RED, fill_opacity=1).set(width=0.30)
        processed_label = MathTex("Processado").set(width=1.5).next_to(processed, RIGHT)

        visited = (
            Circle(color=GREEN, fill_opacity=1).set(width=0.30).next_to(processed, DOWN)
        )
        visited_label = MathTex("Visitado").set(width=1.3).next_to(visited, RIGHT)

        self.graph_group = (
            VGroup(visited, processed, processed_label, visited_label)
            .move_to([0, 6, 0])
            .scale(1.5)
        )

        self.play(Write(self.graph), run_time=1.5)
        self.play(Create(self.graph_group))

        tree.inorder_traversal(
            tree.root, self.processed_callback, self.visited_callback
        )

        self.pause()

    def construct(self):

        setup_group = self.setup_title_and_watermark("Percurso em ordem")

        self.play(Write(setup_group))

        self.small_pause()

        self.play(Unwrite(setup_group))

        self.generate_tree()
