'''
-----------------------------------------------------
The main application module
Run this file run the full model.
-----------------------------------------------------
Author: Lloyd Nsambu
ID: HIM
Email: tendolloyd@gmail.com
Started:  Jan 24, 2025
Completed: March 13,2025
'''


# External imports
import streamlit as st 
import datetime
import pandas as pnds
from dataclasses import dataclass

# Internal imports
from salary_submodel import salary_at_year, salaries_grwth_rate
from wealth_submodel import wealth_that_year, cash_saved_during_year, cash_accumulator, wealths_accumulator, years_to_retirement


@dataclass
class ModelInputs:
    starting_salary: float = 0
    promos_every_n_years: float = 0
    promo_raise: float = 0
    annual_salary_raise: float = 0
    savings_rate: float = 0
    interest_rate: float = 0          
    prior_wealth: float = 0 
    desired_cash: float = 0.0
    working_years: int = 8
    current_year: int = datetime.datetime.now().year


model_data = ModelInputs()
data = model_data




#with st.columns(3, gap='large', vertical_alignment='center')[1]:

st.markdown("<h1 style='text-align: center;'>Dynamic Retirement Tool</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Model Your Financial Future!</h4>", unsafe_allow_html=True)



# added some spacing
""
""
st.write("### Enter Salary Data")


col1, col2, col3,col4 = st.columns(4)

data.starting_salary = col1.number_input("Annual Salary", min_value=0.0, value=0.0, help="The income you expect in a year of work. ")
data.interest_rate = col1.number_input("Interest Rate (%)", min_value=0.0, value=2.75, help="Default: Current Central bank rate (Canada). Can adjust for different scenarios")

data.promos_every_n_years = col2.number_input("Promotion every $x$ year", min_value=0, value=2, help="Ex. 'I expect a promotion every 2 year.' Adjust to your scenario")
data.promo_raise = col3.number_input("Promotion Raise (%)", min_value=0, help="Ex.'When i get my promotion in 2 years, I expect a 5%\ raise.' Adjust to your scenario")

data.desired_cash = col2.number_input("Retirement Goal($)", min_value=0.0,value=0.0 , help="A lump sum amount expected to retire. Ex. $550,000 upon retirement")
data.annual_salary_raise = col3.number_input("Annual Salary Raise (%)", min_value=0.0, value=0.0, help="You expect to recieve an annual raise. Ex. 3%\ salary increase every year")

data.working_years = st.slider("Expected Working Years", min_value=1, max_value=99, help="The years you wish to project")   

# Code to prevent division by zero.
try:
    data.annual_salary_raise /= 100
    data.promo_raise /= 100
    data.savings_rate /=100
    data.interest_rate /= 100
except ZeroDivisionError:
    st.warning("Please enter a valid value greater than 1.")

    


## Displaying the inputs to the user.   
colA, colB, colC = st.columns(3)

colA.metric(label="Starting Salary", value=f"${data.starting_salary:,.2f}")
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

salary_grwth_rate = salaries_grwth_rate(salary_data)
st.write("## Salary Report")
with st.expander("View Report📜"):
    st.write(f"""
        ## Salary Report
            Total salary compensation: ${sum(salary_data['Salary']):,.2f}
            Total Working Years: {salary_data['Year'][-1] - data.current_year}
            Salary at {salary_data['Year'][-1]}: $ {salary_data['Salary'][-1]:,.2f}
            Nominal salary growth: {salary_grwth_rate}%
    """)

    

#<----------------------------------------------------------->

## This section will hold the wealth and cash saved section

st.write(f"""----------------------------------------""")

st.write("### Enter Wealth Data")


col1a, col2a = st.columns(2)
data.desired_cash = col1a.number_input("Desired Retirement Goal ($)", min_value= 0.0, value=data.desired_cash)
data.prior_wealth = col2a.number_input("Current Savings ($)", min_value=0, value=0, help="The current savings you have.")
data.savings_rate = st.slider("#### Savings Rate(%)", min_value=0, max_value=99, help="The percentage of you annual pay you save. Ex. 10%\ of your salary per year.")
data.savings_rate /= 100

colA1, colA2, colA3 = st.columns(3)
colA1.metric(label="Saving Rate", value=f"{(data.savings_rate*100):.1f}%")
colA2.metric(label="Current Asset Value", value=f"${data.prior_wealth:,.1f}")
colA3.metric(label="Desired Retirement Goal", value=f"${data.desired_cash:,.1f}")


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

# Determining their retirement year and money upon retirment
yrs_to_retire, wealth_at_retirement = years_to_retirement(data,wealth_that_year)


#<-------------------------------------->

# This section will summarize the journey to retirement.

st.write(f"""----------------------------------------""")
st.write(f"Wealth and Savings Report")

with st.expander("View Report📈"):
    st.write(f"""
        #### Wealth
            Forecast Years: {len(savings_n_wealths['Years past'])}
            Savings Rate (of salary): {(data.savings_rate*100):.2f}%
            Interest Rate: {(data.interest_rate*100):,.2f}%
            Total Savings: ${savings_n_wealths['Savings'][-1]:,.2f}
            Starting Wealth: ${data.prior_wealth:,.2f}
            Ending Wealth: ${savings_n_wealths['Wealth'][-1]:,.2f}
           
        """
    )
    st.write(f"""
        #### Retirement
            Expected Working Years: {data.working_years:d}
            Desired Retirment Cash: ${data.desired_cash:,.2f}
            Forecasted years to retirement financial goal: {yrs_to_retire:d}

            ** Amounts in the model are nominal.
            ** These are all estimates based on current inputs and
            serve as nominal (below the real/ above the real value).
        """
    )
""
""
# I don't need this in the acc model... 
#st.write(f"#### Would you like use an even better tool?")
#st.write(f"👇Help us fill out this short questionaire👇")
#st.link_button("Feedback", "https://forms.office.com/r/3F5FttxEmM")









