import turtle
import random

# ==== CONFIG ====
CELL_SIZE = 15 # Size of each maze cell
WALL_COLOR = "black"
PATH_COLOR = "white"
PLAYER_COLOR = "blue"

# ==== MAZE GENERATION ====
def generate_maze(size):
    # Initialize all walls as True
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

    # Start carving from (1,1)
    maze[1][1] = 0
    carve(1,1)
    # Add start and end openings
    maze[0][1] = 0
    maze[size-1][size-2] = 0
    return maze

# ==== DRAW MAZE ====
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

# ==== PLAYER ====
class Player:
    def __init__(self, maze, size):
        self.maze = maze
        self.size = size
        self.x, self.y = 1, 0 # Start at the opening
        self.t = turtle.Turtle()
        self.t.shape("circle")
        self.t.color(PLAYER_COLOR)
        self.t.penup()
        self.update_position()

    def update_position(self):
        screen_x = -self.size*CELL_SIZE/2 + self.x*CELL_SIZE + CELL_SIZE/2
        screen_y = self.size*CELL_SIZE/2 - self.y*CELL_SIZE - CELL_SIZE/2
        self.t.goto(screen_x, screen_y)

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy
        if 0 <= new_x < self.size and 0 <= new_y < self.size:
            if self.maze[new_y][new_x] == 0:
                self.x, self.y = new_x, new_y
                self.update_position()
                # Check if reached goal
                if self.y == self.size-1 and self.x == self.size-2:
                    print("You Win!")
                    turtle.bye()
            else:
                print("Game Over!")
                turtle.bye()

# ==== MAIN ====
def main():
    turtle.setup(width=800, height=800)
    turtle.title("Turtle Maze Game")
    size = int(turtle.numinput("Maze Complexity", "Enter maze size (e.g. 10–50):", 20, minval=5, maxval=50))

    if size < 10 or size > 50:
        print("Invalid Number")

    maze = generate_maze(size)
    draw_maze(maze, size)

    player = Player(maze, size)

    # Keyboard bindings
    turtle.listen()
    turtle.onkeypress(lambda: player.move(0, -1), "Down")
    turtle.onkeypress(lambda: player.move(0, 1), "Up")
    turtle.onkeypress(lambda: player.move(-1, 0), "Left")
    turtle.onkeypress(lambda: player.move(1, 0), "Right")

    turtle.done()

if __name__ == "__main__":
    main()