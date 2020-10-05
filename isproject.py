class Node: 
    ''' node configration with its data ( matrix "grid puzzel" , g(n) = 0  , f(n)= 0 , parent position (x,y) )'''
    def __init__(self,mat,gn,fn,parent_x,parent_y):
         self.mat = mat
         self.gn = gn 
         self.fn = fn 
         self.parent_x =parent_x
         self.parent_y = parent_x

    def successor(self):
        ''' this function is responsible for generating the successors of the current node'''
        successors=[]
        ''' get the loction of the blank tile (x,y) ,'0' means blank, m is our grid data of current node '''
        
        x,y = self.blank_tile(self.mat,0)

        ''' generate 4 new locations for the blank tiles and stored then in new_loc[] array'''
        new_loc= [[x-1,y],[x+1,y],[x,y-1],[x,y+1]]
        for i in new_loc:
           new_succsessor= self.swapping(self.mat,i[0],i[1],x,y)
           if new_succsessor != 0:
               new_node = Node(new_succsessor,self.gn+1,0,x,y)
               successors.append(new_node)
        return successors
        

    '''  this function is responsible of getting a copy of current node to swapping it with new blank tile location
      and prevent the crearting any explored node'''
    def swapping(self,current_mat,x1,y1,x,y):
        child_m =[]
        if x1 >= 0 and x1 < len(self.mat) and y1 >= 0 and y1 < len(self.mat) and x1 != self.parent_x and y1 !=self.parent_y :
            '''copy the current matrix '''
            for i in current_mat:
                t =[]
                for j in i:
                    t.append(j)
                child_m.append(t)
            '''  end of copying process ''' 
            ''' swaping process'''       
            temp= child_m[x1][y1]
            child_m[x1][y1] =child_m[x][y]
            child_m[x][y] = temp
            return child_m
        else:
            return 0
    ''' This function is responsible of fining the blank tile location'''
    def blank_tile(self,m,a):
        for i in range(0,len(self.mat)):
            for j in range(0,len(self.mat)):
                if self.mat[i][j] == a:
                    return i,j

class Grid:
    size =[]
    explored_list = []
    frontier = []
    no_of_nodes_generated = 0

    def read_input(self):
        print("(Use 0 for blank tile, Insert spaces after each number & press enter after each row)")
        matrix = [[int(y) for y in input().strip().split(" ")] for x in range(3)]
        return matrix
    
    def evaluation_fn(self,current,goal):

        #return self.manhattan_distance_heuristic(current.mat,goal) + current.gn 
        return self.misplaced_tiles_heuristic(current.mat,goal) + current.gn 
    
    def misplaced_tiles_heuristic(self,current,goal):

        count=0
        for x in range(3):
            for y in range(3):
                if current[x][y] == 0: continue

                if current[x][y] != goal[x][y]:
                    count = count + 1

        return count

    def manhattan_distance_heuristic(self,current,goal):

        current_tile_positions = self.find_tile_positions(current)
        goal_tile_positions = self.find_tile_positions(goal)

        sum =0
        for x in range(8):
            x = x + 1
            sum = sum + abs(goal_tile_positions[x][0] - current_tile_positions[x][0]) + abs(goal_tile_positions[x][1] - current_tile_positions[x][1])

        return sum
    
    def find_tile_positions(self,state):

        tile_positions ={}
        for i in range(3):
            for j in range(3):
                tile_positions.update({state[i][j]:[i,j]})
        
        return tile_positions

    def search(self):
        print("Enter the start state")
        start_state = self.read_input()
        print("Enter the goal state")
        goal_state = self.read_input()
    
        start_state = Node(start_state,0,0,-1,-1)
        start_state.fn = self.evaluation_fn(start_state,goal_state)

        self.frontier.append(start_state)

        while len(self.frontier)!=0:
            current = self.frontier[0]
            print(current.mat)
                

            if self.misplaced_tiles_heuristic(current.mat,goal_state)==0:
                print("Goal found")
                print("No of Nodes Generated", len(self.frontier))
                print("No of Nodes Expanded", len(self.explored_list))
                break
                 # Goal is found 
                

            self.no_of_nodes_generated +=1
                

            for child in current.successor():
                child.fn = self.evaluation_fn(child,goal_state)
                self.frontier.append(child)

            self.explored_list.append(current)
            self.frontier.remove(current)
            #del self.frontier[0]
            
            self.frontier.sort(key=lambda  x:x.fn,reverse=False)
        if(len(self.frontier) == 0): print("No Solution")

           
 

if __name__ == "__main__":

    grid = Grid()
    grid.search()
