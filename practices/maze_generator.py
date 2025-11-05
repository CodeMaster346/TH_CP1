#TH 2nd Maze Generator Program
import turtle
import random

# ==== CONFIG ====
CELL_SIZE = 15 # Size of each maze cell
WALL_COLOR = "black"
PATH_COLOR = "white"
PLAYER_COLOR = "blue"

def generate_maze(size):
    maze = [[1 for _ in range(size)] for _ in range(size)]

    def carve(x, y):
        dirs = [(2,0), (-2,0), (0,2), (0,-2)]
        random.shuffle(dirs)
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < size and 0 <= ny < size and maze[ny][nx] == 1:
                maze[ny - dy//2][nx - dx//2] = 0
                maze[ny][nx] = 0
                carve(nx, ny)

    maze[1][1] = 0
    carve(1,1)
    maze[0][1] = 0
    maze[size-1][size-2] = 0
    return maze

def draw_maze(maze, size):
    turtle.tracer(0, 0)
    turtle.penup()
    turtle.goto(-size*CELL_SIZE/2, size*CELL_SIZE/2)
    turtle.pendown()
    turtle.hideturtle()
    for y in range(size):
        for x in range(size):
            screen_x = -size*CELL_SIZE/2 + x*CELL_SIZE
            screen_y = size*CELL_SIZE/2 - y*CELL_SIZE
            if maze[y][x] == 1:
                draw_square(screen_x, screen_y, WALL_COLOR)
            else:
                draw_square(screen_x, screen_y, PATH_COLOR)

def draw_square(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(CELL_SIZE)
        turtle.right(90)
    turtle.end_fill()

def main():
    turtle.setup(width=800, height=800)
    turtle.title("Turtle Maze Game")
    size = int(turtle.numinput("Maze Complexity", "Enter maze size (10–50, must be an even number or maze wont generate properly):"))
    size += 1

    if size < 11 or size > 51:
        print("Invalid Number")

    maze = generate_maze(size)
    draw_maze(maze, size)

    turtle.mainloop()

if __name__ == "__main__":
    main()