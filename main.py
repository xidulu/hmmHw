import numpy as np

A2 = np.array([[0.5, 0.1, 0.4], [0.3, 0.5, 0.2], [0.2, 0.2, 0.6]])
B2 = np.array([[0.5, 0.5], [0.4, 0.6], [0.7, 0.3]])
pi2 = np.array([0.2, 0.3, 0.5])
Object2 = np.array([0, 1, 0, 0, 1, 0, 1, 1])

alpha = np.zeros((8,3 ))
alpha[0] = np.array(pi2) * B2[:, 0
                           ]

for i in range(1, len(Object2)):
    for j in range(0, 3):
        k = 0
        for t in range(0, 3):
            k += A2[t, j] * alpha[i - 1, t]

        alpha[i, j] = k * B2[j, Object2[i]]


print(alpha)

beta = np.zeros((8, 3))
beta[7] = np.ones((3,))

for i in range(6, -1, -1):
    for j in range(0, 3):
        for t in range(0, 3):
            beta[i, j] += A2[j, t] * B2[t, Object2[i + 1]] * beta[i + 1, t]

print(beta)

o = (np.sum(alpha[7]))
a = (alpha[3, 2])
b = (beta[3, 2])
print("P: {}".format(a * b / o))

