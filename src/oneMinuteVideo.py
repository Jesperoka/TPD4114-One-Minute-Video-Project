if __name__ == "__main__":
    import useManim
    useManim.runManim(__file__, "C:/manim",  "OneMinuteVideo")
else:
    import manimlib as m

    def scene1(self):
        circle = m.Circle()
        circle.set_fill(m.BLUE, opacity=0.5)
        circle.set_stroke(m.BLUE_E, width=4)

        # self.add(circle)

        square = m.Square()

        self.play(m.ShowCreation(square))
        self.wait()
        self.play(m.ReplacementTransform(square, circle))
        self.wait()

    def scene2(self):
        circle = m.Circle()
        circle.set_fill(m.BLUE, opacity=0.5)
        circle.set_stroke(m.BLUE_E, width=4)

        # self.add(circle)

        square = m.Square()

        self.play(m.ShowCreation(square))
        self.wait()
        self.play(m.ReplacementTransform(square, circle))
        self.wait()

    class OneMinuteVideo(m.Scene):
        def construct(self):
            scene1(self)
            scene2(self)
