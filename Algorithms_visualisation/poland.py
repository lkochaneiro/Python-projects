import turtle

"""Here are methods which do all things with drawing."""

polska = [(80, 100, 'Z'), (180, 50, 'G'), (330, 80, 'N'), (420, 130, 'B'),
          (60, 200, 'F'), (140, 200, 'P'), (200, 140, 'C'), (260, 260, 'E'),
          (340, 200, 'W'), (430, 290, 'L'), (110, 300, 'D'), (180, 330, 'O'),
          (240, 350, 'S'), (320, 320, 'T'), (300, 400, 'K'), (400, 380, 'R')]

slownik = {rej: (x, y, rej) for x, y, rej in polska}

# Reprezentacja krawędzi wraz z wagami (w obie strony)
graf = [('Z', 'G', 359), ('Z', 'P', 263), ('Z', 'F', 213),
        ('G', 'Z', 359), ('G', 'P', 322), ('G', 'C', 174), ('G', 'N', 166),
        ('N', 'G', 166), ('N', 'C', 216), ('N', 'W', 215), ('N', 'B', 224),
        ('B', 'N', 224), ('B', 'W', 199), ('B', 'L', 247),
        ('F', 'Z', 213), ('F', 'P', 151), ('F', 'D', 186),
        ('P', 'F', 151), ('P', 'Z', 263), ('P', 'G', 322), ('P', 'C', 139),
        ('P', 'E', 218), ('P', 'O', 284), ('P', 'D', 180),
        ('C', 'P', 139), ('C', 'G', 174), ('C', 'N', 216), ('C', 'W', 310), ('C', 'E', 229),
        ('E', 'P', 218), ('E', 'C', 229), ('E', 'W', 186), ('E', 'T', 153), ('E', 'S', 203), ('E', 'O', 205),
        ('W', 'C', 310), ('W', 'N', 215), ('W', 'B', 199), ('W', 'L', 178), ('W', 'T', 177), ('W', 'E', 186),
        ('L', 'W', 178), ('L', 'B', 247), ('L', 'R', 178), ('L', 'T', 176),
        ('D', 'F', 186), ('D', 'P', 180), ('D', 'O', 98),
        ('O', 'D', 98), ('O', 'P', 284), ('O', 'E', 205), ('O', 'S', 106),
        ('S', 'O', 106), ('S', 'E', 203), ('S', 'T', 154), ('S', 'K', 80),
        ('T', 'S', 154), ('T', 'E', 153), ('T', 'W', 177), ('T', 'L', 176), ('T', 'R', 155), ('T', 'K', 114),
        ('K', 'S', 80), ('K', 'T', 114), ('K', 'R', 168),
        ('R', 'K', 168), ('R', 'T', 155), ('R', 'L', 178)]


def coords(x, y):
    y = 470 - y
    dx = -250
    dy = -235
    return x + dx, y + dy


# Funkcja rysująca liczby (koszt między krawędziami)
def draw_edge_weight(v_start, v_end, number):
    x1, y1, _ = slownik[v_start]
    x2, y2, _ = slownik[v_end]

    final_x = (x1 + x2 - 500) // 2
    final_y = (235-y1 + 235-y2) // 2

    turtle.goto(final_x, final_y)
    turtle.penup()
    turtle.write(number, font=("Verdana", 9, "bold"))
    turtle.pendown()


def draw_circle(x, y, letter):
    x, y = coords(x, y)
    turtle.penup()
    turtle.goto(x, y - 20)
    turtle.pendown()
    turtle.circle(20)
    turtle.write(letter, font=("Verdana", 18, "bold"))
    turtle.penup()


def draw_line(edge, color=None):
    x, y, _ = slownik[edge[0]]
    x, y = coords(x, y)

    if color is not None:
        turtle.pensize(3)
        turtle.color(color)

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    x, y, _ = slownik[edge[1]]
    x, y = coords(x, y)
    turtle.goto(x, y)
    turtle.penup()


def draw_method_and_time(method, time, cost):
    turtle.color('black')
    turtle.penup()
    turtle.goto(-240, -175)
    turtle.write(f'Method: {method}', font=("Verdana", 10, "bold"))
    turtle.pendown()

    turtle.penup()
    turtle.goto(-240, -195)
    turtle.write(f'Total cost of MST: {cost}', font=("Verdana", 10, "bold"))
    turtle.pendown()

    turtle.penup()
    turtle.goto(-240, -215)
    turtle.write(f'Method time: {time}', font=("Verdana", 10, "bold"))
    turtle.pendown()


def draw_map(edges, lines_col=None, mst_edges=None, mst_info=None, col=None):
    # edges - lista krawędzi które mamy połączyć
    # lines_col - kolor linii do zaznaczenia MST
    # mst_edges - krawędzi tworzące MST
    # mst_info - lista trzech informacji [nazwa algorytmu, czas działania, koszt (wagi wierzchołków)]

    wn = turtle.Screen()
    wn.setup(width=500, height=470, startx=10, starty=10)
    wn.title("Polska")
    wn.tracer(1, delay=6)

    wn.addshape("polska.gif")

    myImage = turtle.Turtle()
    myImage.speed(0)
    myImage.shape("polska.gif")
    myImage.penup()
    myImage.goto(0, 0)
    turtle.speed(0)
    turtle.penup()

    if col is None:
        for x, y, r in polska:
            draw_circle(x, y, r)
    else:
        for k, c in col:
            x, y, _ = slownik[k]
            draw_circle(x, y, c)

    if mst_edges:
        if lines_col is not None:
            for _, e in enumerate(edges):
                draw_line(e)

                v_start, v_end, number = e
                draw_edge_weight(v_start, v_end, number)
            for _, e1 in enumerate(mst_edges):
                draw_line(e1, lines_col)

            draw_method_and_time(mst_info[0], mst_info[1], mst_info[2])
            turtle.hideturtle()
    else:
        for i, e in enumerate(edges):
            draw_line(e)
        turtle.hideturtle()

    wn.update()
    wn.mainloop()


if __name__ == "__main__":
    draw_map(graf)