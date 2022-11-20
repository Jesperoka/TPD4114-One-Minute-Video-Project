if __name__ == "__main__":
    import useManim
    useManim.runManim(__file__, "C:/manim",  "OneMinuteVideo")
else:
    import manimlib as m
    from itertools import cycle

    # CONFIG
    # ---------------------------------------------------------------
    WORD_FONT = "Courier New"
    TEXT_FONT = "Constantia"
    WIKI_TEXT_FONT = "Arial"
    TEXT_LINE_SPACING = 1.5
    TEXT_SCALE = 0.6
    DOUBLE = 2.0
    HALF = 0.5
    OPACITY_FADED = 0.4
    ANIM_TIME_VERY_SHORT = 0.3
    ANIM_TIME_SHORT = 0.5
    ANIM_TIME_MEDIUM = 1
    ANIM_TIME_LONG = 2
    Y_SHIFT = 2
    X_SHIFT = 3.1
    # ---------------------------------------------------------------



    # LOOP ANIMATION
    # ---------------------------------------------------------------
    def loopOnce(self, feedbackLoop, colorOut: str, func, inputMobject, dotIn):
        CONNECTOR_TIME = 0.5
        QUICK_LOOP_TIME = (1/4.75)*CONNECTOR_TIME
        TRANSFORM_TIME = 0.01

        self.play(m.MoveAlongPath(dotIn, feedbackLoop[0], rate_func=m.linear, run_time=QUICK_LOOP_TIME))
        self.play(m.Transform(dotIn, feedbackLoop[1], rate_func=m.rush_from, run_time=QUICK_LOOP_TIME))
        dotOut = m.Dot(feedbackLoop[2].get_start(), radius=0.1, color=colorOut).move_to(feedbackLoop[2].get_start())
        self.play(m.ReplacementTransform(dotIn, dotOut, run_time=QUICK_LOOP_TIME))
        outputMobject = func()
        self.play(m.MoveAlongPath(dotOut, feedbackLoop[2], rate_func=m.linear, run_time=QUICK_LOOP_TIME))
        self.play(m.MoveAlongPath(dotOut, feedbackLoop[3], rate_func=m.linear, run_time=CONNECTOR_TIME))
        self.play(m.ReplacementTransform(inputMobject, outputMobject), run_time=TRANSFORM_TIME)
        return outputMobject, dotOut
    # ---------------------------------------------------------------


    # SCENES
    # ---------------------------------------------------------------
    def scene1(self):
        text = m.Text("Feedback Loop", font=WORD_FONT).scale(DOUBLE)
        self.play(m.Write(text), run_time=ANIM_TIME_MEDIUM)
        self.wait()
        return text
        
    def scene2(self,  text1): # Idea: set color orange to begin with, then set it white before text appears. (or use updaters)
        line = m.Line().scale(2.5).shift(1.1*m.UP)
        roundedRectangle = m.RoundedRectangle(color=m.ORANGE).scale(1.3).flip().shift(0.2*m.DOWN)
        text2 = m.Text("A loop is something that loops back on itself.", font=TEXT_FONT, slant=m.ITALIC)
        text3 = m.Text(" -Unknown Author", font=TEXT_FONT)
        quote = m.VGroup(text2, text3).arrange(m.RIGHT).shift(1.25*Y_SHIFT*m.DOWN).scale(TEXT_SCALE)
        all = m.VGroup(line, roundedRectangle, text1, text2, text3, quote)
        transform1 = text1.animate.shift(Y_SHIFT*m.UP).scale(HALF)
        transform2 = m.FadeIn(line, run_time=2)
        transform3 = m.FadeToColor(text1[8:], m.ORANGE)
        transform4 = m.FadeToColor(line, m.ORANGE)
        transform5 = m.Transform(line, roundedRectangle)
        self.play(transform1, transform2)
        self.play(transform3, transform4)
        self.play(transform5)
        self.play(m.FadeIn(quote))
        self.wait()
        self.play(m.FadeOut(all))

    # TODO: use shift(UP + RIGHT) instead of shift(UP).shift(RIGHT) 
    def scene3(self):
        ADJUST = 0.1*m.DOWN
        logo = m.SVGMobject("Wikipedia-logo-v2-en.svg", fill_color=m.GREY_C, stroke_color=m.GREY_B).shift(Y_SHIFT*m.UP).shift(1.75*X_SHIFT*m.LEFT)
        title = m.Text("Feedback", font="Times New Roman", color=m.GREY_C).shift(Y_SHIFT*m.UP).shift(X_SHIFT*m.LEFT)
        sepLine = m.Line(1.3*X_SHIFT*m.LEFT, 1.46*X_SHIFT*m.RIGHT, color=m.GREY_C).shift(0.825*Y_SHIFT*m.UP)
        credit = m.Text("From Wikipedia, the free encyclopedia").shift(0.7*Y_SHIFT*m.UP).shift(0.55*X_SHIFT*m.LEFT).scale(0.8*TEXT_SCALE).set_color(m.GREY_C)
        bodyText = m.Text(
            """
                Feedback occurs when outputs of a system are routed back as 
                inputs as part of a chain of cause-and-effect that forms a 
                circuit or loop.[1] The system can then be said to feed back 
                into itself. The notion of cause-and-effect has to be handled 
                carefully when applied to feedback systems.
            """, font=WIKI_TEXT_FONT, color=m.GREY_C, line_spacing_height=TEXT_LINE_SPACING
        ).scale(TEXT_SCALE).shift(ADJUST)
        bodyText[111:114].set_color(m.BLUE_B).set_opacity(0.5)
        continuation = m.Text(
            """
                Simple causal reasoning about a feedback system is difficult 
                because the first system influences the second and second system 
                influences the first, leading to a circular argument. 
                This makes reasoning based upon cause and effect tricky, 
                and it is necessary to analyze the system as a whole. 
                As provided by Webster, feedback in business is the transmission 
                of evaluative or corrective information about an action, event, 
                or process to the original or controlling source.[2]
                
                    — Karl Johan Åström and Richard M.Murray, Feedback Systems: 
                      An Introduction for Scientists and Engineers[3]
            """, font=WIKI_TEXT_FONT, color=m.GREY_C, line_spacing_height=TEXT_LINE_SPACING, opacity=1
        ).scale(TEXT_SCALE)
        textLines = (continuation[0 : 52], continuation[52 : 52+55],
                    continuation[52+55 : 52+55+46], continuation[52+55+46 : 52+55+46+48],
                    continuation[52+55+46+48 : 52+55+46+48+43], continuation[52+55+46+48+43 : 52+55+46+48+43+55],
                    continuation[52+55+46+48+43+55 : 52+55+46+48+43+55+55], continuation[52+55+46+48+43+55+55 : 52+55+46+48+43+55+55+45],
                    continuation[52+55+46+48+43+55+55+45 : 52+55+46+48+43+55+55+45+51], continuation[52+55+46+48+43+55+55+45+51 : 52+55+46+48+43+55+55+45+51+42]
                    )

        k = 1; animations = []
        for tLine in textLines: 
            animations.append(m.FadeIn(tLine.set_opacity(k*OPACITY_FADED).shift(2.25*Y_SHIFT*m.DOWN).shift(0.09*X_SHIFT*m.RIGHT), run_time=ANIM_TIME_SHORT))
            k = k*0.7
        all = m.VGroup(logo, title, sepLine, credit, bodyText, continuation)

        transform0 = m.FadeIn(logo)
        transform1 = m.FadeIn(title)
        transform2 = m.FadeIn(sepLine)
        transform3 = m.FadeIn(credit)
        transform4 = m.FadeIn(bodyText)
        highlight = m.FadeToColor(bodyText[0:111], m.ORANGE, run_time=ANIM_TIME_MEDIUM)
        transform5 = m.AnimationGroup(*animations, lag_ratio=0.2)

        fullAnimation = m.AnimationGroup(*[m.AnimationGroup(*[transform0, transform1]), transform2, transform3, transform4, transform5], lag_ratio=0.2)
        self.play(fullAnimation)
        self.play(highlight)
        return all, textLines

    def scene4(self, all3):
        triangle = m.Triangle(stroke_color=m.ORANGE).rotate(-m.PI/2, m.Z_AXIS)
        # qMark = m.Tex("?").move_to(triangle.get_center_of_mass()).set_color(m.ORANGE)
        triangleVertices = triangle.get_vertices()
        output = m.Line(triangleVertices[0], triangleVertices[0] + 2*m.RIGHT).set_color(m.ORANGE)
        yDiff = triangleVertices[1][1]-triangleVertices[2][1]
        midPoint = triangleVertices[1] - 0.5*yDiff*m.Y_AXIS
        input = m.Line(midPoint, midPoint + 2*m.LEFT).set_color(m.ORANGE).flip()
        connector = m.Polyline(triangleVertices[0] + 2*m.RIGHT, triangleVertices[0] + 2*m.RIGHT + 2*m.DOWN, midPoint + 2*m.LEFT + 2*m.DOWN, midPoint + 2*m.LEFT).set_color(m.ORANGE)
        ADJUST = 0.2
        text1 = m.Text("Input", font=WORD_FONT, color=m.WHITE).move_to(input.get_center() + ADJUST*m.UP).scale(TEXT_SCALE)
        text2 = m.Text("System", font=WORD_FONT, color=m.WHITE).move_to(triangle.get_center_of_mass()+0.15*m.RIGHT).scale(TEXT_SCALE)
        text3 = m.Text("Output", font=WORD_FONT, color=m.WHITE).move_to(output.get_center() + ADJUST*m.UP).scale(TEXT_SCALE)

        feedbackLoop = m.VGroup(input, triangle, output, connector, text1, text2, text3)
        savedText = all3[4][0:111].save_state()
        self.play(m.AnimationGroup(*[m.ReplacementTransform(all3[4][0:111], feedbackLoop), m.FadeOut(all3[0:4]), m.FadeOut(all3[4][111::]), m.FadeOut(all3[5::])]))
        savedText = savedText.restore().set_color(m.GREY_C)
        self.wait()
        return feedbackLoop, savedText

    def scene5(self, all3, textLines, feedbackLoop, savedText):
        transform1 = m.AnimationGroup(m.FadeIn(savedText), m.FadeOut(feedbackLoop), m.FadeIn(all3))

        AMOUNT = 4
        animations = []
        for tLine in textLines: 
            animations.append(tLine.animate.set_opacity(1).shift(AMOUNT*m.UP))
        linesTransform = m.AnimationGroup(*animations, lag_ratio=0.2)

        transform2 = m.AnimationGroup(all3.animate.shift(AMOUNT*m.UP), linesTransform)
        transform3 = m.FadeToColor(all3[5][0:153], m.ORANGE)
        transform4 = m.AnimationGroup(m.AnimationGroup(m.FadeOut(all3), m.FadeOut(savedText)), m.FadeIn(feedbackLoop), lag_ratio=0.2)

        self.play(transform1)
        self.play(transform2)
        self.play(transform3)
        self.wait()
        self.play(transform4)

    def cornersHelper(feedbackLoop):
        corners = feedbackLoop[3].get_vertices()
        lastCorner = (corners[0]-m.X_AXIS*(corners[1][0]-corners[2][0])).reshape((1,3))
        corners = m.np.vstack((corners, lastCorner))
        return corners

    def scene6(self, feedbackLoop):
        ADJUST = 0.3
        arrow = m.Arrow(m.LEFT, m.RIGHT).flip().scale(ADJUST)
        arrowText = m.Text("This one's my favorite!").scale(ADJUST)
        corners = cornersHelper(feedbackLoop)
        clockTime = m.DecimalNumber(0.00, num_decimal_places=2, text_config={"font":"DSEG7 Classic"}).shift(1.75*m.UP).scale(TEXT_SCALE)
        clockTime.add_updater(lambda t: t.increment_value(0.01))
        synonyms = m.VGroup(
                        m.Text("process", font=WORD_FONT, color=m.BLUE_D), 
                        m.Text("function", font=WORD_FONT, color=m.BLUE_D),
                        m.Text("transformation", font=WORD_FONT, color=m.BLUE_D), 
                        m.Text("input-changing-machine", font=WORD_FONT, color=m.BLUE_D), 
                        m.Text("etc...", font=WORD_FONT, color=m.BLUE_D)
                        ).arrange(m.DOWN, center=True, aligned_edge=m.LEFT, buff=1).shift(1.69*X_SHIFT*m.LEFT).scale(0.8*TEXT_SCALE)

        transform1 = m.AnimationGroup(feedbackLoop[5].animate.set_color(m.BLUE_D), feedbackLoop[1].animate.set_color(m.BLUE_D))
        transform2 = m.AnimationGroup(
                        m.TransformFromCopy(feedbackLoop[5], synonyms[0]), 
                        m.TransformFromCopy(feedbackLoop[5], synonyms[1]), 
                        m.TransformFromCopy(feedbackLoop[5], synonyms[2]),
                        m.TransformFromCopy(feedbackLoop[5], synonyms[3]),
                        m.TransformFromCopy(feedbackLoop[5], synonyms[4]), lag_ratio=0.2)
        
        transform3 = m.AnimationGroup(
                        m.FadeIn(arrow.next_to(synonyms[4], buff=0.2)), 
                        m.FadeIn(arrowText.next_to(arrow, buff=0.2)), lag_ratio=0.1)

        transform4 = m.AnimationGroup(
                        m.FadeOut(arrow.next_to(synonyms[4], direction=m.RIGHT, buff=0.2)), 
                        m.FadeOut(arrowText.next_to(arrow, direction=m.RIGHT, buff=0.2)), lag_ratio=0.1)

        transform5 = m.AnimationGroup(feedbackLoop[1].animate.set_color(m.ORANGE),
                        m.ReplacementTransform(synonyms[0], feedbackLoop[5]), 
                        m.ReplacementTransform(synonyms[1], feedbackLoop[5]),
                        m.ReplacementTransform(synonyms[2], feedbackLoop[5]),
                        m.ReplacementTransform(synonyms[3], feedbackLoop[5]),
                        m.ReplacementTransform(synonyms[4], feedbackLoop[5]), lag_ratio=0.2)

        transform6 = m.AnimationGroup(
                        feedbackLoop[4].animate.shift(0.2*m.UP),
                        feedbackLoop[6].animate.shift(0.2*m.UP),
                        )

        CONNECTOR_TIME = 2
        QUICK_LOOP_TIME = (1/4.75)*CONNECTOR_TIME
        dotIn = m.Dot(point=corners[3], radius=0.1, color="#CA4732").shift(0.5*m.RIGHT)
        transform7 = m.FadeIn(dotIn, shift=0.5*m.RIGHT, run_time=QUICK_LOOP_TIME/4)
        transform8 = m.MoveAlongPath(dotIn, feedbackLoop[0], rate_func=m.linear, run_time=QUICK_LOOP_TIME)
        transform9 = m.ReplacementTransform(dotIn, feedbackLoop[1], rate_func=m.rush_from, run_time=QUICK_LOOP_TIME)
        
        dotOut = m.Dot(dotIn.get_center(), radius=0.1).move_to(feedbackLoop[2].start).set_color("#51AD79")
        transform10 = m.TransformFromCopy(feedbackLoop[1], dotOut, run_time=QUICK_LOOP_TIME)
        transform11 = m.MoveAlongPath(dotOut, feedbackLoop[2], rate_func=m.linear, run_time=QUICK_LOOP_TIME)

        fadeOut = m.AnimationGroup(m.FadeOut(dotOut), m.FadeOut(feedbackLoop))

        self.play(transform1)
        self.play(transform2)
        self.play(transform3)
        self.play(transform4)
        self.play(transform5)
        self.play(transform6)
        self.play(transform7)
        self.play(transform8)
        self.play(transform9)

        self.add(clockTime) #m.Clock exists
        self.wait()
        self.wait()
        self.remove(clockTime)
        
        self.play(transform10)
        self.play(transform11)
        self.play(fadeOut)
        return feedbackLoop

    def scene7(self, feedbackLoop):
        colors = cycle(["#F6BC1B","#CA4732","#FDF1A3","#51AD79","#15337E"])

        feedbackLoop1 = feedbackLoop[0:4].copy()
        feedbackLoop1.shift(Y_SHIFT*m.UP).scale(HALF)
        box1 = m.Square(side_length=0.5).next_to(feedbackLoop1[0], direction=m.UP, buff=0.2)
        box2 = m.Square(side_length=0.5).next_to(feedbackLoop1[2], direction=m.UP, buff=0.2)
        self.play(m.AnimationGroup(m.ShowCreation(feedbackLoop1), m.ShowCreation(box1), m.ShowCreation(box2), lag_ratio=0.2))
        corners1 = cornersHelper(feedbackLoop1)

        feedbackLoop2 = feedbackLoop.copy()
        feedbackLoop2.scale(HALF)
        corners2 = cornersHelper(feedbackLoop2)

        feedbackLoop3 = feedbackLoop.copy()
        feedbackLoop3.shift(Y_SHIFT*m.DOWN).scale(HALF)
        corners3 = cornersHelper(feedbackLoop3)

        def rotation25():
            box2.rotate(angle=-25*m.DEGREES)
            return box2.copy().move_to(box1.get_center())
        # def lengthen15():
        #     pass
        # def halve():
        #     pass

        colorIn = next(colors)
        dotIn = m.Dot(point=corners1[3], radius=0.1, color=colorIn)#.shift(0.5*m.RIGHT)
        for i in range(10):
            colorOut = next(colors)
            box1, dotIn = loopOnce(self, feedbackLoop1, colorOut, rotation25, box1, dotIn)
            colorIn = colorOut
            dotIn.set_color(colorIn)

    def scene8(self):
        pass

    def scene9(self):
        pass
    # ---------------------------------------------------------------



    # ANIMATION CONSTRUCTOR
    # ---------------------------------------------------------------
    class OneMinuteVideo(m.Scene): 
        def construct(self):
            text = scene1(self)
            scene2(self, text)
            all3, textLines = scene3(self)
            feedbackLoop, savedText = scene4(self, all3)
            scene5(self, all3, textLines, feedbackLoop, savedText)
            feedbackLoop2 = scene6(self, feedbackLoop)
            scene7(self, feedbackLoop2)
    # ---------------------------------------------------------------