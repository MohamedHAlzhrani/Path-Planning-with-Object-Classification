import pandas as pd 
import numpy as np
from vgg import *
import math as m



class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0
        self.h2 = 0
        self.f2 = 0


    def __eq__(self, other):
        return self.position == other.position



def astar(maze, start, end,type):#when a type be M that mean MANHATTAN , or when E that mean straight line
    


    # Create start and end node
    start_node = Node(None,start)
    start_node.g = start_node.h = start_node.h2 = start_node.f = start_node.f2 = 0
    end_node = Node(None,end)
    end_node.g = end_node.h = end_node.h2= end_node.f = end_node.f2 = 0


    # Initialize both open and closed list
    open_list = []
    closed_list = []
    
    # Add the start node
    open_list.append(start_node)
    
    # Loop until you find the end
    while len(open_list) > 0:  
        if type =='M':
            # Get the current node
            current_node = open_list[0]
            current_index = 0
            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index
        elif type =='E': #E that mean straight line
            # Get the current node
            current_node = open_list[0]
            current_index = 0
            for index, item in enumerate(open_list):
                if item.f2 < current_node.f2:
                    current_node = item
                    current_index = index
        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)
        

        # Found the goal
        if current_node == end_node:
            path = []
            cost=current_node.g
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return spece, cost, closed_list, path[::-1] # Return reversed pat
        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])


      
            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue
            if Node(current_node, node_position) in closed_list:
                continue          
             # Make sure walkable terrai
            if  (maze[node_position[0]][node_position[1]] !='P') and(maze[node_position[0]][node_position[1]] != 'G') and(maze[node_position[0]][node_position[1]] == 'W'):
                continue
            if (maze[node_position[0]][node_position[1]] =='A') or (maze[node_position[0]][node_position[1]] == 'B') or (maze[node_position[0]][node_position[1]] =='C') or (maze[node_position[0]][node_position[1]] == 'D')or (maze[node_position[0]][node_position[1]] =='E') or (maze[node_position[0]][node_position[1]] == 'F') or (maze[node_position[0]][node_position[1]] =='H') or (maze[node_position[0]][node_position[1]] == 'I')or (maze[node_position[0]][node_position[1]] =='J') or (maze[node_position[0]][node_position[1]] == 'K') or  (maze[node_position[0]][node_position[1]] =='L') or (maze[node_position[0]][node_position[1]] == 'M')or  (maze[node_position[0]][node_position[1]] =='N') or (maze[node_position[0]][node_position[1]] == 'O') or  (maze[node_position[0]][node_position[1]] =='Q') or (maze[node_position[0]][node_position[1]] == 'R') or (maze[node_position[0]][node_position[1]] == 'T')or (maze[node_position[0]][node_position[1]] =='U') or (maze[node_position[0]][node_position[1]] == 'V') or (maze[node_position[0]][node_position[1]] =='X') or (maze[node_position[0]][node_position[1]] == 'Y')or  (maze[node_position[0]][node_position[1]] =='Z'):                    
                
                p=sc(rec(maze[node_position[0]][node_position[1]]))
                
                if p<=397:
                 continue
                     
            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    break
                else:
                    # Create the f, g, and h values
                    child.g = current_node.g + 1                                                      
                    child.h =abs ((child.position[0] - end_node.position[0])) + abs ((child.position[1] - end_node.position[1])) 
                    child.f = child.g + child.h
                    child.h2 = m.sqrt((child.position[0] - end_node.position[0]) **2 + (child.position[1] - end_node.position[1]) **2)
                    child.f2 = child.g + child.h2

            # Child is already in the open list
                    for open_node in open_list:
                        if child == open_node and child.g >= open_node.g:
                           break
                    else:
                    # Add the child to the open list
                        spece=len(open_list)
                        open_list.append(child)
                        if len(open_list)>spece:
                            spece=len(open_list)
#get the xy of start node S and end node G
def fstartAndEnd(maze):
    for i in range(len(maze)):
        for j in range(len(maze)):
            if maze[i][j] == 'S':
                start=(i,j)
            if maze[i][j] == 'G':
                    end=(i,j)
            


    return start,end

    
def main():

    data1 = pd.read_csv("maze10x10.txt", sep=" ", header=None)
    data2 = pd.read_csv("maze50x50.txt", sep=" ", header=None)
    data3 = pd.read_csv("maze100x100.txt", sep=" ", header=None)
   
    array = np.array(data1).reshape(data1.shape)
    array5 = np.array(data2).reshape(data2.shape)
    array00 = np.array(data3).reshape(data3.shape)
   

    maze = array
    maze1 = array5       
    maze2 = array00
    
    start , end = fstartAndEnd(maze)
    start1 , end1 = fstartAndEnd(maze1)
    start2 , end2 = fstartAndEnd(maze2)
    spece,cost,closelist, path = astar(maze, start, end,'M')
    print(array)
    print("_______________________________________________________10X10____________________________________________________________________________")
    print("The Manhattan distance")
    print(" M--->",path)
    print(" cost of path of (M) = ",cost)
    print(" Time complixty of 'M' ",len(closelist))
    print("spece complixty of 'M' :",spece)
    print("_____________________________________________________________________________________________________________________________________________________________")
    spece,cost,closelist, path = astar(maze, start, end,'E')
    print("The straight line distance")
    print(" E--->",path)
    print(" cost of path of  'E' = ",cost)
    print(" Time complixty 'E' ",len(closelist))
    print("spece complixty 'E' :",spece)
    ##########################################################################################################################################################
    print("_______________________________________________________50X50_________________________________________________________________________________________________")
    print(array5)
    spece,cost,closelist, path = astar(maze1, start1, end1,'M')
    print("The Manhattan distance")
    print(" M--->",path)
    print(" cost of path of (M) = ",cost)
    print(" Time complixty of 'M' ",len(closelist))
    print("spece complixty of 'M' :",spece)
    print("_____________________________________________________________________________________________________________________________________________________________")
    spece,cost,closelist, path = astar(maze1, start1, end1,'E')
    print("The straight line distance")
    print(" E--->",path)
    print(" cost of path of  'E' = ",cost)
    print(" Time complixty 'E' ",len(closelist))
    print("spece complixty 'E' :",spece)
##########################################################################################################################################################

    print("_______________________________________________________100X100________________________________________________________________________________________________")
    print(array00)
    spece,cost,closelist, path = astar(maze2, start2, end2,'M')
    print("The Manhattan distance")
    print(" M--->",path)
    print(" cost of path of (M) = ",cost)
    print(" Time complixty of 'M' ",len(closelist))
    print("spece complixty of 'M' :",spece)
    print("______________________________________________________________________________________________________________________________________________________________")
    spece,cost,closelist, path = astar(maze2, start2, end2,'E')
    print("The straight line distance")
    print(" E--->",path)
    print(" cost of path of ('E') 'E' = ",cost)
    print(" Time complixty 'E' ",len(closelist))
    print("spece complixty 'E' :",spece)
    #cost1,closelist1,path1=astar2(maze,start,end)

    #print(" M--> ",path1)
    #print(" cost M = ",cost1)
    #print(" number of exbanded node ",len(closelist1))
   

    

    




if __name__ == '__main__':
    main()
