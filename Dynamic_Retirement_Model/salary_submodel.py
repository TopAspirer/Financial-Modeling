
'''
-----------------------------------------------------
This is module that acts as a submodel for the 
salary calculations component. 
-----------------------------------------------------
Author: Top Aspirer
ID: HIM
Email: tendolloyd@gmail.com
Started:  Jan 24, 2025
Completed: March 13,2025
'''
from math import pow

def salary_at_year (data, year):
    """
    Calculates the salary at a specific year.
    Parameters are: 
    - data (cost of living raise, promotion raise, and starting salary)
    - year (The specific year you would like to determine your salary amount)
    """
    if data.promos_every_n_years != 0:
        num_promos = int(year / data.promos_every_n_years)
    elif data.promos_every_n_years == 0 or data.promos_every_n_years < 0: 
        num_promos = 0 
    salary_t = data.starting_salary * (1 + data.cost_living_raise)**year * (1 + data.promo_raise) ** num_promos
    return salary_t

def salaries_grwth_rate(salary_data):
    """
    Function handles the growth rate
    of their salary over the specified period
    Parameters:
    - Salaries  (list)
    Returns:
    - grwth rate (float, percentage)
    """
    beg_salary = salary_data['Salary'][0]
    end_salary = salary_data['Salary'][-1]
    years = len(salary_data['Salary'])
    try:
        grwth_rate =  pow(end_salary/beg_salary, (1/years))-1
        grwth_rate = round(grwth_rate*100,2)
    except ZeroDivisionError:
        grwth_rate = 0
    return grwth_rate


# Function is made mainly for testing in the salary testing module
def salary_presenter(data,num_years):
    """
    This function was created to be used in other modules.
    It returns a list of salary compensation grouped by the year.

    Currently this function is in use in the wealth testing module.
    """
    promo_every_n_year = data.promos_every_n_years
    date_list = []
    salaries = []

    current_year = data.current_year + 1
    for a in range(num_years):  
        date_list.append(current_year + a )

    temp_current_yr = current_year

    promos_list = []
    promo_list_date = []
    MAX_RANGE_OF_PROMOS = current_year + 100

    for i in range(num_years):
        year = i + 1
        temp_current_yr = i + 1     
        salary =  round(salary_at_year(data, year), 2)
        salaries.append(salary)        
        
        
    return salaries, date_list
 










    


