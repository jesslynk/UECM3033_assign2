UECM3033 Assignment #2 Report
========================================================

- Prepared by: Jesslyn Kho Hui Yee
- Tutorial Group: T3

--------------------------------------------------------

## Task 1 --  $LU$ Factorization or SOR method

The reports, codes and supporting documents are to be uploaded to Github at: 

[https://github.com/jesslynk/UECM3033_assign1](https://github.com/jesslynk/UECM3033_assign1)

Explain your selection criteria here.

If the matrix is sparse matrix, then we use SOR method. 
Sparse matrix is a matrix which the most elements are zero. 
The condition i set for deciding whether use LU or SOR by comparing the number of nonzero elements in matrix A with the half of the length of matrix A. 
If the nonzero element in matrix A is more than half of total elements in matrix A, it mean matrix A have large number of nonzero compared to zero. 
So if the condition is true, it will perform LU factorization, else it will perform SOR method. 
The number of nonzero element is counted by using numpy function,count_nonzero. 
The length of A is use len.

Explain how you implement your `task1.py` here.

In self-defined fucntion named lu, decompose the LU sand solve the LU using for.
To perform SOR method, set a iteration limit as 10 and initiate omega as 1.03. 
In self-defined fucntion named sor, let x be zero matrix which is same size as matrix b.

Use np.array to make the A and b to be a matrix. astype float is used to convert to float. 
Assign the variables sol=np.linalg.solve(A,b) 
Then solve the Ax=b by using LU if the condition is true ,else use SOR. 
Display the sol.









---------------------------------------------------------

## Task 2 -- SVD method and image compression

Put here your picture file (neko.jpg)




How many non zero element in Sigma?
There are 800 non zero elements for the three colours. All the elements are non zero.

Put here your lower and better resolution pictures. Explain how you generate
these pictures from `task2.py`.






First, create a self defined function named svd. Read the "neko.jpg" image and assiged to img. 
Then, compute the U, Sigma and V for for each of the red, green and blue matrices. 
Next, count the number of non zero elements in Sigma for red,green and blue colours respectively using the len function.

The following steps are in the built-in function,svd. 
Create a new Sigma matrix by copying the each of original Sigma and keep the first n nonzero elememts while set all other none zero elements to zero by using numpy function zeros_like. 
To construct a lower resolution matrix, change the dimension of Sigma to 30 by using indexing function like [0:30].
In order to use dot multiplication for new matrix,so the new matrix will be U*Sigma*V which is dimension of (800,1000). 
Then, create and display the new resolution images.
Repeat the same process by changing the resolution picture to 200.

What is a sparse matrix?
A sparse matrix is a matrix that allows special techniques to take advantage of the large number of "background" (commonly zero) elements.
A sparse matrix is also a matrix with the most of the elememts are zero, meaning it has larger number of zero values compared to nonzero. 
In contrast,a matrix where many elements are nonzero is called dense, as the Sigma matrix we had in task 2.

-----------------------------------

<sup>last modified: 10/3/16</sup>
