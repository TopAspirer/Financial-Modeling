import streamlit as st 
import datetime
import pandas as pnds
from model_functions import cash_saved_during_year, wealth_that_year, years_to_retirement
from dataclasses import dataclass
from salary_functions import salary_at_year

@dataclass
class ModelInputs:
    starting_salary: float = 0
    promos_every_n_years: float = 0
    promo_raise: float = 0
    cost_living_raise: float = 0
    savings_rate: float = 0
    interest_rate: float = 0          
    prior_money: float = 0 
    desired_cash: float = 0
    working_years: int = 0
    current_year: int = datetime.datetime.now().year


model_data = ModelInputs()
data = model_data

st.title("Dynamic Retirement Model")


## -----------------------------------------------------
# Draw the actual page 


"""

This is a dynamic retirement model that takes your inputs and and determines
the amount of years it'll take you to reach your desired financial amount for retirement.
There are more tools yet to be added. 
"""

# added some spacing
""
""
st.write("### Input Data", divider='yellow')
col1, col2, col3,col4 = st.columns(4)
data.starting_salary = col1.number_input("Starting Salary", min_value=0, value=49000)
data.promos_every_n_years = col1.number_input("# Promotion every $x$ year", min_value=0, value=5)
data.interest_rate = col2.number_input("Interest Rate (in %)", min_value=0.0, value=5.5)
data.savings_rate = col2.number_input("Your rate of saving (in %)", min_value=0.0,value=0.25 )
data.cost_living_raise = col3.number_input("Cost of living raise (in %)", min_value=0.0, value=0.025)
data.desired_cash = col3.number_input("Desired cash for Retirment", min_value=0.0, value=120000.0)
data.working_years = col4.number_input("Working years", min_value=0, value=45)
data.prior_money = col4.number_input("Value of current assets", min_value=0.00, value= 5000.00)           # This doesn't work yet



      
## Displaying the Inputs to the user.
colA, colB, colC = st.columns(3)

colA.metric(label="Starting Salary", value=f"{data.starting_salary:,.2f}")
colB.metric(label="Working Years", value=f"{data.working_years:.1f}")
colC.metric(label="Desired Cash", value=f"{data.desired_cash:,.2f}")

# Calculate yearly salary 

date_list = []         # A list that will hold the years in it. starting from the user's current year.
year_list = []         # A list that holds the year number. 
salaries = []
formatted_salaries = []    # Smthing to think about finishing. It's to make
num_years = data.working_years
promo_every_n_year = data.promos_every_n_years

# Loop makes a list of years along
current_year = data.current_year + 1
for a in range(num_years):
    year = a +1  
    date_list.append(current_year + a )
    year_list.append(year)

# Loop makes a list of the salary earned at each year the user inputed
for i in range(num_years):
    year = i + 1      
    salary =  round(salary_at_year(data, year), 2)
    salaries.append(salary)
    

# Loop makes a list of all the years a promotion is hit.
promos_list = []
MAX_NUM_OF_PROMOS = current_year + 1000
temp_current_yr = current_year
for b in range(num_years):
    if temp_current_yr in range(promo_every_n_year,MAX_NUM_OF_PROMOS, promo_every_n_year):
         promos_list.append(year)


# This dictionary holds all the salary data for each year.
salary_data = {
     'date': date_list,
     'salary': salaries,
     'year' : year_list
     
} 
promotion_data ={
    'date': date_list,
    'promotion': promos_list

}


df_salary = pnds.DataFrame(data = salary_data)

# Display the data frame as a chart
st.header("Yearly Salary Growth", divider='grey')
salary_growth_df = df_salary[['date',"salary"]].groupby("date").min()
st.line_chart(salary_growth_df, x_label= 'Year', y_label='Salary')

# Display a point point graph that points all the dates that a promotion is hit.




# Sends a prompt to user that 
if salary_data['salary'][-1] != data.desired_cash:
    st.write("Within your working timeframe, you won't reach your retirement goald soley on salary.")
elif salary_data['salary'][-1] == data.desired_cash:
    st.write("Within your working timefram, you'll be able to reach your retirement goal")














