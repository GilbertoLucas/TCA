import numpy as np
from q5 import fecho_convexo_sequencial
from fecho_openCL2 import fecho_convexo_com_open_cl
import matplotlib.pyplot as plt

n = [1000, 10000, 100000]#, 250000]#[50, 100, 500, 1000, 10000, 100000]

DeltaT_paralelo = []
DeltaT_sequencial = []

fecho_x_paralelo = []#[[] for i in range(len(n))]
fecho_y_paralelo = []#[[] for i in range(len(n))]

fecho_x_sequencial = []#[[] for i in range(len(n))]#[]
fecho_y_sequencial = []#[[] for i in range(len(n))]#[]

x = []#[[] for i in range(len(n))]
y = []#[[] for i in range(len(n))]

for i in range(len(n)):

    random_numbers_x = np.random.uniform(-n[i], n[i], size=n[i]).tolist()
    random_numbers_y = np.random.uniform(-n[i], n[i], size=n[i]).tolist()

    x_np = (np.array(random_numbers_x)).astype(np.float32)
    y_np = (np.array(random_numbers_y)).astype(np.float32)

    x.append(x_np)
    y.append(y_np)

    time_paralelo, fecho_x_par, fecho_y_par = fecho_convexo_com_open_cl(x_np, y_np)
    time_sequencial, fecho_x_seq, fecho_y_seq = fecho_convexo_sequencial(x_np, y_np)

    DeltaT_paralelo.append(time_paralelo)
    DeltaT_sequencial.append(time_sequencial)

    fecho_x_paralelo.append(fecho_x_par)
    fecho_y_paralelo.append(fecho_y_par)

    fecho_x_sequencial.append(fecho_x_seq)
    fecho_y_sequencial.append(fecho_y_seq)

plt.plot(n, DeltaT_paralelo, '-x', label="Paralelo")
plt.plot(n, DeltaT_sequencial, '-d', label="Sequencial")
plt.xticks(n)
plt.xlabel("Número de pontos")
plt.ylabel("Tempo (s)")
plt.yscale("log")
plt.xscale("log")
plt.legend()
plt.grid()
plt.show()
#
# for i in range(len(n)):
#     plt.scatter(x[i], y[i], label = "Pontos")
#     plt.plot(fecho_x_sequencial[i], fecho_y_sequencial[i], '-x', label="Fecho convexo - Sequencial")
#     plt.plot(fecho_x_paralelo[i], fecho_y_paralelo[i], '-d', label="Fecho convexo - Paralelo")
#     plt.legend()
#     plt.grid()
#     plt.show()