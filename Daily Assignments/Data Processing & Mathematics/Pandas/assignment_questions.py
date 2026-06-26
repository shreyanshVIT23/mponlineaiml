import pandas as pd
import numpy as np

# 16. Student Management System Using Pandas
students = pd.DataFrame(
    {"ID": [101, 102, 103], "Name": ["Alice", "Bob", "Charlie"], "Marks": [85, 90, 78]}
)

print("16. Student Management System")
print(students)

students.loc[len(students)] = [104, "David", 88]
print("\nAfter Adding Student:")
print(students)


# 17. Employee Data Analysis (Sorting, Filtering, Grouping, Statistics)
employees = pd.DataFrame(
    {
        "Name": ["A", "B", "C", "D"],
        "Department": ["HR", "IT", "HR", "IT"],
        "Salary": [30000, 50000, 35000, 55000],
    }
)

print("\n17. Employee Analysis")

print("\nSorted by Salary:")
print(employees.sort_values("Salary"))

print("\nSalary > 40000:")
print(employees[employees["Salary"] > 40000])

print("\nDepartment-wise Average Salary:")
print(employees.groupby("Department")["Salary"].mean())

print("\nStatistical Analysis:")
print(employees["Salary"].describe())


# 18. Sales Data Analysis
sales = pd.DataFrame(
    {"Product": ["A", "B", "C", "D"], "Sales": [5000, 7000, 3000, 9000]}
)

print("\n18. Sales Analysis")

print("Total Sales:", sales["Sales"].sum())
print("Average Sales:", sales["Sales"].mean())
print("Highest Sales:", sales["Sales"].max())
print("Lowest Sales:", sales["Sales"].min())


# 19. Handle Missing Values
data = pd.DataFrame({"Marks": [80, np.nan, 90, np.nan, 70]})

print("\n19. Original Data")
print(data)

print("\nFill with Mean")
print(data.fillna(data["Marks"].mean()))

print("\nFill with 0")
print(data.fillna(0))

print("\nForward Fill")
print(data.ffill())


# 20. Merge, Concatenate and Join
df1 = pd.DataFrame({"ID": [1, 2, 3], "Name": ["A", "B", "C"]})

df2 = pd.DataFrame({"ID": [1, 2, 3], "Marks": [80, 90, 85]})

print("\n20. Merge")
print(pd.merge(df1, df2, on="ID"))

print("\nConcatenate")
print(pd.concat([df1, df2], axis=1))

print("\nJoin")
print(df1.join(df2["Marks"]))


# 21. Examination Result Analysis
results = pd.DataFrame(
    {
        "Name": ["A", "B", "C"],
        "Math": [95, 80, 88],
        "Science": [85, 92, 87],
        "English": [90, 84, 91],
    }
)

results["Total"] = results[["Math", "Science", "English"]].sum(axis=1)

print("\n21. Examination Analysis")

topper = results.loc[results["Total"].idxmax()]
print("Topper:")
print(topper)

print("\nAverage Marks:")
print(results["Total"].mean())

print("\nSubject-wise Highest Marks:")
print(results[["Math", "Science", "English"]].max())


# 22. Banking Transaction Analysis
transactions = pd.DataFrame(
    {"Customer": ["A", "B", "A", "C"], "Transaction": [5000, 3000, 2000, 7000]}
)

print("\n22. Banking Analysis")

print("Total Transactions:")
print(transactions["Transaction"].sum())

print("\nCustomer-wise Transactions:")
print(transactions.groupby("Customer")["Transaction"].sum())


# 23. Dataset Cleaning and Preprocessing
dirty_data = pd.DataFrame(
    {"Name": ["Alice", None, "Charlie"], "Marks": [85, np.nan, 90]}
)

clean_data = dirty_data.copy()

clean_data["Name"] = clean_data["Name"].fillna("Unknown")
clean_data["Marks"] = clean_data["Marks"].fillna(clean_data["Marks"].mean())

print("\n23. Cleaned Dataset")
print(clean_data)


# 24. Weather Data Analysis
weather = pd.DataFrame(
    {"Day": ["Mon", "Tue", "Wed", "Thu", "Fri"], "Temperature": [30, 35, 28, 40, 32]}
)

print("\n24. Weather Analysis")

print("Highest Temperature:", weather["Temperature"].max())

print("Lowest Temperature:", weather["Temperature"].min())

print("Average Temperature:", weather["Temperature"].mean())


# 25. Compare NumPy Arrays and Pandas DataFrames
array = np.array([[1, 2], [3, 4]])

dataframe = pd.DataFrame(array, columns=["A", "B"])

print("\n25. NumPy Array")
print(array)

print("\nPandas DataFrame")
print(dataframe)


# 26. Employee Salary Statistical Analysis
salary_data = pd.DataFrame({"Salary": [30000, 45000, 50000, 60000, 70000]})

print("\n26. Salary Statistics")

print("Mean:", salary_data["Salary"].mean())
print("Median:", salary_data["Salary"].median())
print("Maximum:", salary_data["Salary"].max())
print("Minimum:", salary_data["Salary"].min())
print("Standard Deviation:", salary_data["Salary"].std())


# 27. Random DataFrame and Mathematical Operations
random_df = pd.DataFrame(
    np.random.randint(1, 100, (5, 4)), columns=["A", "B", "C", "D"]
)

print("\n27. Random DataFrame")
print(random_df)

print("\nColumn-wise Sum")
print(random_df.sum())

print("\nColumn-wise Mean")
print(random_df.mean())


# 28. Attendance Report Generation
attendance = pd.DataFrame(
    {"Student": ["A", "B", "C", "D"], "Attendance": [90, 75, 85, 95]}
)

attendance["Status"] = attendance["Attendance"].apply(
    lambda x: "Eligible" if x >= 75 else "Not Eligible"
)

print("\n28. Attendance Report")
print(attendance)


# 29. Mini Data Analytics Project
sales_data = pd.DataFrame(
    {"Product": ["A", "B", "C", "D"], "Sales": [1000, 2500, 1800, 3200]}
)

print("\n29. Mini Data Analytics Project")

print("Best Selling Product:")
print(sales_data.loc[sales_data["Sales"].idxmax()])

print("\nAverage Sales:")
print(sales_data["Sales"].mean())


# 30. Data Visualization Preparation
monthly_sales = pd.DataFrame(
    {
        "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
        "Sales": [1200, 1800, 1500, 2200, 2500],
    }
)

print("\n30. Data for Visualization")
print(monthly_sales)
