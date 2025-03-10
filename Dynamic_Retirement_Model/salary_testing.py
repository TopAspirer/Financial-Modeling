

## this module will be used to test how the data calculated by the functions will be framed. 
## The goal of this model is to create a method to frame the salary data in an organized manner


import model_functions as mf
from dataclasses import dataclass
import datetime

from salary_submodel import salary_at_year, salary_presenter
import pandas as pnds

@dataclass
class ModelInputs:
    starting_salary: float = 100000
    promos_every_n_years: float = 0
    promo_raise: float = 0.0
    cost_living_raise: float = 0.0
    savings_rate: float = 0
    interest_rate: float = 0          
    #prior_money: float = 0 
    desired_cash: float = 0
    current_year: int = datetime.datetime.now().year


data = ModelInputs
num_years = 8


     
salaries, date_list = salary_presenter(data,num_years)

salary_data = {
     'year': date_list,
     'salary': salaries
}



df_salary = pnds.DataFrame(salary_data)                             
print(df_salary)

# I want to know the total over compensation over my working years.

total_compensation = sum(salaries)
print(f"Total life time compensation: ${total_compensation:,.2f}")
