import sys
import csv
import heapq
from collections import deque


def graph_search(G, h_function, start_node, goal_node, strategy):
    """
    You are free to implement this however you like but you will most likely need to input the graph data structure G, the heuristic function h, the start state s, the goal state t, and the search strategy X  
    """
    n = len(G) #number of nodes
    explored = set()
    discovered = []

    
    if strategy == 'B':
        discovered = deque([(start_node, [start_node], 0, 0)])
    elif strategy == 'D':
        discovered = deque([(start_node, [start_node], 0, 0)])
    else:
        counter = 0
        if strategy == 'G':
            priority = h_function(start_node)
        else: # strategy = A*
            priority = 0 + h_function(start_node)
    
    while discovered:
        if strategy == 'B':  # BFS - FIFO
            current_node, path, g_cost, depth = discovered.popleft()
        elif strategy == 'D':  # DFS - LIFO
            current_node, path, g_cost, depth = discovered.pop()
        else:  # Greedy or A* - priority queue
            if not discovered:
                break
            _, _, (current_node, path, g_cost, depth) = heapq.heappop(discovered)
   
        if current_node == goal_node:
            return path
    
        if current_node in explored:
            continue
        explored.add(current_node)
    
   
    return None


# ---- INCLUDE ANY OTHER CODE THAT YOU NEED HERE ----


if __name__ == "__main__":

    # get parameters from command line. We need -1 for our vertex numbers since our indexing starts at 0 in python
    start_state = int(sys.argv[1]) - 1
    goal_state = int(sys.argv[2]) - 1
    search_strategy = sys.argv[3]
    graph_csv = sys.argv[4]
    heuristic_csv = sys.argv[5]

    # get the graph
    graph = []
    with open(graph_csv, "r", encoding='utf-8-sig') as csvfile:
        reader_variable = csv.reader(csvfile, delimiter=",")
        for row in reader_variable:
            row_as_ints = [int(val) if val != '' else None for val in row]
            graph.append(row_as_ints)

    # get the heuristic matrix
    heuristic = []
    with open(heuristic_csv, "r", encoding='utf-8-sig') as csvfile:
        reader_variable = csv.reader(csvfile, delimiter=",")
        for row in reader_variable:
            heuristic_row = [float(val) if val != '' else None for val in row]
            heuristic.append(heuristic_row)

    # once we have the goal we can create the heuristic function using the matrix
    heuristic_func = lambda n: heuristic[n][goal_state]        
            
    # find and print the path. The vertices are numbered as they appear in the original graph. Add whatever inputs you need to your graph search function
    path = graph_search()
    if path is not None:
        path = str([state + 1 for state in path])
    print(path)

