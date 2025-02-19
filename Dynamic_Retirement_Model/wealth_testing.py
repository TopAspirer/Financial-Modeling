# Module to handle Wealth submodel testing

from dataclasses import dataclass
import datetime
import pandas as pnds

from wealth_submodel import cash_saved_during_year, wealth_that_year
from salary_submodel import salary_at_year
from salary_testing import salary_presenter



@dataclass
class ModelInputs:
    starting_salary: float = 100000
    promos_every_n_years: float = 2
    promo_raise: float = 0.02
    cost_living_raise: float = 0.02
    savings_rate: float = 0.15
    interest_rate: float = 0.03           
    prior_wealth: float = 0 
    desired_cash: float = 10000
    current_year: int = datetime.datetime.now().year

data = ModelInputs

num_years = 8
salaries, years_list = salary_presenter(data,num_years)          # This is why this function was made! much clearer module😁

#----------------------------------------------------------
## Starting to work on the wealth algorithm

year = 1
data.prior_wealth = 0

print(f"Salaries over a span of {num_years} years: {salaries}")

# Building a dataframe of all saved cash
cash_savings = []
num_years_saving = []

print(f"Prior Wealth ${data.prior_wealth}\n")

for a in range(num_years):

    year = a + 1
    cash_saved = round(cash_saved_during_year(data, year),2)
    #print(f"Year {year}: ${cash_saved:,.2f}")
    cash_savings.append(cash_saved)
    num_years_saving.append(year)

savings_data = {
    'year': years_list,
    'savings': cash_savings
}


df_cash_savings = pnds.DataFrame(savings_data, index=num_years_saving)   # Index the number of year. 
print(f"\n{df_cash_savings}")





#wealth_accumulated = wealth_that_year(data,salary_at_year, year)
#print(f"Wealth Accumulated in year {year} is ${wealth_accumulated}")