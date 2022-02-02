import pandas as pd
import statistics
df=pd.read_csv(r"C:/Users/kanis/OneDrive/Mithun-One drive/OneDrive/Desktop/hello/).csv")
x=df["Weight"]

m1=statistics.median(x)
m2=statistics.mode(x)
m3=statistics.mean(x)
print (m1)
print (m2)
print (m3)

