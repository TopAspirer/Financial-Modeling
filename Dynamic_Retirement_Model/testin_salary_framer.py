

## this module will be used to test how the data calculated by the functions will be framed. 
## The goal of this model is to create a method to frame the salary data in an organized manner


import model_functions as mf
from dataclasses import dataclass
import datetime

import salary_functions as sf
import pandas as pnds

@dataclass
class ModelInputs:
    starting_salary: float = 100000
    promos_every_n_years: float = 3
    promo_raise: float = 2
    cost_living_raise: float = 0.02
    savings_rate: float = 0.15
    interest_rate: float = 0.0315           
    #prior_money: float = 0 
    desired_cash: float = 2500000
    current_year: int = datetime.datetime.now().year


data = ModelInputs
num_years = 9
promo_every_n_year = data.promos_every_n_years


# This for loop makes a list of years depending on the amount of year are being tested. 
# 1 plus current year so that the salary projection is accurate. 
years_list = []
current_year = data.current_year + 1
for a in range(num_years):  
    years_list.append(current_year + a )

salaries = []




for i in range(num_years):
    year = i + 1      
    salary =  round(sf.salary_at_year(data, year), 2)
            
    if year in range(promo_every_n_year,120, promo_every_n_year):
        print(f"You get a raise in year {year}: ${salary:,.2f}")
    elif year not in range(promo_every_n_year,120, promo_every_n_year):
        print(f"Salary in year {year}: ${salary:,.2f}")

        salaries.append(salary)
    

print(years_list)   
print(salaries)
    

salary_data = {
     'year': years_list,
     'salary': salaries
}

df = pnds.DataFrame(data = salary_data)

print(df)