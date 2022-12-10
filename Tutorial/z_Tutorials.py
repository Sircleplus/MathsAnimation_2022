
from manim import *  # Always at the top to start the code.

'''Text Square run_time square_attributes moving to edge'''

class Simple(Scene): #which means the name of the class that we are making and would be later used.
    def construct(self): # you have to write this to start creating self ( which refers to creating itself, you can change name but recommended not to)
        t1 = Text("Your text here") # If you wish to animate text, You can add many attributes
        sq = Square(side_length=9, stroke_color= WHITE, fill_color= BLUE, fill_opacity= 0.75).to_edge(UL,buff=0.5) # this makes square with the attributes #.to_edge and buff is used to define the position of the square once it is created
        self.play(Write(t1)) # which means start writing that
        self.play(Create(sq), run_time=3) # add run_time to specify the amount of time you want the animation to be
        self.wait() #wait after you finish writing.

'''Transformation from one shape to the another; color and opacity; Basic rotation; Uncreate; animating rotation; Fadeout;'''

class transform(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparenyc

        square = Square()  # create a square
          # rotate a certain amount with using pi as rotation metre self.play(my_mobject.animate.shift(RIGHT).rotate(PI))

        self.play(Create(square))  # animate the creation of the square
        self.play(square.animate.rotate(PI/4))
        self.play(Transform(square, circle),run_time= 1)  # Transform is used to Interpolate; covert one thing to the other. you can slow or fast the animtion by run time
        # self.play(circle.animate.set_fill(BLUE, opacity=0.8)) #can animate any dot effect
        self.play(Uncreate(square))
        # self.play(circle.animate.rotate(PI), Rotate(square, angle=PI), run_time=2)
        self.play(FadeOut(square))  # FadeOut to fade out transition
        self.wait(2)


# class pop(Scene):
#     def construct():


class sq(Scene):
    def construct(self):
        circle = Circle(radius=2)  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency
        square.next_to(circle, LEFT, buff=0.2) #.nect_to means it would come on the right side of the previous mobject
        # self.play(Create(circle),Create(square))
        self.add(square)
        self.play(Create(circle))
        #self.play()s
        self.wait()


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # .set_fill is used to set the color and transparency
        self.play(Create(circle))  # this creates the name defined to the object
        self.wait(2)

class multiplicatio(Scene):
    def construct(self):
        for a in [1,2,3]:
            theTable = []
            theTable2 = []
            for b in range(147,70,-7):
                theTable.append([1*(b)])
            for c in range(70,0,-7):
                theTable2.append([1*(c)])
            texTable = MathTable(theTable,include_outer_lines=False).scale(0.6).to_edge(UP)
            texTable.remove(*texTable.get_horizontal_lines())
            texTable2 = MathTable(theTable2,include_outer_lines=False).scale(0.65).next_to(texTable, RIGHT)
            texTable2.remove(*texTable2.get_horizontal_lines())

            self.play(Write(texTable))
            self.play(Write(texTable2))

            self.wait(5)
            self.remove(texTable)

class multiplication(Scene):
    def construct(self):
        for a in [1,2,3]:
            theTable = []
            theTable2 = []
            for b in range(147,70,-7):
                theTable.append([1*(b)])
            for c in range(70,0,-7):
                theTable2.append([1*(c)])
            texTable = MathTable(theTable,include_outer_lines=False).scale(0.6).to_edge(UP)
            texTable.remove(*texTable.get_horizontal_lines()) # to remove the lines of the table and then it looks it in the way.
            texTable2 = MathTable(theTable2,include_outer_lines=False).scale(0.65).next_to(texTable, RIGHT)
            texTable2.remove(*texTable2.get_horizontal_lines())

            self.play(Write(texTable))
            self.play(Write(texTable2))

            self.wait(2)
              
            # for index, obj in enumerate(texTable2.get_entries()):                                 #enumerate is used to mark one by one the listings of the enteries.
            #     self.add(Tex(r"{}".format(index), font_size=16).next_to(obj, RIGHT))    

            # self.wait(2)

            # texTable2.get_entries()[3].add_updater(lambda obj: obj.become(obj)) # .rotate(10*DEGREES)

            self.play(texTable.get_entries()[3].animate.scale(3).shift(4*RIGHT+1*DOWN),run_time=1.8) # Moving object slightly here and there shift

            self.wait(5)
            self.remove(texTable)

class star(Scene):
    def construct(self):
        # i=1
        # while i <= 5:
        for m in [1,2,3]:
            j=[]
            for a in range(1,5):
                j.append([a])
            # text = Tex(j)
            texTable = MathTable(j,include_outer_lines=False)
            texTable.remove(*texTable.get_horizontal_lines()) 
            # print(i*"*")
            # j=j+1
            self.play(Write(texTable))

'''There are 3 Types of tables in Manim
1. Table 
2. MobjectTable
3. MathTable'''

class ram(Scene):
    def construct(self): 
        t0 = MobjectTable(                # This is way to make tables. in this every element must be an mobject otherwise use the "Table" rather than MobjectTable
            [[Text("Ram")],
            [Square(side_length=0.5)],
            [Text("Sita")]])
        t0.get_entries((1,2)).rotate(PI/4)
        t0.remove(*t0.get_horizontal_lines()) 
        self.play(Write(t0),run_time=8)
        self.wait(3)

'''Using Font's in Manim''' '''How to change fonts'''
from manim_fonts import *               #First import * from manim_fonts (you must have manim_fonts downloaded)

class fontcheck(Scene):                 
    def construct(self):
        with RegisterFont("Bungee Spice") as fonts:              #define the font that you want to use from the Google fonts
            ram = Text("Ram   Shyaam  &  Sita" ,font=fonts[0])  #only Text function works with the different font and use ,font=fonts[0]  to use it
            self.play(Write(ram))
            self.wait(3)

'''Changing the background of manim page.. and also you can turn it into some kind of Light mode'''

from manim import *
config.background_color = "#FFD000"  #changing the backgorund colour to anything
Mobject.set_default(color=BLACK) # changing the default setting of the attribute of something.
Tex.set_default(color=BLACK)        # just change the tex to black and all the text would turn to black.
Text.set_default(color=BLACK)

class check(Scene):
    def construct(self):
        with RegisterFont("Kalam") as fonts:
            some_text = Text("This text should be black and also good font", font=fonts[0])
            self.play(Create(some_text), run_time=3)
            self.wait()

class tri(Scene):
    def construct(self):
        with RegisterFont("Kalam") as fonts:
            text = Text("Triangle",font=fonts[0]).scale(2.5).to_edge(UP) 
            triangle = Triangle(stroke_color= BLACK, fill_color= WHITE, fill_opacity= 0.75).scale(2).shift(DOWN*0.8+LEFT*3) #Shifting objects can use + for multiple things
            isosceles = Polygon([-5, 1.5, 0], [-2, 1.5, 0], [-3.5, -2, 0],stroke_color= BLACK, fill_color= WHITE, fill_opacity= 0.75).rotate(PI).shift(RIGHT*4) # Draw any shape with the help of polygons use co-ordinate points to guide the shape
            Scalene = Polygon([-5, 1.5, 0], [-2, 0, 0], [-3.5, -2, 0],stroke_color= BLACK, fill_color= WHITE, fill_opacity= 0.75).rotate(PI).to_edge(RIGHT,buff=2) 
            self.play(Write(text))
            self.wait(3)
            self.play(Create(triangle))
            self.wait(3)
            self.play(Write(isosceles))
            self.wait(3)
            self.play(Write(Scalene))
            self.wait()


class triangle1(Scene):
    def construct(self):
        text = Text("What is Triangle ?").scale(1.5).to_edge(UP)
        Tri = Triangle(stroke_color= BLACK, fill_color= BLUE, fill_opacity= 0.5).scale(2)
        text2 = Tex("3 sided, closed figure").scale(1.3).shift(DOWN*2)
        self.play(Write(text),run_time=0.7)
        self.play(Write(text2),run_time=0.7)
        self.play(Create(Tri),run_time=1.5)
        self.wait(5)

'''How to create a labeled triangle, How to mark angles'''

class label(Scene):
    def construct(self):
        text = Text("Triangle").scale(2.5).to_edge(UP)
        vertices = [
            [-1, +1, 0],
            [+4, -3, 0],
            [-3, -3, 0],
        ]

        triangle = Polygon(*vertices,stroke_color= BLACK, fill_color= BLUE, fill_opacity= 0.75) # how to create polygons using vertices.

        vertexLabelPlacements = [UP, DR, DL]
        vertexLabelNames = ['','','']
        vertexLabels = VGroup(
            *[MathTex(r"{}".format(vertexLabelNames[i])).next_to(vertices[i],vertexLabelPlacements[i]) for i in range(3)] 
        )

        sides = VGroup(
            Line(vertices[0],vertices[1], color=YELLOW),
            Line(vertices[1],vertices[2], color=GREEN),
            Line(vertices[2],vertices[0], color=BLUE),
        )

        sideLabelPlacements = [UR, DOWN, UL]
        sideLabelNames = ['a','b','c']
        sideLabels = VGroup(
            *[Tex(r"{}".format(sideLabelNames[i])).next_to(sides[i].get_center(),sideLabelPlacements[i]) for i in range(3)]
        )

        shortestSide = 1000
        for i in range(3):
            if sides[i].get_length() < shortestSide:
                shortestSide = sides[i].get_length()

        angles = VGroup() 
        for i in range(3):  # Complicated but this is how you put angles in the shapes.. particularly triangles.
            startAngle = np.arctan2(vertices[(i-1)%3][1]-vertices[i][1],vertices[(i-1)%3][0]-vertices[i][0])
            endAngle = np.arctan2(vertices[(i+1)%3][1]-vertices[i][1],vertices[(i+1)%3][0]-vertices[i][0])
            angles += AnnularSector(inner_radius=0, outer_radius=0.2*shortestSide, start_angle=startAngle, angle=endAngle-startAngle,arc_center=vertices[i],color=ORANGE,fill_opacity=1) 

        
        l=Line(start=[-1, +1, 0],end=[+4, -3, 0],color=RED).set_stroke(width=10)
        l2=Line(start=[+4, -3, 0],end=[-3, -3, 0],color=RED).set_stroke(width=10)
        l3=Line(start=[-3, -3, 0],end=[-1, +1, 0],color=PURPLE).set_stroke(width=10)

        l4=Line(start=[-3, -3, 0],end=[-1, +1, 0],color=RED).set_stroke(width=10)       # Creating multiple objects with little variations to facilitate the transitions between them
        l5=Line(start=[-1, +1, 0],end=[+4, -3, 0],color=PURPLE).set_stroke(width=10)
        l6=Line(start=[+4, -3, 0],end=[-3, -3, 0],color=PURPLE).set_stroke(width=10)
        l7=Line(start=[-1, +1, 0],end=[+4, -3, 0],color=RED).set_stroke(width=10)

        t1 = Tex(r"$a-b<c$").to_edge(LEFT,buff=1.5)
        t2 = Tex(r"$b-c<a$").shift(DOWN).to_edge(LEFT,buff=1.5)
        t3 = Tex(r"$c-a<b$").shift(DOWN*2).to_edge(LEFT,buff=1.5)


        # self.play(Write(text))
        self.play(Create(triangle),Create(angles))

        self.add(vertexLabels)
        self.wait(2) 
        self.add(sideLabels)  
        self.wait(2)                  

        self.play(Create(l),Create(l2))
        self.play(Create(l3))
        self.wait(2)
        self.play(Write(t1),Write(t2),Write(t3))
        self.wait(2)
        self.play(Transform(l3, l4),Transform(l,l5),run_time= 1) # Multiple transformations how to create changing colour effect.
        self.wait(2)
        self.play(Transform(l2, l6),Transform(l5,l7))
        self.wait(2)                           

        # self.add(angles)
        # self.wait(2)

'''How to create a line'''

class line(Scene):
    def construct(self):
        l=Line(start=[+4, -2, 0],end=[-3, -2, 0],color=RED)
        l2=Line(start=[+4, -3, 0],end=[-3, -3, 0],color=RED).set_stroke(width=10)
        self.play(Create(l))
        self.play(Create(l2))
        self.wait()

class label2(Scene):
    def construct(self):
        text = Text("Triangle").scale(2.5).to_edge(UP)
        vertices = [
            [-1, +1, 0],
            [+4, -3, 0],
            [-3, -3, 0],
        ]

        triangle = Polygon(*vertices,stroke_color= BLACK, fill_color= ORANGE, fill_opacity= 0.75) # how to create polygons using vertices.

        vertexLabelPlacements = [UP, DR, DL]
        vertexLabelNames = ['','','']
        vertexLabels = VGroup(
            *[MathTex(r"{}".format(vertexLabelNames[i])).next_to(vertices[i],vertexLabelPlacements[i]) for i in range(3)] 
        )

        sides = VGroup(
            Line(vertices[0],vertices[1], color=YELLOW),
            Line(vertices[1],vertices[2], color=GREEN),
            Line(vertices[2],vertices[0], color=BLUE),
        )

        sideLabelPlacements = [UR, DOWN, UL]
        sideLabelNames = ['a','b','c']
        sideLabels = VGroup(
            *[Tex(r"{}".format(sideLabelNames[i])).next_to(sides[i].get_center(),sideLabelPlacements[i]) for i in range(3)]
        )

        shortestSide = 1000
        for i in range(3):
            if sides[i].get_length() < shortestSide:
                shortestSide = sides[i].get_length()

        angles = VGroup() 
        for i in range(3):  # Complicated but this is how you put angles in the shapes.. particularly triangles.
            startAngle = np.arctan2(vertices[(i-1)%3][1]-vertices[i][1],vertices[(i-1)%3][0]-vertices[i][0])
            endAngle = np.arctan2(vertices[(i+1)%3][1]-vertices[i][1],vertices[(i+1)%3][0]-vertices[i][0])
            angles += AnnularSector(inner_radius=0, outer_radius=0.2*shortestSide, start_angle=startAngle, angle=endAngle-startAngle,arc_center=vertices[i],color=BLUE,fill_opacity=1) 

        cc= BLACK
        pp = RED
        l=Line(start=[-1, +1, 0],end=[+4, -3, 0],color=cc).set_stroke(width=10)
        l2=Line(start=[+4, -3, 0],end=[-3, -3, 0],color=cc).set_stroke(width=10)
        l3=Line(start=[-3, -3, 0],end=[-1, +1, 0],color=pp).set_stroke(width=10)

        l4=Line(start=[-3, -3, 0],end=[-1, +1, 0],color=cc).set_stroke(width=10)       # Creating multiple objects with little variations to facilitate the transitions between them
        l5=Line(start=[-1, +1, 0],end=[+4, -3, 0],color=pp).set_stroke(width=10)
        l6=Line(start=[+4, -3, 0],end=[-3, -3, 0],color=pp).set_stroke(width=10)
        l7=Line(start=[-1, +1, 0],end=[+4, -3, 0],color=cc).set_stroke(width=10)

        t1 = Tex(r"$\left| a-b \right|<c$").to_edge(LEFT,buff=1.5)
        t2 = Tex(r"$\left|b-c\right|<a$").shift(DOWN).to_edge(LEFT,buff=1.5)
        t3 = Tex(r"$\left|c-a\right|<b$").shift(DOWN*2).to_edge(LEFT,buff=1.5)


        # self.play(Write(text))
        self.play(Create(triangle),Create(angles))

        self.add(vertexLabels)
        self.wait(2) 
        self.add(sideLabels)  
        self.wait(2)                  

        self.play(Create(l),Create(l2))
        self.play(Create(l3))
        self.wait(2)
        self.play(Write(t1),Write(t2),Write(t3))
        self.wait(2)
        self.play(Transform(l3, l4),Transform(l,l5),run_time= 1) # Multiple transformations how to create changing colour effect.
        self.wait(2)
        self.play(Transform(l2, l6),Transform(l5,l7))
        self.wait(2)

'''How to make moving equations'''

class ex(Scene):
    def construct(self):
        t1 = MathTex(r"{1",r"\over",r"3}",r"(3.14)",r"(2.312)^2",r"H =",r"18.0469").shift(UP*1.2)  # Write all the equations in different lines.. differentiated by comma. 
        tt = t1.copy()                                                                             # you can copy the same thing.. using .copy() you can use it as a different object while it is the same one.
        t2 = MathTex(r"(3.14)",r"(2.312)^2",r"H =",r"{",r"3",r"\times",r"18.0469",r"\over 1}")     # Use \\over instead of \\frac as it is more considerable. 
        t3 = MathTex(r"(2.312)^2",r"H =",r"{",r"3",r"\times",r"18.0469",r"\over",r"(3.14)",r"}")
        t4 = MathTex(r"H =",r"{",r"3",r"\times",r"18.0469",r"\over",r"(3.14)",r"(2.312)^2",r"}")   # Divide the equation in multiple structures.. to be able to facilitate.. the small actions visibly.
        tt2 = t4.copy()
        t5 = MathTex(r"H =",r"3.224" r"\hspace{1mm}" r"in").shift(DOWN*1.2)         #MathTex is the best for writing equations.
        self.play(Write(t1))
        self.add(tt)
        self.play(TransformMatchingTex(t1,t2),run_time=1)   #Use TransformMatchingTex to move equations with the same text.. which look real.
        self.play(TransformMatchingTex(t2,t3),run_time=1)
        self.play(TransformMatchingTex(t3,t4),run_time=1)
        self.wait(2)
        self.add(tt2)
        self.play(TransformMatchingTex(t4,t5),tun_time=1)
        self.wait()


