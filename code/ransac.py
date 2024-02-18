from lse import least_squares_estimation
import numpy as np

def ransac_estimator(X1, X2, num_iterations=60000):
    sample_size = 8

    eps = 10**-4

    best_num_inliers = -1
    best_inliers = None
    best_E = None

    for i in range(num_iterations):
        permuted_indices = np.random.RandomState(seed=(i*10)).permutation(np.arange(X1.shape[0]))
        sample_indices = permuted_indices[:sample_size]
        test_indices = permuted_indices[sample_size:]

        # estimating the essential matrix using the least squares method
        Sample_x1 = X1[sample_indices]
        Sample_x2 = X2[sample_indices]
        E = least_squares_estimation(Sample_x1, Sample_x2)

        inliers_s = []
        e3_define = np.array([0, 0, 1])
        e3 = e3_define.T
        e3_hat_s = np.array([[0, -e3[2], e3[1]], [e3[2], 0, -e3[0]], [-e3[1], e3[0], 0]])
        
        # computing the error by measuring the distance between the points and the epipolar lines
        for j in range(len(test_indices)):
            x1 = X1[test_indices[j]]
            x2 = X2[test_indices[j]]
            # finding the epipolar lines
            l1 = np.dot(E, x1)
            l2 = np.dot(E.T, x2)
            # getting the distance
            norm_1 = np.linalg.norm(np.dot(e3_hat_s, l1))
            norm_2 = np.linalg.norm(np.dot(e3_hat_s, l2))
            
      
            d1 = (np.dot(x2.T,l1))/(norm_1)
            d2 = (np.dot(x1.T,l2))/(norm_2)
            # print("d1:", d1)
            # print("d2:", d2)
            # print("norm_1:", norm_1)
            # print("norm_2:", norm_2)
            # finding error
            error = (d1**2 + d2**2)
            # print("error:", error)
            if error < eps:
                inliers_s.append(test_indices[j])

        inliers_s = np.array(inliers_s)
        inliers_1 = np.concatenate((sample_indices,inliers_s), axis=0)
        
        if inliers_1.shape[0] > best_num_inliers:
            best_num_inliers = inliers_1.shape[0]
            best_E = E
            best_inliers = inliers_1

    return best_E, best_inliers
