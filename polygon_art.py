import turtle
import random

# def draw_polygon(num_sides, size, orientation, location, color, border_size):
#     turtle.penup()
#     turtle.goto(location[0], location[1])
#     turtle.setheading(orientation)
#     turtle.color(color)
#     turtle.pensize(border_size)
#     turtle.pendown()
#     for _ in range(num_sides):
#         turtle.forward(size)
#         turtle.left(360/num_sides)
#     turtle.penup()

# def get_new_color():
#     return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))



# # draw a polygon at a random location, orientation, color, and border line thickness
# num_sides = random.randint(3, 5) # triangle, square, or pentagon
# size = random.randint(50, 150)
# orientation = random.randint(0, 90)
# location = [random.randint(-300, 300), random.randint(-200, 200)]
# color = get_new_color()
# border_size = random.randint(1, 10)
# draw_polygon(num_sides, size, orientation, location, color, border_size)

# # specify a reduction ratio to draw a smaller polygon inside the one above
# reduction_ratio = 0.618

# # reposition the turtle and get a new location
# turtle.penup()
# turtle.forward(size*(1-reduction_ratio)/2)
# turtle.left(90)
# turtle.forward(size*(1-reduction_ratio)/2)
# turtle.right(90)
# location[0] = turtle.pos()[0]
# location[1] = turtle.pos()[1]

# # adjust the size according to the reduction ratio
# size *= reduction_ratio

# # draw the second polygon embedded inside the original 
# draw_polygon(num_sides, size, orientation, location, color, border_size)

# # hold the window; close it by clicking the window close 'x' mark
# turtle.done()


class Polygon:
    def __init__(self, num_sides, size, orientation, location, color, border_size) -> None:
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size

    def move(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])

    def draw_polygon(self):
        self.move()
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360/self.num_sides)
        turtle.penup()


class EmbeddedPolygon(Polygon):

    def __init__(self, num_sides, size, orientation, location, color, border_size, num_levels, ratio=0.618) -> None:
        super().__init__(num_sides, size, orientation, location, color, border_size)
    
        self.num_levels = num_levels
        self.ratio = ratio

    def draw_polygon(self):
        super().draw_polygon()
        # reposition the turtle and get a new location
        for _ in range(self.num_levels):
            turtle.penup()
            turtle.forward(self.size*(1-self.ratio)/2)
            turtle.left(90)
            turtle.forward(self.size*(1-self.ratio)/2)
            turtle.right(90)
            self.location[0] = turtle.pos()[0]
            self.location[1] = turtle.pos()[1]
            self.size *= self.ratio
            super().draw_polygon()


class Run:
    def __init__(self) -> None:
        self.choice = None

    def ask(self):
        ch = input("Which art do you want to generate? Enter a number between 1 to 9 \ninclusive: ")
        self.choice = ch


    def get_new_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    def run(self):

        num_polygons = random.randint(1,50)
        if self.choice in ['1', '5']:
            """Draw Triangle"""
            num_sides = 3
        elif self.choice in ['2', '6']:
            """Draw regtangle"""
            num_sides = 4
        elif self.choice in ['3', '7']:
            """Draw pentagon"""
            num_sides = 5

        for _ in range(num_polygons):
            if self.choice in ['4', '8', '9']:
                """Draw random"""
                num_sides = random.randint(3,5)
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = self.get_new_color()
            border_size = random.randint(1, 10)
            if self.choice in ['1','2','3','4']:
                p = Polygon(num_sides, size, orientation, location, color, border_size)
                p.draw_polygon()
            elif self.choice in ['5','6','7','8']:
                emb_p = EmbeddedPolygon(num_sides, size, orientation, location, color, border_size, 3)
                emb_p.draw_polygon()
            elif self.choice == '9':
                flag = random.randint(1,2)
                if flag == 1:
                    p = Polygon(num_sides, size, orientation, location, color, border_size)
                    p.draw_polygon()
                else:
                    emb_p = EmbeddedPolygon(num_sides, size, orientation, location, color, border_size, 3)
                    emb_p.draw_polygon()
        turtle.done()





turtle.speed(10)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)
r = Run()
r.ask()
r.run()


