class Node: 
    ''' node configration with its data ( matrix "grid puzzel" , g(n) = 0  , f(n)= 0 )'''
    def __init__(self,mat,gn,fn):
         self.mat = mat
         self.gn = gn 
         self.fn = fn 

    def successor(self):
        ''' this function is responsible for generating the successors of the current node'''
        successors=[]
        ''' get the loction of the blank tile (x,y) ,'_' means blank, m is our grid data of current node '''
        
        x,y = self.blank_tile(self.mat,'0')

        ''' generate 4 new locations for the blank tiles and stored then in new_loc[] array'''
        new_loc= [[x-1,y],[x+1,y],[x,y-1],[x,y+1]]
        for i in new_loc:
           new_succsessor= self.swapping(self.mat,i[0],i[1],x,y)
           if new_succsessor != 0:
               new_node = Node(new_succsessor,self.gn+1,0)
               successors.append(new_node)
        return successors
        

    '''  get a copy of current node to swapping it with new blank tile loction '''
    def swapping(self,current_mat,x1,y1,x,y):
        child_m =[]
        if x1 >= 0 and x1 < len(self.mat) and y1 >= 0 and y1 < len(self.mat):
            for i in current_mat:
                t =[]
                for j in i:
                    t.append(j)
                child_m.append(t)
            '''  end of copying process '''        
            temp= child_m[x1][y1]
            child_m[x1][y1] =child_m[x][y]
            child_m[x][y] = temp
            return child_m
        else:
            return 0

    def blank_tile(self,m,a):
        for i in range(0,len(self.mat)):
            for j in range(0,len(self.mat)):
                if self.mat[i][j] == a:
                    return i,j


        
