import pandas as pd
import numpy as np

# Creating a DataFrame
info = {
    "Name": ["Rahul", "Harhita", "Shradha"],
    "CGPA": [9.5, 7.5, 8.5]
}

df = pd.DataFrame(info)
print(df)

# Series: one-dimensional labeled array
s = pd.Series([1, 2, 3, 4, 5])
print(s)
print(type(s))
print(s.iloc[0])
print(s.iloc[2])

# Series with custom index
s = pd.Series([23, 45, 14, 26], index=["A", "B", "C", "D"])
print(s)
print(s.loc["A"])
print(s.iloc[0])
print(s.index)

# Series with mixed data types
s = pd.Series([23, 45, 14, 26, "abc"], index=["A", "B", "C", "D", 25])
print(s)
print(s.loc["A"])
print(s.loc["B"])
print(s.index)

# Vectorized operations
s1 = pd.Series([1, 2, 3, 4])
s2 = pd.Series([23, 45, 14, 26])
print(s1 + s2)

# Updating a Series value
s1.iloc[0] = 100
print(s1)

# Dropping an element (creates a new Series)
changed_s1 = s1.drop(0)
print(s1)
print(changed_s1)

# Creating another DataFrame
info = {
    "Name": ["Rahul", "Harhita", "Shradha"],
    "CGPA": [9.5, 7.5, 8.5],
    "age": [23, 45, 14]
}

df = pd.DataFrame(info)
print(df)
print(type(df))
print(df.columns)
print(df.index)

# Another DataFrame example
df2 = pd.DataFrame(
    [["Adam", 48],
     ["Bob", 45],
     ["Eve", 23]],
    columns=["Name", "Age"]
)
print(df2)

# NumPy array to DataFrame
np_arr = np.array([
    [1, 2, 3, 4],
    [4, 5, 6, 7]
])

df3 = pd.DataFrame(np_arr, columns=["A", "B", "C", "D"])
print(df3)

