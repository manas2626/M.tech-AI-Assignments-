import pandas as pd 
import  matplotlib.pyplot as plt

data =  pd.read_csv('data.csv')

def loss_function(m,b,points):
    total_error=0
    for i in range (len(points)):
        x=points.iloc[i].studytime
        y=points.iloc[i].score
        total_error += (y - (m * x + b)) ** 2
    return total_error / len(points)

def gradient_descent(m_now, b_now, points, L):
    m_gradient = 0
    b_gradient = 0
    N = float(len(points))

    for i in range(len(points)):
        x = points.iloc[i].studytime
        y = points.iloc[i].score
        prediction = m_now * x + b_now

        m_gradient += -(2 / N) * x * (y - (m_now * x+ b_now))
        b_gradient += -(2 / N) * (y - (m_now * x + b_now))

    m = m_now - (L * m_gradient)
    b = b_now - (L * b_gradient)
    return m, b

m=0
b=0
L=0.0001
epochs=1000

for i in range(epochs):

    if i%50==0:
        print(f"Epoch: {i}")
    m, b = gradient_descent(m, b, data, L)
print(m,b)

plt.scatter(data.studytime, data.score)
plt.plot(data.studytime, m*data.studytime + b, color='black')
plt.plot(list(range(0, 11)), [m*x + b for x in range(0, 11)], color='red')
plt.show()
