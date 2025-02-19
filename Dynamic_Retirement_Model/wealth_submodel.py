
## Module Holds all components of the wealth of the model.

from dataclasses import dataclass
from salary_submodel import salary_at_year


def cash_saved_during_year (data, year):
    """
    This function is a component of the overall
    wealth equation. Determines the cash saved 
    in any given year. This function is solving
    the end portion of the wealth equation 
    defined in the Outline of the markdown cell.

    Parameters:
    - model data (salary, savings rate)
    - year
    """
    salary = salary_at_year(data,year)
    cash_saved = salary * data.savings_rate
    return cash_saved


def wealth_that_year(data,salary_at_year, year):
    """
    Function determines the wealth in any given year.
    Parameters include:
    - data (interest rate)
    - cash saved (determined in another function)
    - prior wealth (determined in another function)

    The function does two things, calculates prior
    wealth and overall wealth.
    """
    cash_saved = cash_saved_during_year(data, year)
    prior_wealth = data.prior_wealth
    wealth =  prior_wealth * (1 + data.interest_rate) + cash_saved
    return wealth




