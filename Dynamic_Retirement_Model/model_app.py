
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


starting_salary = st.chat_input(
    "What is your starting/current salary",
    salary_salary = input("70,000....?")
)
data.starting_salary = float(starting_salary)

if starting_salary != float or int : 
    st.warning("Please enter a numerical value")

""
""
""

promos_every_n_years = st.chat_input(
    "Enter every number of years you get a promotion",
    promos_every_n_years = input("5...?")
)
data.promos_every_n_years = promos_every_n_years

""
""
""

promo_raise = st.chat_input(
    "What's raise you get for every promotion?",
    promo_raise = input("Enter as a percentage")
)
data.promo_raise = promo_raise /100