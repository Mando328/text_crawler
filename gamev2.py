import os
from random import randint, choice
from sys import platform
import msvcrt
class Mapgrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []
        self.quiz = []
        self.start = (0, 0)
        self.goal = (width-1, height-1)
        self.player = (0, 0)

def move_player(graph, direction): # funkcja przesuwa gracza w zadanym kierunku, jeśli nie ma ściany    
    x, y = graph.player
    if direction == 'w':
        new_pos = (x, y-1)
    elif direction == 's':
        new_pos = (x, y+1)
    elif direction == 'a':
        new_pos = (x-1, y)
    elif direction == 'd':
        new_pos = (x+1, y)
    else:
        return  # nieznany kierunek

    if (0 <= new_pos[0] < graph.width and
        0 <= new_pos[1] < graph.height and
        new_pos not in graph.walls):
        graph.player = new_pos
    
def draw_map(graph, width = 3): # funkcja rysuje matrycę mapy
    for y in range(graph.height):
        for x in range(graph.width):
            if (x, y) in graph.walls:
                print("%%-%ds" % width % '#', end="")
            elif (x, y) == graph.player:
                print("%%-%ds" % width % '$', end="")
            elif (x, y) == graph.goal:
                print("%%-%ds" % width % '!', end="")
            else:
                print("%%-%ds" % width % '.', end="")
        print()

def setup_quiz(graph, pct=1 ):
    out = []
    for i in range(int(graph.height*pct)):
        x = 0
        y = randint(0, graph.height - 1)
        out.append((x, y))
    for i in range(int(graph.height*pct)):
        x = graph.width-1
        y = randint(0, graph.height - 1)
        out.append((x, y))
    for i in range(int(graph.width*pct)):
        y = 0
        x = randint(0, graph.width - 1)
        out.append((x, y))
    for i in range(int(graph.width*pct)):
        y = graph.height-1
        x = randint(0, graph.width - 1)
        out.append((x, y))
    return out
            
def setup_walls(graph, pct= 0.3): # funkcja losowo generuje ściany na mapie, przyjmuje procent zajętości mapy
    out = []
    for i in range(int(graph.height * graph.width*pct//2)):
            x = randint(1, graph.width-1)
            y = randint(1, graph.height-2)

            out.append((x, y))
            out.append((x + choice([-1, 0, 1]), y + choice([-1, 0, 1])))
    return out

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    g = Mapgrid(15, 10)
    g.walls = setup_walls(g)
    g.quiz = setup_quiz(g)
    draw_map(g)
    
    while g.player != g.goal:
        print("Move (w/a/s/d): ", end="", flush=True)
        move = msvcrt.getch().decode('utf-8').lower()
        print(move)  # Display the key pressed
        move_player(g, move)
        clear()
        draw_map(g)
    if g.player == g.goal:
        print("Congratulations! You've reached the goal!")


if __name__ == '__main__':
    main()


