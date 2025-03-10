import streamlit as st 
import datetime
import pandas as pnds
from dataclasses import dataclass




from salary_submodel import salary_at_year
from wealth_submodel import wealth_that_year,cash_saved_during_year, cash_accumulator, wealths_accumulator


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
    working_years: int = 8
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

data.starting_salary = col1.number_input("Starting Salary", min_value=0.0, value=0.0)
data.interest_rate = col1.number_input("Interest Rate (%)", min_value=0.0, value=0.0)

data.promos_every_n_years = col2.number_input("Promotion every $x$ year", min_value=0, value=2)
data.promo_raise = col3.number_input("Promotion Raise (%)")

data.desired_cash = col2.number_input("Desired Financial Goal", min_value=0.0,value=0.0 )
data.cost_living_raise = col3.number_input("Cost of Living Raise (%)", min_value=0.0, value=0.0)

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

years_list = []         # A list that will hold the years in it. starting from the user's current year.
salaries = []
working_years = data.working_years
promo_every_n_year = data.promos_every_n_years

# Loop makes a list of years along
current_year = data.current_year + 1
for a in range(working_years):
    year = a + 1  
    years_list.append(current_year + a )
    


    

# Loop makes a list of the salary earned at each year the user inputed
for i in range(working_years):
    year = i + 1      
    salary =  round(salary_at_year(data, year), 2)
    salaries.append(salary)
    


# This dictionary holds all the salary data for each year.
salary_data = {
     'Year': years_list,
     'Salary': salaries,
}


df_salary = pnds.DataFrame(data = salary_data)

# Display the salary data frame as a line graph
st.header("Yearly Salary Growth", divider='grey')
salary_growth_df = df_salary[['Year','Salary']].groupby('Year').min()
salary_chart = st.line_chart(salary_growth_df, x_label= 'Year', y_label='Salary')

st.write("## Salary Summary:")
with st.expander("📜"):
    st.write(f"""
    Total salary compensation: ${sum(salary_data['Salary']):,.2f}\n
    Total Working Years: {salary_data['Year'][-1] - data.current_year}\n
    Salary at {salary_data['Year'][-1]}: $ {salary_data['Salary'][-1]:,.2f}\n
    
    
    """)
    

#<----------------------------------------------------------->

## This section will hold the wealth and cash saved section

st.write(f"""----------------------------------------""", color='Ffff00')

st.write("### Enter Wealth Data")


col1a, col2a = st.columns(2)
data.desired_cash = col1a.number_input("Desired Retirement Cash ($)", min_value=0, value=0)
data.prior_wealth = col2a.number_input("Current Asset Value ($)", min_value=0, value=0)
data.savings_rate = st.slider("#### Savings Rate(%)", min_value=0, max_value=99)
data.savings_rate /= 100

colA1, colA2, colA3 = st.columns(3)
colA1.metric(label="Saving Rate", value=f"{(data.savings_rate*100):.1f}%")
colA2.metric(label="Current Asset Value", value=f"${data.prior_wealth:.1f}")
colA3.metric(label="Desired Retirment Goal", value=f"${data.desired_cash:.1f}")


# Calling the cash savings and wealth calculating functions with loops in them.


# This loop provides the index and years past column on the wealth and cash df.
years_past = []
for i in range(1,working_years+1):
    years_past.append(i)

# Cash savings and wealths accumulated
cash_savings = cash_accumulator(data,cash_saved_during_year, working_years)     
wealths = wealths_accumulator(data, working_years,wealth_that_year)

# Dictionary created for savings and wealth data
savings_n_wealths = {
    'Year': years_list,
    'Savings': cash_savings,
    'Wealth': wealths,
    'Years past':years_past
}

df_savings_n_wealths = pnds.DataFrame(savings_n_wealths, index=years_past)

wealth_chart = st.header("Wealth Vs Savings Accumulated", divider='grey')
wealth_growth_df = df_savings_n_wealths[['Year','Savings', 'Wealth']].groupby('Year').min()

st.line_chart(wealth_growth_df, x_label= 'Year', y_label='Value($)' )

#<-------------------------------------->

# This section will summarize the journey to retirement.



st.write(f"""----------------------------------------""")
st.write(f"Wealth and Savings Summary")
with st.expander("📈"):
    st.write(f"""
        ### Wealth Summary
            Projected Years: {len(savings_n_wealths['Years past'])}
            Preferred Savings Rate (of salary): {data.savings_rate*100}%
            Total Savings: ${sum(savings_n_wealths['Savings']):,.2f}
            Accumulated Wealth: ${sum(savings_n_wealths['Wealth']):,.2f}

            Financial Target Reached?
            ---> Feature Available Soon <----
            

        """

)
    
    











