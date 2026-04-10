import os
import time
from random import randint, choice, sample
from sys import platform
import msvcrt
BASE_DIR = os.path.dirname(os.path.abspath(__file__))   #kod z ai żeby upewnić się że będzie działać na każdym komputerze, niezależnie od systemu operacyjnego i odpalało się z każdego katalogu, a nie tylko z tego, w którym znajduje się plik .py
QUESTIONS_FILE = os.path.join(BASE_DIR, "PYTANIA.txt") 
points = 0
class Mapgrid:  #szymon
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []
        self.quiz = []
        self.start = (0, 0)
        self.goal = (width-1, height-1)
        self.player = (0, 0)
        self.barrier = []

def read_file(): #emilka
    with open(QUESTIONS_FILE, "r", encoding="utf-8") as file:
        lines = file.readlines()
        lines = [i.strip() for i in lines]
    return lines

def set_anwsers(n, lines=None): #emilka
    if lines is None:
        lines = read_file()
    q=lines[n*5]
    o=[]
    p = lines[n*5+1]
    for i in lines[n*5+2:n*5+5]:
        o.append(i)
    return q,p,o

        
def setup_barrier(graph):   #emilka
        out=[]
        x=0
        for i in range(1,graph.height - 1):
            out.append((x,i))
        x=graph.width-1
        for i in range(1,graph.height - 1):
            out.append((x,i))
        y=0
        for i in range(1,graph.width - 1):
            out.append((i,y))
        y=graph.height-1
        for i in range(1,graph.width - 1):
            out.append((i,y))
        return out

def move_player(graph, direction, pkt=points): #szymon  
    pkt=int(pkt)
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

    if (0 <= new_pos[0] < graph.width and #wywoływane pytania robiła emilka
        0 <= new_pos[1] < graph.height and
         new_pos not in graph.walls and new_pos not in graph.quiz):
        graph.player = new_pos 
    elif new_pos in graph.quiz:
        q,p,o=set_anwsers(randint(0,73))
        print(q)
        for i in o:
            print(i)
        a=input()
        if a == p:
            print("Gratulacje, prawidłowa odpowiedź!")
            pkt = pkt + 100
            time.sleep(1)
            while new_pos in graph.quiz:
                graph.quiz.remove(new_pos)
            graph.player = new_pos
        else:
            print("To zła odpowiedź, nie przechodzisz dalej :(")
            pkt = pkt - 50
            time.sleep(1)
    return pkt
    
def draw_map(graph, width = 3): #szymon
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

def setup_quiz(graph, pct=0.4 ):    #emilka
    out = []
    for i in range(int(2* graph.height + 2*(graph.width-2)*pct)):
        (x,y) = choice(graph.barrier)
        out.append((x,y))
    return out
            
def setup_walls(graph, pct= 0.4): #szymon
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

def clear():    #szymon, kod z internetu
    os.system('cls' if os.name == 'nt' else 'clear')

def start_menu():   #szymon
    print("""╔╗─╔╦═══╦╗──╔╗──╔═══╗╔╗
║║─║║╔══╣║──║║──║╔═╗║║║
║╚═╝║╚══╣║──║║──║║─║║║║
║╔═╗║╔══╣║─╔╣║─╔╣║─║║╚╝
║║─║║╚══╣╚═╝║╚═╝║╚═╝║╔╗
╚╝─╚╩═══╩═══╩═══╩═══╝╚╝""")
    print("Use W/A/S/D to move up/left/down/right.")
    print("Answer quizzes '?' to earn points, but beware of wrong answers!")
    print("Reach the goal '!' while avoiding walls '#' and answering quizzes '?'.")
    print("Press 'R' to reset the game at any time.")
    input("Press Enter to start...")
    clear()
           
def main(): #szymon
    points = 0
    g = Mapgrid(15, 10)
    g.barrier = setup_barrier(g)
    g.walls = setup_walls(g)
    g.quiz = setup_quiz(g)
    clear()
    start_menu()
    draw_map(g)
    
    while g.player != g.goal and True: #warunek sprawdza koniec gry i szczytuje klawisz, który gracz wcisnął, żeby poruszyć się po planszy
        print("Move (w/a/s/d): ", end="", flush=True)
        move = msvcrt.getch().decode('utf-8').lower()
        print(move)  # Display the key pressed
        points = move_player(g, move, points)
        clear()
        draw_map(g)
        if move == "r":
            clear()
            print("The end")          
            time.sleep(2)       
            clear()
            break
    if g.player == g.goal:
        print("Congratulations! You've reached the goal!")
        print(f"Final Score: {points}")
        time.sleep(5)
    

if __name__ == '__main__': #szymon
    main()


