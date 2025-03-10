'''
-----------------------------------------------------
Module Holds all the federal and provincial tax 
calculation. Module is heavily dependent on the data
in the tax_men module.
-----------------------------------------------------
Author: Top Aspirer
ID: HIM
Email: tendolloyd@gmail.com
Created:  Monday 10, March, 2025
'''

from the_taxmen import FederalTax, OntarioTax

# Initializing Federal tax
FT_RATE = FederalTax.BracketRates
FT_BRACKET = FederalTax.BracketRanges

# Initializing Ontario tax
ON_rate = OntarioTax.BracketRates
ON_bracket = OntarioTax.BracketRanges


def calculate_federal_tax(salary):
    """
    Function handles the tax calculations for federal income taxes.
    Use: fed_taxed_amount = calculate_Ontario_tax(salary)
    Parameters:
    - Salary        (float < 0)
    Returns:
    - Taxed Amount  (float < 0)
    """
    brackets = [
        (FT_BRACKET.MIN_BRACKET_1, FT_BRACKET.MAX_BRACKET_1, FT_RATE.BRACKET_1),
        (FT_BRACKET.MIN_BRACKET_2, FT_BRACKET.MAX_BRACKET_2, FT_RATE.BRACKET_2),
        (FT_BRACKET.MIN_BRACKET_3, FT_BRACKET.MAX_BRACKET_3, FT_RATE.BRACKET_3),
        (FT_BRACKET.MAX_BRACKET_4, FT_BRACKET.MAX_BRACKET_4, FT_RATE.BRACKET_4),
        (FT_BRACKET.MIN_BRACKET_5, FT_BRACKET.MAX_BRACKET_5, FT_RATE.BRACKET_5),
    ]

    fed_taxed_amount = 0
    previous_limit = 0
    for min_limit, max_limit, rate in brackets:
        if salary > min_limit:
            taxable_income = min(salary, max_limit) - min_limit
            fed_taxed_amount += taxable_income * rate
        else:
            break

    return fed_taxed_amount

salary = 35000
taxed_amount = calculate_federal_tax(salary)
print(f"Total Taxes paid: ${taxed_amount}")


def calculate_Ontario_tax(salary):
    """
    Function handles the tax calculations for Ontario incomes.
    Use: ontario_taxed_amount = calculate_Ontario_tax(salary)
    Parameters:
    - Salary        (float < 0)
    Returns:
    - Taxed Amount  (float < 0)
    """
    brackets = [
        (ON_bracket.MIN_BRACKET_1, ON_bracket.MAX_BRACKET_1, ON_rate.BRACKET_1),
        (ON_bracket.MIN_BRACKET_2, ON_bracket.MAX_BRACKET_2, ON_rate.BRACKET_2),
        (ON_bracket.MIN_BRACKET_3, ON_bracket.MAX_BRACKET_3, ON_rate.BRACKET_3),
        (ON_bracket.MAX_BRACKET_4, ON_bracket.MAX_BRACKET_4, ON_rate.BRACKET_4),
        (ON_bracket.MIN_BRACKET_5, ON_bracket.MAX_BRACKET_5, ON_rate.BRACKET_5),
    ]

    ON_taxed_amount = 0
    previous_limit = 0
    for min_limit, max_limit, rate in brackets:
        if salary > min_limit:
            taxable_income = min(salary, max_limit) - min_limit
            ON_taxed_amount += taxable_income * rate
        else:
            break

    return ON_taxed_amount

salary = 35000
taxed_amount = calculate_federal_tax(salary)
print(f"Total Taxes paid: ${taxed_amount}")