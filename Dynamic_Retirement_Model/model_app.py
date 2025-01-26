

import streamlit as st 
from model_functions import salary_at_year, cash_saved_during_year, wealth_that_year, years_to_retirement
from dataclasses import dataclass


st.write("Dynamic Retirement Model")
st.write("by Lloyd Nsambu")

@dataclass
class ModelInputs:
    starting_salary: float = 60000
    promos_every_n_years: float = 5
    promo_raise: float = 0.15
    cost_living_raise: float = 0.02
    savings_rate: float = 0.25
    interest_rate: float = 0.05             
    #prior_money: float = 0 
    desired_cash: float = 1500000
    

model_data = ModelInputs()
data = model_data



## Testing the salary over a course of 40 years. 
## Returns a text indicating when you'll recieve a promotion.

promo_every_n_year = data.promos_every_n_years
year = 40

for i in range(year):
    year = i + 1
    salary = salary_at_year(data,year)
    if year in range(promo_every_n_year,120, promo_every_n_year):
        print(f"You get a raise in year {year}: ${salary:,.2f}")

    elif year not in range(promo_every_n_year,120, promo_every_n_year):
        print(f"Salary in year {year}: ${salary:,.2f}")



## Testing the cash saved over a period of time
prior_wealth = 0 

for i in range(year):
    year = i + 1
    cash_saved = cash_saved_during_year(data,year)
    print(f"Money saved in year {year}: ${cash_saved:,.2f}")



for i in range(year):
    """
    Loop takes the first wealth and iterates it to the prior wealth
    for the length of years that are being tested.

    !! Before you rerun it, restart all variables in the model, 
    otherwise the if you run the loop it'll keep adding onto the 
    previously calculated wealth that's in memory.
    """
    year = i + 1
    wealth = wealth_that_year(model_data,year, prior_wealth) 
    print(f"Your wealth in year {year}: ${wealth:,.2f}")
    prior_wealth = wealth


years_to_retirement(data)