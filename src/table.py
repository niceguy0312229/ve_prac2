import pandas as pd
import numpy as np


#----------------
# ex-1)
#----------------
df = pd.DataFrame(np.random.randn(10,5))  # showing table, look tidy!!
#df = np.random.randn(10,5) #showing just array 

# just head !!!
print(f"Only head portion(5 lines)........ \n{df.head()}")   

# show full
print(f"Shows full........\n{df}")

#----------------
# ex-2)
#----------------
data = {
    'Name': ['Tom', 'Jack', 'Steve', 'Ricky'],
    'Age': [28, 34, 29, 42]
}
df = pd.DataFrame(data)
print("original shape :", df.shape)
print(df)
df_transposed = df.transpose()
print("\nTransposed shape:", df_transposed.shape)
print(df_transposed)
print("\n")


#----------------
# ex-3)
#----------------
lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks']
df = pd.DataFrame(lst)
print(df)
print(df.shape)



#df = pd.DataFrame([lst])
#print(df)
#print(df.shape)