import numpy as np
import scipy.linalg as sp
#Your optional code here
#You can import some modules or create additional functions

def lu(A, b):
    x = sp.lu_factor(A,False,True)
    sol = sp.lu_solve(x,b,0,False,True)
    return list(sol)
    
def sor(A, b):
    sol = []
    A = np.asarray(A)
    b = np.asarray(b)

    #A = D-L-U 
    #Compute matrix D     
    D = np.zeros([len(A),len(A.T)])
    for i in range(len(A)):
        D[i][i] = A[i][i]
        
    #Compute matrix L
    L = np.zeros([len(A),len(A.T)])
    for i in range (len(A)):
        for j in range (0,i):
            L[i][j] = -A[i][j]
    
    #Compute matrix U      
    U = np.zeros([len(A),len(A.T)])
    for i in range (len(A)):
       for j in range(i+1, len(A)):
            U[i][j] = -A[i][j]
            
    #Calculate matrix Kj
    Kj = np.dot(sp.inv(D),(L+U))
    SR = max(sp.eigvals(Kj))     # Spectral Radius
    w = 2*(1-np.sqrt(1-(SR**2)))/(SR**2)  # Calculate optimal omega
    
    Q = np.zeros([len(A),len(A.T)])
    for i in range (0, len(A)):
        for j in range (0, len(A)):
            Q[i][j] = (1/w)*(D[i][j] - w*L[i][j])    
            
    X = b
    for i in range(20):
        X = np.dot(sp.inv(Q),np.dot((Q-A),X)) + np.dot(sp.inv(Q),b)
        print("Iteration %1d: " %(i+1), X)
        
    sol = X 
    return list(sol)

def solve(A, b):
    A = np.asarray(A)
    b = np.asarray(b)
    
    #check if the eigen values of matrix are positive
    eigenvalue_pos = np.all(np.linalg.eigvals(A) > 0)
    
    #check if it is symmetry
    symmetry = (A.T == A).all()
    
    #check if the matrix are positive definite
    check = (eigenvalue_pos and symmetry)    
    
    condition = not(check) # State and implement your condition here
    if condition:
        print('Solve by lu(A,b)')
        return lu(A,b)
    else:
        print('Solve by sor(A,b)')
        return sor(A,b)

if __name__ == "__main__":
    ##import checker
    ##checker.test(lu, sor, solve)
    
    A = [[2,1,6], [8,3,2], [1,5,1]]
    b = [9, 13, 7]

    sol = solve(A,b)
    print(sol)
    
    A = [[6566, -5202, -4040, -5224, 1420, 6229],
         [4104, 7449, -2518, -4588,-8841, 4040],
         [5266,-4008,6803, -4702, 1240, 5060],
         [-9306, 7213,5723, 7961, -1981,-8834],
         [-3782, 3840, 2464, -8389, 9781,-3334],
         [-6903, 5610, 4306, 5548, -1380, 3539.]]
    b = [17603,  -63286,   56563,  -26523.5, 103396.5, -27906]
    
    sol = solve(A,b)
    print(sol)
