
import numpy as np
import streamlit as st 
from model_functions import salary_at_year, cash_saved_during_year, wealth_that_year, years_to_retirement
from dataclasses import dataclass


@dataclass
class ModelInputs:
    starting_salary: float = 0
    promos_every_n_years: float = 0
    promo_raise: float = 0
    cost_living_raise: float = 0
    savings_rate: float = 0
    interest_rate: float = 0            
    #prior_money: float = 0 
    desired_cash: float = 0
    

model_data = ModelInputs()
data = model_data



## -----------------------------------------------------
# Draw the actual page 


"""
# Dynamic Retirement Model 

This is a dynamic retirement model that takes your inputs and and determines
the amount of years it'll take you to reach your desired financial amount for retirement.
There are more tools yet to be added. 
"""

# added some spacing
""
""
""

"What is your starting/current salary"
starting_salary = float(st.text_input("70,000....?"))
if starting_salary != float or int : 
    st.warning("Please enter a numerical value")
else:
    data.starting_salary = starting_salary



""
""
""

"Enter every number of years you get a promotion"
promos_every_n_years = float(st.text_input("$...?"))
if promos_every_n_years != float or int : 
    st.warning("Please enter a numerical value")
else:
    data.promos_every_n_years = promos_every_n_years

""
""
""

"What's the raise you recieve for every promotion?"
promo_raise = float(st.text_input("Enter as a percentage"))
if starting_salary != float or int : 
    st.warning("Please enter a valid numerical value")
else:
    data.promo_raise = promo_raise /100

""
""
""

"What's your current interest rate?"
current_interest_rate = float(st.text_input("Enter as a percentage"))
if starting_salary != float or int : 
    st.warning("Please enter a valid numerical value")
else:
    data.interest_rate = current_interest_rate /100

""
""
""

"Lastly, enter your desired cash to retire with"
promo_raise = float(st.text_input("$...."))
if starting_salary != float or int : 
    st.warning("Please enter a valid numerical value")
else:
    data.promo_raise = promo_raise /100


