import pandas as pd
import numpy as np

# 6. Read and Write CSV Files Using Pandas

data = {"Name": ["Alice", "Bob", "Charlie"], "Marks": [85, 90, 78]}

df = pd.DataFrame(data)

# Write DataFrame to CSV
df.to_csv("students.csv", index=False)

# Read CSV File
df_csv = pd.read_csv("students.csv")

print("6. Data Read from CSV")
print(df_csv)


# 7. Filter Students with Marks Greater Than 80

filtered_students = df[df["Marks"] > 80]

print("\n7. Students with Marks > 80")
print(filtered_students)


# 8. Sort a DataFrame by Marks

sorted_df = df.sort_values(by="Marks", ascending=False)

print("\n8. Data Sorted by Marks")
print(sorted_df)


# 9. Handle Missing Values Using fillna()

data_missing = {"Name": ["Alice", "Bob", "Charlie"], "Marks": [85, np.nan, 78]}

df_missing = pd.DataFrame(data_missing)

df_missing["Marks"].fillna(df_missing["Marks"].mean(), inplace=True)

print("\n9. Missing Values Handled")
print(df_missing)


# 10. Find Mean, Maximum and Minimum Values of a Column

print("\n10. Statistics of Marks Column")

print("Mean:", df["Marks"].mean())
print("Maximum:", df["Marks"].max())
print("Minimum:", df["Marks"].min())


# 11. Merge Two DataFrames

df1 = pd.DataFrame({"ID": [1, 2, 3], "Name": ["Alice", "Bob", "Charlie"]})

df2 = pd.DataFrame({"ID": [1, 2, 3], "Marks": [85, 90, 78]})

merged_df = pd.merge(df1, df2, on="ID")

print("\n11. Merged DataFrame")
print(merged_df)


# 12. Group Data Department-wise

employees = pd.DataFrame(
    {
        "Department": ["HR", "IT", "HR", "IT", "Sales"],
        "Salary": [30000, 50000, 35000, 55000, 40000],
    }
)

grouped = employees.groupby("Department")["Salary"].mean()

print("\n12. Department-wise Average Salary")
print(grouped)


# 13. Rename DataFrame Columns

df_renamed = df.rename(columns={"Name": "Student_Name", "Marks": "Student_Marks"})

print("\n13. Renamed Columns")
print(df_renamed)


# 14. Find Unique Values from a Column

departments = employees["Department"].unique()

print("\n14. Unique Departments")
print(departments)


# 15. Apply Lambda Function on DataFrame Column

df["Bonus_Marks"] = df["Marks"].apply(lambda x: x + 5)

print("\n15. After Applying Lambda Function")
print(df)
