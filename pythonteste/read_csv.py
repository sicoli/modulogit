import re
import pandas as pd
import numpy as np
import math

a = np.array([0,1,2,3])
a1 = np.vectorize(a)
a + 1
b = np.sin(a)

df =pd.DataFrame({'Valor': pd.Series(a),'Seno': pd.Series(b)})

print(df)
