
import salary_submodel as sf
def perc_to_deci(dict,list): 
    """
    This function converts the percentage rates
     in a dictionary into decimals and appends all the values to
    a list.

    * Used primarily in the inflation module.
    
    Parameters
    - dictionary with key
    ex. infl['jan'] ----> [1.0, 2.2...n.n]
    - a list that will hold the converted values
        
    Returns 
    -  The list that you passed will have all the
        numbers in it. 
    """
    for a in dict:
        deci_num = round(a / 100,5)
        list.append(deci_num)





def years_to_retirement(data):
    """
    Function runs a while loop untill the year
    your desired cash target is met. 

    Function returns two things, 
    the retirement year and the retirement amount($)
    """
    prior_wealth = 0 
    wealth = 0 
    year = 0

    print("Wealths over time: \n")
    while wealth < data.desired_cash:
        year = year + 1
        wealth = wealth_that_year(data,year, prior_wealth) 
        print(f"Your wealth in year {year}: ${wealth:,.2f}")
        prior_wealth = wealth

        if wealth >= data.desired_cash:
            retirement_year = year

    print(f"\nRetirement:")
    print(f"It will take {retirement_year} years to retire.")
    return retirement_year, wealth


