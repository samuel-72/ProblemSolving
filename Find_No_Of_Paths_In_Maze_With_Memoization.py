def recursiveTraversal(row,col):

    global n, d

    if ( row < 0 or col < 0 ):
        return 0
                        
    if ( (row,col) in d.keys() ):
        return d[(row,col)]
    
    else:
        d[ (row,col) ] =  ( recursiveTraversal(row-1,col) + recursiveTraversal(row,col-1) )
        return  ( d[ (row,col) ] )

    



n = int(input("Enter the n in NxN matrix : ")) 
d = {}

for i in range(n):
    d [(i,0)] = 1
    d [(0,i)] = 1

print "Total no of paths : " + str(recursiveTraversal(n,n))

