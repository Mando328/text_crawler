import os
import time
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
        self.barrier = []

class Question:
    def _init_(self,number):
        self.lines = []
        self.number=number
        self.anwsers=[]
        self.number=0
        self.odpowiedzi=[]
        self.poprawna=0
def read_file():
    with open("PYTANIA.txt", "r",encoding="utf-8") as file:
        lines = file.readlines()
        lines = [i.strip() for i in lines]
        return lines
def set_anwsers(n,lines=read_file()):
    q=lines[n*5]
    o=[]
    p = lines[n*5+1]
    for i in lines[n*5+2:n*5+5]:
        o.append(i)
    return q,p,o

def setup_barrier(graph):
        out=[]
        x=0
        for i in range(0,graph.height):
            out.append((x,i))
        x=graph.width-1
        for i in range(0,graph.height):
            out.append((x,i))
        y=0
        for i in range(0,graph.width):
            out.append((i,y))
        y=graph.height-1
        for i in range(0,graph.width):
            out.append((i,y))
        return out

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
        new_pos not in graph.walls and new_pos not in graph.quiz):
        graph.player = new_pos 
    elif new_pos in graph.quiz:
        q,p,o=set_anwsers(randint(0,75))
        print(q)
        for i in o:
            print(i)
        a=input()
        if a == p:
            print("Gratulacje, prawidłowa odpowiedź!")
            time.sleep(1)
            graph.player = new_pos
        else:
            print("To zła odpowiedź, nie przechodzisz dalej :(")
            time.sleep(1)
        
    
def draw_map(graph, width = 3): # funkcja rysuje matrycę mapy
    for y in range(graph.height):
        for x in range(graph.width):
            if (x, y) in graph.walls:
                print("%%-%ds" % width % '#', end="")
            elif (x, y) == graph.player:
                print("%%-%ds" % width % '$', end="")
            elif (x, y) == graph.goal:
                print("%%-%ds" % width % '!', end="")
            elif (x, y) in graph.quiz:
                print("%%-%ds" % width % '?', end="")
            else:
                print("%%-%ds" % width % '.', end="")
        print()

def setup_quiz(graph, pct=0.4 ):
    out = []
    for i in range(int(2* graph.height + 2*(graph.width-2)*pct)):
        (x,y) = choice(graph.barrier)
        out.append((x,y))
    return out
            
def setup_walls(graph, pct= 0.4): # funkcja losowo generuje ściany na mapie, przyjmuje procent zajętości mapy
    out = []
    for i in range(int(graph.height * graph.width*pct//2)):
            x = randint(1, graph.width-2)
            if  graph.width-3 <= x <= graph.width-2:
                y = randint(1, graph.height-3)
            else:
                y = randint(1, graph.height-2)
            out.append((x, y))
            out.append((x + choice([-1, 0, 1]), y + choice([-1, 0, 1])))
    for i in out:
        if i in graph.barrier:
            out.remove(i)
    return out

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
            
def main():
    
    g = Mapgrid(15, 10)
    g.barrier = setup_barrier(g)
    g.walls = setup_walls(g)
    g.quiz = setup_quiz(g)
    
    
    draw_map(g)
    
    while g.player != g.goal and True:
        print("Move (w/a/s/d): ", end="", flush=True)
        move = input()
        move_player(g, move)
        clear()
        draw_map(g)
        if move == "r":
            break
    if g.player == g.goal:
        print("Congratulations! You've reached the goal!")
    
    
if __name__ == '__main__':
    main()


