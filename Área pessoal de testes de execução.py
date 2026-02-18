import numpy as np
import matplotlib.pyplot as plt

vendas = np.random.randint(1000, 3000, 50)
meses = np.arange(1, 51)
plt.figure(1, figsize=(15, 4.5))
plt.subplot(1,3,1)
plt.plot(meses, vendas, "-", color='red')
plt.axis([0, 50, 0, max(vendas)+200])
plt.xlabel('Meses')
plt.ylabel("Vendas")

plt.subplot(1,3,2)
plt.scatter(meses, vendas)

plt.subplot(1,3,3)
plt.bar(meses, vendas)
plt.show()