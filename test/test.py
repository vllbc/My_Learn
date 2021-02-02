import numpy as np
import pandas as pd

ar1 = pd.Series(list("abcdefghijklmnopqrstuvwxyz"))
ar2 = pd.Series(np.arange(26))

df = pd.concat([ar1, ar2], axis=1)
print(df)
