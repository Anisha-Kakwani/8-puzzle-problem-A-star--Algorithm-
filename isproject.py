class Node : 
    ''' node configration with its data ( matrix "grid puzzel" , g(n) = 0  , f(n)= 0 )'''
    def __init__(self, mat , gn , fn)
         self.mat = mat
         self.gn = gn 
         self. fn = fn 

    def successor(self)
        ''' this function is responsible for generating the successors of the current node'''
        successors=[]
        ''' get the loction of the blank tile (x,y) ,'0' means blank, m is our grid data of current node '''
        m = self.mat
         for i in range(0,len(self.mat))
            for j in range(0,len(self.mat))
                 if m[i][j] == 0:
                     x=i
                     y=j

        ''' generate 4 new locations for the blank tiles and stored then in new_loc[] array'''
        new_loc= [[x,y-1],[x,y+1],[x-1,y],[x+1,y]];


