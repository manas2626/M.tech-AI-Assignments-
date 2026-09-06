import math
x=[[9.066964285714283, -10.076785714285714, -0.726785714285712],
[-10.076785714285714, 159.125, 123.05357142857143],
[-0.726785714285712, 123.05357142857143, 684.6964285714286]]


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
        break #new_root is the first root
    root=new_root
root1= new_root    


b1 = -a + root1
b2 = b + root1 * b1


determinant = b1**2 - 4*b2
root2 = (-b1 + math.sqrt(determinant)) / 2
root3 = (-b1 - math.sqrt(determinant)) / 2

print("\nEigenValues :")
print("λ1 =", root1)
print("λ2 =", root2)
print("λ3 =", root3)
