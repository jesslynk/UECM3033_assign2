UECM3033 Assignment #2 Report
========================================================

- Prepared by: Jesslyn Kho Hui Yee
- Tutorial Group: T3

--------------------------------------------------------

## Task 1 --  $LU$ Factorization or SOR method

The reports, codes and supporting documents are to be uploaded to Github at: 

[https://github.com/jesslynk/UECM3033_assign1](https://github.com/jesslynk/UECM3033_assign1)

Explain your selection criteria here.

First, we check if the matrix is diagonally dominant matrix, then we use LU method. If not, we continue to check if the matrix is positive definite, if so we solve it by SOR and if not, we use LU method. This is because when matrix is positive definite, we can find an optimum omega in the range (0,2) for SOR method and it will converge to the solution.

Explain how you implement your `task1.py` here.

In self-defined function named lu, factorize the matrix and solve the LU using scipy.linalg.lu_factor and scipy.linalg.lu_solve.

In self-defined function named sor, optimal w is found using the formula w = 2*(1-np.sqrt(1-(SR**2)))/(SR**2). If matrix A is positive definite, then optimal w will be found in the range of {0,2} which will give a quick convergence rate. 

To check the answer, the formula Ax=b is used by multiply the solution matrix with A and see whether the result is approximated to b.



















---------------------------------------------------------

## Task 2 -- SVD method and image compression

Put here your picture file (neko.jpg)




How many non zero element in Sigma?
There are 800 non zero elements for the three colors. All the elements are non zero.












Put here your lower and better resolution pictures. 

Lower resolution picture (lowerneko.png):


Better resolution picture (betterneko.png):








Explain how you generate these pictures from `task2.py`.


First, read the "neko.jpg" image and assigned to img. 
Then, compute the U, Sigma and V for each of the red, green and blue matrices using linalg.svd decomposition. 
Next, count the number of non zero elements in Sigma for red, green and blue colors respectively using the len function.

Create a new Sigma matrix by copying the each of original Sigma and keep the first n nonzero elements while set all other none zero elements to zero by using numpy function zeros_like. 
To construct a lower resolution matrix, change the dimension of Sigma to 30 by using indexing function like [0:30].
In order to use dot multiplication for new matrix, so the new matrix will be U*Sigma*V which is dimension of (800,1000). 
Then, create and display the new resolution images.
Repeat the same process by changing the resolution picture to 200.

What is a sparse matrix?
A sparse matrix is a matrix that allows special techniques to take advantage of the large number of "background" (commonly zero) elements.
A sparse matrix is also a matrix with the most of the elements are zero, meaning it has larger number of zero values compared to nonzero. 
When we compress the picture into lower resolution, the matrix will have more zeros and hence becoming a sparse matrix. Naturally, it is easier to be compressed and it requires less storage.

-----------------------------------

<sup>last modified: 10/3/16</sup>
