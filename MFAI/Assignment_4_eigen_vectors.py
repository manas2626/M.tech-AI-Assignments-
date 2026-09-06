import math

def eigenValues(x):

    a=x[0][0]+x[1][1]+x[2][2]


    b=((x[1][1]*x[2][2])-(x[1][2]*x[2][1])) + ((x[0][0]*x[2][2])-(x[0][2]*x[2][0])) + ((x[0][0]*x[1][1])-(x[0][1]*x[1][0]))

   
    c= x[0][0]*((x[1][1]*x[2][2])-(x[1][2]*x[2][1])) - x[0][1]*((x[1][0]*x[2][2])-(x[1][2]*x[2][0])) + x[0][2]*((x[1][0]*x[2][1])-(x[1][1]*x[2][0]))
   

    def f(value):
        return value**3 - a*value**2 + b*value - c
    def derivative(value):
        return 3*value**2 - 2*a*value + b

    root=0
    for i in range(100):
        new_root= root - f(root)/derivative(root)
        if abs(new_root - root)<0.000001:
            break 
        root=new_root
    root1= new_root    

 
    b1 = -a + root1
    b2 = b + root1 * b1


    D = b1**2 - 4*b2
    root2 = (-b1 + math.sqrt(D)) / 2
    root3 = (-b1 - math.sqrt(D)) / 2

    return [root1, root2, root3]



A=[[9.066964285714283, -10.076785714285714, -0.726785714285712],
[-10.076785714285714, 159.125, 123.05357142857143],
[-0.726785714285712, 123.05357142857143, 684.6964285714286]]

eigenvalues= eigenValues(A)
for x in eigenvalues:
    print("\nEigenvalue:", x)

    M = [
        [A[0][0]-x,      A[0][1],        A[0][2]],
        [A[1][0],        A[1][1]-x,      A[1][2]],
        [A[2][0],        A[2][1],        A[2][2]-x]
    ]

    v1 = M[0][1] * M[1][2] - M[0][2] * M[1][1]
    v2 = M[0][2] * M[1][0] - M[0][0] * M[1][2]
    v3 = M[0][0] * M[1][1] - M[0][1] * M[1][0]

    length = math.sqrt(v1**2 + v2**2 + v3**2)
    v1 = v1 / length
    v2 = v2 / length
    v3 = v3 / length

    print("Eigenvector:", [v1, v2, v3])
