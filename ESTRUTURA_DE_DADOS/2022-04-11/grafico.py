import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(1, 10, 100)
funcs = [
    ( "Constante", np.ones(n.shape) ),
    ( "Logaritmico", np.log(n) ),
    ( "Linear", n ),
    ( "Log Linear", n * np.log(n) ),
    ( "Quadrada", n**2 ),
    ( "Cúbico", n**3 ),
    ( "Exponecial", 2**n )
]

plt.figure(figsize=(5,4))
plt.ylim(0, 100)

for index in range(0, len(funcs)):
    label, fun = funcs[index]
    plt.plot(n, fun, label=label)


plt.legend()
plt.ylabel("Tempo de execucao")
plt.xlabel("n")
plt.show()
