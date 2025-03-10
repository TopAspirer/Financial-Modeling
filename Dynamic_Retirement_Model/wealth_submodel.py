
## Module Holds all components of the wealth of the model.

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


def wealth_that_year(data, year, prior_wealth):
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
    wealth =  prior_wealth * (1 + data.interest_rate) + cash_saved
    return wealth


def cash_accumulator(data, cash_saved_during_year, working_years):
    """
    Takes the cash saved function and runs it through a loop that
    creates a list of the cashed saved over period of years.
    This function performs no calculations. It is simply to keep code
    in other modules clutter free.

    Parameters:
    - cash_saved_during_year() : A function
    - number of working years for the for loop 
    - Model data
    Returns:
    - A list of cash saved over a period of time.
    Ex. [1000,2000,4000,5000]
    """
    cash_savings = []

    for i in range(working_years):
        year = i + 1
        cash_saved = cash_saved_during_year(data, year)
        round(cash_saved,2)
        cash_savings.append(cash_saved)
    
    return cash_savings

def wealths_accumulator(data, working_years,wealth_that_year):
    """
    Returns a list of wealth accumulated over a period of years.

    Parameters:
    - data (dataclass)
    - working years (int)

    Returns:
    - List of accumulated wealth
    """
    prior_wealth = data.prior_wealth    #Start with the initial prior wealth
    wealths_accumulated = []

    for year in range(1, working_years+1):
        """
        See Model documentation so see how this works
        """
        wealth = wealth_that_year(data,year, prior_wealth)
        prior_wealth = round(wealth,2)      # Updates the prior_wealth for the next year.
        wealths_accumulated.append(prior_wealth)

    return wealths_accumulated


