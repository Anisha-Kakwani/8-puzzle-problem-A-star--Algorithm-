class Grid:
    size =[]
    explored_list = []
    frontier = []

    def read_input(self):
        print("(Use 0 for blank tile, Insert spaces after each number & press enter after each row)")
        matrix = [[int(y) for y in input().strip().split(" ")] for x in range(3)]
        return matrix
    
    def evaluation_fn(self,current,goal):

        # return self.manhattan_distance_heuristic(current,goal) 
        #  level of node 
        return "Im the value of evaluation function"
    
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
        for x in range(9):
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
        print("Ready to solve the 8-puzzle-problem ?")
        print("Enter the start state")
        start_state = self.read_input()
        print("Enter the goal state")
        goal_state = self.read_input()

        print("Accepted states are")
        print(start_state,"@@@@@@@@@@@@@@@")
        print(goal_state,"$$$$$$$$$$$$$$$$")
        distance = self.manhattan_distance_heuristic(start_state,goal_state)
        print(distance)


if __name__ == "__main__":

    grid = Grid()
    grid.search()
    



