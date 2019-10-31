import pandas as pd
from itertools import chain
df = pd.read_csv('higher.csv', names=["build1", "build2", "build3", "build4", "build5", "build6", "build7", "build8", "build9", "build10"])
# print(df.head())
# print (list(chain.from_iterable(df.iloc[1:, ::2].T.values)))
df['build2'] = pd.Series(list(chain.from_iterable(df.iloc[1:].T.values)))
df['build3'] = pd.Series(list(chain.from_iterable(df.iloc[2:].T.values)))
df['build4'] = pd.Series(list(chain.from_iterable(df.iloc[3:].T.values)))
df['build5'] = pd.Series(list(chain.from_iterable(df.iloc[4:].T.values)))
df['build6'] = pd.Series(list(chain.from_iterable(df.iloc[5:].T.values)))
df['build7'] = pd.Series(list(chain.from_iterable(df.iloc[6:].T.values)))
df['build8'] = pd.Series(list(chain.from_iterable(df.iloc[7:].T.values)))
df['build9'] = pd.Series(list(chain.from_iterable(df.iloc[8:].T.values)))
df['build10'] = pd.Series(list(chain.from_iterable(df.iloc[9:].T.values)))
print(df.head())
# df.to_csv('a1.csv')