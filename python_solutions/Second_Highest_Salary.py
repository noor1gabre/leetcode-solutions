import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_salaries = employee['salary'].unique()
    if len(unique_salaries) == 1:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    else:
        return pd.DataFrame({'SecondHighestSalary': [sorted(unique_salaries)[-2]]})