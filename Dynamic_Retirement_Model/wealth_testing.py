# Module to handle Wealth submodel testing

from dataclasses import dataclass
import datetime
import pandas as pnds

from wealth_submodel import cash_saved_during_year, wealth_that_year, wealths_accumulator, cash_accumulator
from salary_submodel import salary_at_year, salary_presenter
from salary_testing import salary_presenter



@dataclass
class ModelInputs:
    starting_salary: float = 100000
    promos_every_n_years: float = 0
    promo_raise: float = 0.0
    cost_living_raise: float = 0.0
    savings_rate: float = 0.25
    interest_rate: float = 0.0           
    prior_wealth: float = 0 
    desired_cash: float = 0
    current_year: int = datetime.datetime.now().year

data = ModelInputs

working_years = 8
salaries, years_list = salary_presenter(data,working_years)        

#----------------------------------------------------------
## Starting to work on the wealth algorithm

# This loop creates a list that'll be used as an index from the df
years_past = []
for i in range(1,working_years+1):
    years_past.append(i)

cash_savings = cash_accumulator(data,cash_saved_during_year, working_years)     # Function called from the wealth submodel

# initializing wealth portion

wealths = wealths_accumulator(data, working_years,wealth_that_year)

# combining data cash and wealth into single df
savings_n_wealths = {
    'year': years_list,
    'savings': cash_savings,
    'wealth': wealths,
    'years_past':years_past
}

df_savings_n_wealths = pnds.DataFrame(savings_n_wealths, index=years_past)
print(df_savings_n_wealths)


