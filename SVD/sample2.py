import numpy as np
a=np.array(
    [[0,0,1,1,0,0,0,0,0],
     [0,0,0,0,0,1,0,0,1],
     [0,1,0,0,0,0,0,1,0],
     [0,0,0,0,0,0,1,0,1],
     [1,0,0,0,0,1,0,0,0],
     [1,1,1,1,1,1,1,1,1],
     [1,0,1,0,0,0,0,0,0],
     [0,0,0,0,0,0,1,0,1],
     [0,0,0,0,0,2,0,0,1],
     [1,0,1,0,0,0,0,1,0],
     [0,0,0,1,1,0,0,0,0]]
)




u,s,v = np.linalg.svd(a)