import numpy as np

def least_squares_estimation(X1, X2):

  E = np.zeros((3, 3))
  # computing the matrix A
  Mat_A = np.zeros((len(X1),9))
  # print("Mat_A shape before wala:", Mat_A.shape)
  for i in range(len(X1)):
    x1,y1,z1 = X1[i]
    x2,y2,z2 = X2[i]
    Mat_A[i] = np.array([x1*x2,x2*y1,x2*z1,y2*x1,y2*y1,y2*z1,z2*x1,z2*y1,z2*z1])
    
  # Mat_A= np.kron(X1,X2)
  # print("Mat_A shape after multiplication:", Mat_A.shape)
  # computing the SVD of A
  U,S,Vt = np.linalg.svd(Mat_A)
  # print("U shape:", U.shape)
  
  # print("Vt shape:", Vt.shape)
  E_vec = Vt[-1,:]
  
  # reshaping the vector to matrix
  E1 = E_vec.reshape((3,3))
  # print("E_vec shape:", E_vec.shape)

# enforcig the rank 2 constraint
  U1,S1,Vt1 = np.linalg.svd(E1)
  b = np.array([[1,0,0],[0,1,0],[0,0,0]])
  c = np.dot(b,Vt1)
  a = np.dot(U1, c)
  E= a
  # print("E shape:", E.shape)

  return E
