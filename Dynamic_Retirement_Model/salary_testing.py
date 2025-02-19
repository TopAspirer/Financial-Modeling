

## this module will be used to test how the data calculated by the functions will be framed. 
## The goal of this model is to create a method to frame the salary data in an organized manner


import model_functions as mf
from dataclasses import dataclass
import datetime

from salary_submodel import salary_at_year
import pandas as pnds

@dataclass
class ModelInputs:
    starting_salary: float = 100000
    promos_every_n_years: float = 2
    promo_raise: float = 0.02
    cost_living_raise: float = 0.02
    savings_rate: float = 0.15
    interest_rate: float = 0.03           
    #prior_money: float = 0 
    desired_cash: float = 10000
    current_year: int = datetime.datetime.now().year


data = ModelInputs
num_years = 8

def salary_presenter(data,num_years):
    """
    Does the whole salary calculation for a number x number years.
    Parameters:
    - The number of years are passed as a parameter
    - Data

    This function isn't a proper function in the sense of it's organization.
    It's made so that using the salary data in other testing modules doesn't require me to 
    code and paste this whole block of code....
    """
    promo_every_n_year = data.promos_every_n_years
    date_list = []
    salaries = []

    current_year = ModelInputs.current_year + 1
    for a in range(num_years):  
        date_list.append(current_year + a )

    temp_current_yr = current_year

    promos_list = []
    promo_list_date = []
    MAX_RANGE_OF_PROMOS = current_year + 100

    for i in range(num_years):
        year = i + 1
        temp_current_yr = i + 1     
        salary =  round(salary_at_year(data, year), 2)
        salaries.append(salary)        
        if temp_current_yr in range(promo_every_n_year,MAX_RANGE_OF_PROMOS, promo_every_n_year):
            promos_list.append(year)
            promo_list_date.append(temp_current_yr)
        
    return salaries, date_list
     
salaries, date_list = salary_presenter(data,num_years)

salary_data = {
     'year': date_list,
     'salary': salaries
}



df_salary = pnds.DataFrame(salary_data)                             
print(df_salary)

# I want to know the total over compensation over my working years.

total_compensation = sum(salaries)
print(salaries)