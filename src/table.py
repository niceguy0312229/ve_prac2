import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10,5))  # showing table, look tidy!!
#df = np.random.randn(10,5) #showing just array 


# just head !!!
print(df.head())   

# show full
print(df)


data = {
    'Name': ['Tom', 'Jack', 'Steve', 'Ricky'],
    'Age': [28, 34, 29, 42]
}
df = pd.DataFrame(data)
print(df)




lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks']
df = pd.DataFrame(lst)
print(df)