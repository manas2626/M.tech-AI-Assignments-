import numpy as np

np.set_printoptions(suppress=True)

def get_covariance_matrix(heights, weights):
    data = np.vstack((heights, weights))
    cov_matrix = np.cov(data)
    return cov_matrix

height_input = [1.70, 1.62, 1.52, 1.85, 1.91, 1.62]
weight_input = [72, 64, 84, 80, 72, 70]

matrix = get_covariance_matrix(height_input, weight_input)
print("Covariance Matrix:\n", matrix)
