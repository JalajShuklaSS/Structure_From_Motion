import numpy as np

def pose_candidates_from_E(E):
  transform_candidates = []
  ##Note: each candidate in the above list should be a dictionary with keys "T", "R"
  u,s,vt = np.linalg.svd(E)
  #extracting the thrid column of U and opposite
  Transform1 = u[:,2]
  Transform2 = -u[:,2]

  R_1 = np.array ([[0,-1,0],[1,0,0],[0,0,1]])
  R_2 = R_1.T 
  
  transform_candidates.append({'T':Transform1,'R':u@R_1.T@vt})
  transform_candidates.append({'T':Transform1,'R':u@R_2.T@vt})
  transform_candidates.append({'T':Transform2,'R':u@R_1.T@vt})
  transform_candidates.append({'T':Transform2,'R':u@R_2.T@vt})
  
  

  return transform_candidates