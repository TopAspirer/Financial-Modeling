'''
-----------------------------------------------------
This is module is the lab, the testing center for
the salary calculations to make sure it adds up before
importing the functions from the salary submodel into 
main application module.
-----------------------------------------------------
Author: Top Aspirer
ID: HIM
Email: tendolloyd@gmail.com
Started:  Jan 24, 2025
Completed: March 13,2025
'''

from dataclasses import dataclass
import datetime

from salary_submodel import salary_presenter
import pandas as pnds


@dataclass
class ModelInputs:
    starting_salary: float = 100000
    promos_every_n_years: float = 2
    promo_raise: float = 0.08
    annual_salary_raise: float = 0.0
    savings_rate: float = 0
    interest_rate: float = 0          
    #prior_money: float = 0 
    desired_cash: float = 0
    current_year: int = datetime.datetime.now().year


data = ModelInputs()
num_years = 9


salaries, date_list = salary_presenter(data,num_years)

salary_data = {
     'year': date_list,
     'salary': salaries
}

# view/ testing the results... remove "#"
df_salary = pnds.DataFrame(salary_data)                             
print(df_salary)

total_compensation = sum(salaries)
print(f"Total life time compensation: ${total_compensation:,.2f}")


## - Created a salary growth rate calculator.
#grwth_rate = salaries_grwth_rate(salary_data)
#print(f"Nominal growth rate: {grwth_rate}")