
## This module will deal with everything regarding salary
## This module will house the the code for the json file that will hold the salary data. 

from dataclasses import dataclass


 

# Tax deductions
SINGLE = 14000
MARRIED_FILING_JOINTLY  = 29200
HEAD_OF_HOUSE_HOLD = 21900

# Need to create a data class that'll hold tax brackets

@dataclass
class FederalTaxRates:
    """Holds 2025 Canadian Federal tax rates """

    """On the portion of taxable $57,375 or less"""
    _0_to_57375_: float = 0.15

    """On the portion taxable income $52,375 to $114,750"""
    _57375_to_114750: float = 0.205

    """On the portion $114,750 to $117882"""
    _114750_to_177882: float = 0.26

    """On the portion $ 117,882 to $ 253,414"""
    _177882_to_253414: float = 0.29

    """On the portion $253,414"""
    _253414: float = 0.33

@dataclass
class FederalDeductions:
    SINGLE = 14000
    MARRIED_FILING_JOINTLY  = 29200
    HEAD_OF_HOUSE_HOLD = 21900


@dataclass
class OntarioTaxRates:
    """Holds the 2025 Ontario Tax Rates"""

    """On the portion $52,886 or less"""
    OT1: float = 52886

    """On the portion $52,886 to $105,775"""
    OT2: float = 105775


# testing progressive algo
salary = 105030

#if salary <= 105775:
 #   b1 = ON_rate_1 * 52886
  #  b2 = (salary - 52886 ) * ON_rate_2
    
  #  tax = b1 + b2 
  #  print(f"{tax:,.2f}")

#else:
#    print(f"Can't calculate salary")





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




