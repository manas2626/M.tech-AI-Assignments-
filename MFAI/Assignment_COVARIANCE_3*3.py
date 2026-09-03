# Data
X = [12.1,13.2,15.6,17.2,18.8,10.3,11.7,16.4]
Y = [48,59,32,18,41,32,31,30]
Z = [101,171,112,132,140,112,151,96]


n = len(X)
mean_X = sum(X) / n
mean_Y = sum(Y) / n
mean_Z = sum(Z) / n

def covariance(A, B):
    mean_A = sum(A) / len(A)
    mean_B = sum(B) / len(B)

    total = 0

    for i in range(len(A)):
        total += (A[i] - mean_A) * (B[i] - mean_B)

    return total / (len(A) - 1)

cov_xx = covariance(X, X)
cov_xy = covariance(X, Y)
cov_xz =covariance(X, Z)

cov_yx = covariance(Y, X)
cov_yy =  covariance(Y, Y)
cov_yz = covariance(Y, Z)

cov_zx =covariance(Z, X)
cov_zy = covariance(Z, Y)
cov_zz = covariance(Z, Z)

covariance_matrix = [
    [cov_xx, cov_xy, cov_xz],
    [cov_yx, cov_yy, cov_yz],
    [cov_zx, cov_zy, cov_zz]
]

print("\n3 x 3 Covariance Matrix:")

for row in covariance_matrix:
    print(row)
