import pandas as pd

s1 = pd.Series([10,20,30])

s2 = pd.Series([40,50,60])

print(s1,"s1 series")

print(s2,"s2 series")

print(s1 + s2)
print(s1 - s2)
print(s1 * s2)
print(s1 / s2)
print(s1 % s2)
print(s1 ** s2)
print(s1 < s2)
print(s1 > s2)
print(s1 == s2)

