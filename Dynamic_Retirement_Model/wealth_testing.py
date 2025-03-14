'''
-----------------------------------------------------
This is module is the wealth and cash savings testing
area for all the functions created in the wealth submodel.
Testing is conducted here before importing the function into
the main application model.
-----------------------------------------------------
Author: Lloyd Nsambu
ID: HIM
Email: tendolloyd@gmail.com
Started:  Jan 24, 2025
Completed: March 13,2025
'''

from dataclasses import dataclass
import datetime
import pandas as pnds

from wealth_submodel import cash_saved_during_year, wealth_that_year, wealths_accumulator, cash_accumulator,years_to_retirement
from salary_submodel import salary_at_year, salary_presenter




@dataclass
class ModelInputs:
    starting_salary: float = 50494
    promos_every_n_years: float = 3
    promo_raise: float = 0.02
    cost_living_raise: float = 0.00
    savings_rate: float = 0.20
    interest_rate: float = 0.0275           
    prior_wealth: float = 0 
    desired_cash: float = 3000000
    current_year: int = datetime.datetime.now().year

data = ModelInputs()

working_years = 10
salaries, years_list = salary_presenter(data,working_years)        

# Intializing the wealth and cash savings.
# All the calculations are done in the wealth sub model and imported here for testing.
cash_savings = cash_accumulator(data,cash_saved_during_year, working_years)    
wealths = wealths_accumulator(data, working_years,wealth_that_year)


#This loop creates a list that'll be used as an index from the df
years_past = []
for i in range(1,working_years+1):
    years_past.append(i)

# combining data cash and wealth into single df
savings_n_wealths = {
    'year': years_list,
    'savings': cash_savings,
    'wealth': wealths,
    'years_past':years_past
}

# Test/view the dataframes created
df_savings_n_wealths = pnds.DataFrame(savings_n_wealths, index=years_past)
print(df_savings_n_wealths)


## testing the retirement determiner... The logic works properly like the formula 😁

#retirement_year, wealth_at_retirement = years_to_retirement(data, wealth_that_year)

#print(f"Your retirement year is: {retirement_year}")
#print(f"Your wealth at retirement year is: {wealth_at_retirement:,.2f}")

