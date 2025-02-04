

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
    promos_every_n_years: float = 5
    promo_raise: float = 0.20
    cost_living_raise: float = 0.02
    savings_rate: float = 0.15
    interest_rate: float = 0.0315           
    #prior_money: float = 0 
    desired_cash: float = 2500000
    current_year: int = datetime.datetime.now().year


data = ModelInputs
promo_every_n_year = data.promos_every_n_years
num_years = 8

# This for loop makes a list of years depending on the amount of year are being tested. 
# 1 plus current year so that the salary projection is accurate. 
date_list = []
salaries = []

current_year = data.current_year + 1
for a in range(num_years):  
    date_list.append(current_year + a )

temp_current_yr = current_year

promos_list = []
promo_list_date = []
MAX_RANGE_OF_PROMOS = current_year + 100

for i in range(num_years):
    year = i + 1
    temp_current_yr = i + 1     
    salary =  round(sf.salary_at_year(data, year), 2)
    salaries.append(salary)        
    if temp_current_yr in range(promo_every_n_year,MAX_RANGE_OF_PROMOS, promo_every_n_year):
         promos_list.append(year)
         promo_list_date.append(temp_current_yr)
    #elif year not in range(promo_every_n_year,120, promo_every_n_year):
     #   print(f"Salary in year {year}: ${salary:,.2f}")

     

salary_data = {
     'year': date_list,
     'salary': salaries
}



#df = pnds.DataFrame(data = salary_data)

#print(df)

print(f"years: {len(date_list)}")
print(f"Salaries: {len(salaries)}")

# creating promotions dataframe



print(f"Total promotions: {len(promos_list)}")

promotions = {
    'year': date_list,
    'promotion': promos_list

}

df_2 = pnds.DataFrame(zip(promo_list_date,promos_list))                             
print(df_2)

