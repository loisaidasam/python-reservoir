from reservoir.sampling import *
import matplotlib.pyplot as plt
import numpy as np

uniform = UniformSampler(size=1000)
uniform.sample(range(50000))
data = np.array(uniform.reservoir)
plt.plot(data, data*0+1, 'o', alpha=0.3)
plt.title("Uniform Sampling")
plt.xlabel("n")
plt.yticks([1], ["Selected"])
plt.savefig("uniform.png")

plt.clf()

exponential = ExponentialSampler(size=1000, decay=10000)
exponential.sample(range(50000))
data = np.array(exponential.reservoir)
plt.plot(data, data*0+1, 'o', alpha=0.3)
plt.title("Exponential Sampling")
plt.yticks([1], ["Selected"])
plt.xlabel("n")
plt.savefig("exponential.png")
