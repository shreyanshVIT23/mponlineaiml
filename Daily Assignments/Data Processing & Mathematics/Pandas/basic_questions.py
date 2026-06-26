import pandas as pd

# 1. Create a Series using a List
data = [10, 20, 30, 40, 50]

series = pd.Series(data)

print("1. Pandas Series")
print(series)


# 2. Create a DataFrame from Dictionary
student_data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [20, 21, 22],
    "Marks": [85, 90, 88],
}

df = pd.DataFrame(student_data)

print("\n2. DataFrame from Dictionary")
print(df)


# 3. Display First and Last Rows using head() and tail()
print("\n3. First 2 Rows")
print(df.head(2))

print("\nLast 2 Rows")
print(df.tail(2))


# 4. Add a New Column in DataFrame
df["Grade"] = ["A", "A+", "A"]

print("\n4. DataFrame After Adding Grade Column")
print(df)


# 5. Delete a Column from DataFrame
df.drop("Age", axis=1, inplace=True)

print("\n5. DataFrame After Deleting Age Column")
print(df)
