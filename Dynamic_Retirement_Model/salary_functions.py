
## This module will deal with everything regarding salary
## This module will house the the code for the json file that will hold the salary data. 



def salary_at_year (data, year):
    """
    Calculates the salary at a specific year.
    Parameters are: 
    - data (cost of living raise, promotion raise, and starting salary)
    - year (The specific year you would like to determine your salary amount)
    """
    num_promos = int(year / data.promos_every_n_years)
    num_promos
    salary_t = data.starting_salary * (1 + data.cost_living_raise)**year * (1 + data.promo_raise) ** num_promos
    return salary_t