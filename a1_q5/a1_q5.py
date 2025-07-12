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
    node_counter = 0
    
    if strategy == 'B':
        discovered = deque([(start_node, [start_node], 0, 0)])
    elif strategy == 'D':
        discovered = deque([(start_node, [start_node], 0, 0)])
    else:
        discovered = []
        if strategy == 'G':
            priority = h_function(start_node)
            heapq.heappush(discovered, (priority, node_counter, (start_node, [start_node], 0, 0)))
            node_counter += 1
        else: # strategy = A*
            priority = 0 + h_function(start_node)
            heapq.heappush(discovered, (priority, node_counter, (start_node, [start_node], 0, 0)))
            node_counter += 1

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
    
        neighbors = []
        for neighbor_node in range(n):
            if G[current_node][neighbor_node] is not None:
                edge_cost = G[current_node][neighbor_node]
                new_g_cost = g_cost + edge_cost
                new_depth = depth + 1
                new_path = path + [neighbor_node]
                
                if neighbor_node not in explored:
                    neighbors.append((neighbor_node, new_path, new_g_cost, new_depth))
        
        # Add neighbors to frontier based on strategy
        for neighbor_node, new_path, new_g_cost, new_depth in neighbors:
            if strategy == 'B':  # BFS
                discovered.append((neighbor_node, new_path, new_g_cost, new_depth))
            elif strategy == 'D':  # DFS
                discovered.append((neighbor_node, new_path, new_g_cost, new_depth))
            elif strategy == 'G':  # Greedy
                priority = h_function(neighbor_node)
                node_counter += 1
                heapq.heappush(discovered, (priority, node_counter, (neighbor_node, new_path, new_g_cost, new_depth)))
            else:  # A*
                priority = new_g_cost + h_function(neighbor_node)  # g + h
                node_counter += 1
                heapq.heappush(discovered, (priority, node_counter, (neighbor_node, new_path, new_g_cost, new_depth)))
    
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
    path = graph_search(graph, heuristic_func, start_state, goal_state, search_strategy)
    if path is not None:
        path = str([state + 1 for state in path])
    print(path)

