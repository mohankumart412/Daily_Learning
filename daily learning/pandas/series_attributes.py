import pandas as pd

# list = [1,2,3,4,5,6]

df = pd.Series([1,2,3,4,5] ,index = ['a','b','c', 'd', 'e'], name = "numbers")

print(df.index,": all index values in series")
print(df.values,": all values in series")
print(df.name,": name of the series if exists")
print(df.size,": size of the series")
print(df.shape,": shape of the series")
print(df.array,": array of the series")
print(df.ndim,": dimention of the series")
print(df.nbytes,": the memory occupied by the values")
print(df.memory_usage(),": memory ocupied by both index and values")
print(df.memory_usage(index = False),": memory ocupied by only values because of index is false")
print(df.empty,": return true if the series is empty else false")
print(df.dtype,": datatype of the value")