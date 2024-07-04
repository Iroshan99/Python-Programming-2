import seaborn as sns
from numpy import random
import matplotlib.pyplot as plt

sns.distplot(random.normal(size=1000),hist=False)
plt.show()