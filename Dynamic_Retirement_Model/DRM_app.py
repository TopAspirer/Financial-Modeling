import streamlit as st 
import datetime
import pandas as pnds
from dataclasses import dataclass

from salary_submodel import salary_at_year

@dataclass
class ModelInputs:
    starting_salary: float = 0
    promos_every_n_years: float = 0
    promo_raise: float = 0
    cost_living_raise: float = 0
    savings_rate: float = 0
    interest_rate: float = 0          
    prior_wealth: float = 0 
    desired_cash: float = 0
    working_years: int = 50
    current_year: int = datetime.datetime.now().year


model_data = ModelInputs()
data = model_data




## -----------------------------------------------------
# Draw the actual page 
st.title("Dynamic Retirement Model")

"""

This is a dynamic retirement model that takes your inputs and and determines
the amount of years it'll take you to reach your desired financial amount for retirement.
There are more tools yet to be added. 
"""

# added some spacing
""
""
st.write("### Enter Salary Data")


col1, col2, col3,col4 = st.columns(4)

data.starting_salary = col1.number_input("Starting Salary", min_value=0.0, value=20000.0)
data.interest_rate = col1.number_input("Interest Rate (%)", min_value=1.0, value=5.5)

data.promos_every_n_years = col2.number_input("Promotion every $x$ year", min_value=0, value=2)
data.promo_raise = col3.number_input("Promotion Raise (%)")

data.savings_rate = col2.number_input("Your rate of saving (%)", min_value=1.0,value=2.0 )
data.cost_living_raise = col3.number_input("Cost of living raise (%)", min_value=1.0, value=2.0)

data.working_years = st.slider("Working Years", min_value=1, max_value=99)   

# Code to prevent division by zero.

try:
    data.cost_living_raise /= 100
    data.promo_raise /= 100
    data.savings_rate /=100
    data.interest_rate /= 100
except ZeroDivisionError:
    st.warning("Please enter a valid value greater than 1.")
    


      
## Displaying the Inputs to the user.
colA, colB, colC = st.columns(3)

colA.metric(label="Starting Salary", value=f"${data.starting_salary:.1f}")
colB.metric(label="Working Years",   value=f"{data.working_years:d}")
colC.metric(label="Promotion Raise", value=f"{(data.promo_raise*100):.1f}%")

# Calculate yearly salary 

year_list = []         # A list that will hold the years in it. starting from the user's current year.
salaries = []
formatted_salaries = []    # Smthing to think about finishing. It's to make
NUM_YEARS = data.working_years
promo_every_n_year = data.promos_every_n_years

# Loop makes a list of years along
current_year = data.current_year + 1
for a in range(NUM_YEARS):
    year = a +1  
    year_list.append(current_year + a )
    years_past = year - current_year


    

# Loop makes a list of the salary earned at each year the user inputed
for i in range(NUM_YEARS):
    year = i + 1      
    salary =  round(salary_at_year(data, year), 2)
    salaries.append(salary)
    

# Loop makes a list of all the years a promotion is hit.
promos_list = []
MAX_NUM_OF_PROMOS = current_year + 1000
temp_current_yr = current_year
for b in range(NUM_YEARS):
    if temp_current_yr in range(promo_every_n_year,MAX_NUM_OF_PROMOS, promo_every_n_year):
         promos_list.append(year)


# This dictionary holds all the salary data for each year.
salary_data = {
     'Year': year_list,
     'Salary': salaries,
    


     
} 
promotion_data ={
    'date': year_list,
    'promotion': promos_list
}


df_salary = pnds.DataFrame(data = salary_data)

# Display the data frame as a chart
st.header("Yearly Salary Growth", divider='grey')
salary_growth_df = df_salary[['Year','Salary']].groupby('Year').min()
st.line_chart(salary_growth_df, x_label= 'Year', y_label='Salary')

st.write(f"""## Salary Summary:
             Total Compensation in Working Years: ${sum(salaries):,.2f}
    Total Federal Taxes Paid:  ----> Available soon <----
    Total Provincial Taxes Paid:  ----> Available soon <----

         """
         ) 

#<----------------------------------------------------------->

## This section will hold the wealth section

st.write(f"""----------------------------------------""", color='Ffff00')

st.write("### Enter Wealth Data")


col1a, col2a = st.columns(2)

data.desired_cash = col1a.number_input("Desired Retirement Cash ($)", min_value=0, value=0)
data.prior_wealth = col2a.number_input("Current Asset Value ($)", min_value=0, value=0)



colA1, colA2, colA3 = st.columns(3)

colA1.metric(label="Saving Rate", value=f"{(data.savings_rate*100):.1f}%")
colA2.metric(label="Current Asset Value", value=f"${data.prior_wealth:.1f}")
colA3.metric(label="Desired Retirment Goal", value=f"${data.desired_cash:.1f}")











