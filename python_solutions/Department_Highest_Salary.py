import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(employee, department, left_on='departmentId', right_on='id', how='left')
    merged_df.rename(columns={'name_x': 'Employee' , 'name_y': 'Department' ,'salary': 'Salary'}, inplace=True)
    max_salaries = merged_df.groupby('Department')['Salary'].max()
    max_salaries_df = max_salaries.reset_index()
    result = pd.merge(max_salaries_df, merged_df, on=['Department', 'Salary'], how='left')[['Department', 'Employee', 'Salary']]
    return result.sort_values(by='Department')
    