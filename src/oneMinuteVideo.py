if __name__ == "__main__":
    import useManim
    useManim.runManim(__file__, "C:/manim",  "OneMinuteVideo")
else:
    import manimlib as m

    def scene1(self):
        text = m.Text("Feedback Loop", font="Copperplate").scale(2)
        # text.arrange(m.RIGHT, buff=m.MED_SMALL_BUFF)
        self.play(m.Write(text), run_time=1)
        self.wait()
        return text
        
    def scene2(self,  text):
        line = m.Line().scale(2.5).shift(1.1*m.UP)
        roundedRectangle = m.RoundedRectangle(color=m.ORANGE).scale(1.3).flip().shift(0.2*m.DOWN)
        transform1 = text.animate.shift(2*m.UP).scale(0.5)
        transform2 = m.FadeIn(line, run_time=2)
        transform3 = m.FadeToColor(text[8:], m.ORANGE)
        transform4 = m.FadeToColor(line, m.ORANGE)
        transform5 = m.Transform(line, roundedRectangle)
        # transform5 = m.ShowCreation(roundedRectangle)
        self.play(transform1, transform2)
        self.play(transform3, transform4)
        self.play(transform5)

    class OneMinuteVideo(m.Scene): 
        def construct(self):
            text = scene1(self)
            scene2(self, text)
