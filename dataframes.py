import pandas as pd
import numpy as np

data = {
    "emp_id":     list(range(101, 126)),
    "name":       ["Alice", "Bob", "Carla", "David", "Elena", "Frank", "Grace",
                   "Henry", "Irene", "Jack", "Karen", "Leo", "Maria", "Nate",
                   "Olivia", "Paul", "Quinn", "Rosa", "Sam", "Tina", "Uma",
                   "Victor", "Wendy", "Xavier", "Yara"],
    "department": ["Sales", "IT", "HR", "Sales", "IT", "Finance", "Sales",
                   "IT", "HR", "Finance", "Sales", "IT", "Finance", "HR",
                   "Sales", "IT", "Finance", "Sales", "HR", "IT", "Finance",
                   "Sales", "IT", "HR", np.nan],
    "age":        [29, 41, 35, np.nan, 28, 52, 33, 45, np.nan, 38, 27, 31, 49,
                   36, 30, np.nan, 42, 26, 55, 34, 39, 44, 32, np.nan, 37],
    "salary":     [58000, 82000, 61000, 55000, np.nan, 97000, 62000, 91000,
                   59000, np.nan, 54000, 78000, 99000, 60000, 57000, 85000,
                   np.nan, 52000, 64000, 80000, 93000, 66000, 76000, 58000,
                   72000],
    "years_exp":  [4, 15, 9, 3, 5, 25, 8, 20, 11, 12, 2, 7, 22, 10, 6, 18, 14,
                   1, 30, 9, 13, 17, 6, 12, 10],
    "rating":     [4.2, 3.8, 4.5, 3.1, np.nan, 4.8, 3.9, 4.1, np.nan, 4.4, 3.5,
                   4.0, 4.7, 3.6, 4.3, np.nan, 4.6, 3.2, 3.9, 4.2, 4.5, 4.0,
                   3.7, np.nan, 4.1],
}
employees_df = pd.DataFrame(data)
#1
print(employees_df.head())
print(employees_df.shape)
print(employees_df.dtypes)
#2
print(employees_df["name"].head(n=4))
#3
print(employees_df[["name", "department", "salary"]].head(n=4))
#4
print(employees_df[employees_df["salary"]>80000][["name", "department", "salary"]])
#5
print(employees_df[(employees_df["department"] == "IT") & (employees_df["years_exp"]>10)][["name", "years_exp"]])
#6
print(employees_df[employees_df["name"].str.startswith("A")]["name"])
#7
print(employees_df.sort_values(["department", "salary"]))
#8
print(employees_df.sort_values(["department", "salary"],ascending=[True,False]))
#9
employees_df["monthly_salary"] = (employees_df["salary"]/12).round(2)
print(employees_df[["salary", "monthly_salary"]])
#10
employees_df["senior"] = employees_df["years_exp"] >= 10
print(employees_df[["name", "years_exp", "senior"]])
#11

employees_df["name"] = employees_df["name"].str.upper()
print(employees_df["name"])
#12
employees_df["exp_level"] = pd.cut(employees_df["years_exp"],
                                   bins=[0,5,15,100],
                                   labels=["Junior","Mid","Senior"],
                                   right=True)
print(employees_df[["years_exp", "exp_level"]])
#13
employees_df_copy = employees_df.copy()
#14
employees_df["department"] = employees_df["department"].fillna("Unknown")
print(employees_df["department"])
#15
print(employees_df.dropna(subset=["salary"]))
#16
print(employees_df.dropna())
#17
age_mean = employees_df["age"].mean()
employees_df = employees_df_copy.copy()
employees_df["age"] = employees_df["age"].fillna(age_mean).round(0)
print(employees_df[["name", "age"]])
#18
salary_median = employees_df["salary"].median()
employees_df["salary"] = employees_df["salary"].fillna(salary_median)
print(employees_df["salary"])
#19
summary_stats = employees_df.describe().round(0)
print(summary_stats)
#20
print(employees_df["salary"].mean())
print(employees_df["salary"].median())
print(employees_df["salary"].max())
print(employees_df["salary"].min())
print(employees_df["salary"].std())
print(employees_df["salary"].quantile(q=0.9))
#21
correlations = employees_df[["age", "salary", "years_exp", "rating"]].corr()
print(correlations)
#22
print(employees_df.groupby(["department"]).agg({"salary":"mean"}))








