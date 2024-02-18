import numpy as np
import matplotlib.pyplot as plt

def show_reprojections(image1, image2, uncalibrated_1, uncalibrated_2, P1, P2, K, T, R, plot=True):

  # calculating the projection matrix
  ones_points1 = np.ones((P1.shape[0], 1))
  Points_1 = np.hstack((P1, ones_points1))
  print("Points_1 shape:", Points_1.shape)
    
  H_R_T = np.hstack((R, T.reshape(3, 1)))  # Fixing the syntax error here
  print("H_R_T shape:", H_R_T.shape)
    
  V_R_T_1_2 = np.vstack((H_R_T, np.array([0, 0, 0, 1])))
  print("V_R_T_1_2 shape:", V_R_T_1_2.shape)
    
  Final_2_1 = np.linalg.inv(V_R_T_1_2)
  print("Final_2_1 shape:", Final_2_1.shape)
    
  ones_points2 = np.ones((P2.shape[0], 1))
  Points_2 = np.hstack((P2, ones_points2))  # Fixing the syntax error here
  print("Points_2 shape:", Points_2.shape)
    
  a = np.dot(Final_2_1, Points_2.T)
  print("a shape:", a.shape)
    
  P2proj = np.dot(K, a[:3, :]).T
  print("P2proj shape:", P2proj.shape)

  b = np.dot(V_R_T_1_2, Points_1.T)
  P1proj = np.dot(K, b[:3, :]).T
    


  if plot:
      plt.figure(figsize=(6.4 * 3, 4.8 * 3))
      ax = plt.subplot(1, 2, 1)
      ax.set_xlim([0, image1.shape[1]])
      ax.set_ylim([image1.shape[0], 0])
      plt.imshow(image1[:, :, ::-1])
      plt.plot(P2proj[:, 0] / P2proj[:, 2],
              P2proj[:, 1] / P2proj[:, 2], 'bs')
      plt.plot(uncalibrated_1[0, :], uncalibrated_1[1, :], 'ro')

      ax = plt.subplot(1, 2, 2)
      ax.set_xlim([0, image1.shape[1]])
      ax.set_ylim([image1.shape[0], 0])
      plt.imshow(image2[:, :, ::-1])
      plt.plot(P1proj[:, 0] / P1proj[:, 2],
              P1proj[:, 1] / P1proj[:, 2], 'bs')
      plt.plot(uncalibrated_2[0, :], uncalibrated_2[1, :], 'ro')

  else:
      return P1proj, P2proj
