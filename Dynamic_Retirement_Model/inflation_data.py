

## This folder will primarilly manage the calculation and projection of inflation rates. 
## this will be a dictionary that contains the inflation rates of every month for the past 34 years.


import pandas as pnds
import numpy as np
from model_functions import perc_to_deci


years = []
for year in range(1990,2025):
    years.append(year)


## Ended at 1998
## Alot more data to add
annual_infl_data_1990_to_2024 ={
    'years': years,
    'inflation': [4.8,5.6, 1.5, 1.9,0.2, 2.1,1.6, 1.6, 1.0, 1.7,
                  2.7,2.5,2.3, 2.8, 1.9, 2.2, 2.0, 2.1, 2.4, 0.3,
                  1.8, 2.9, 1.5, 0.9, 1.9, 1.1, 1.4, 1.6, 2.3,
                  1.9, 0.7, 3.4, 6.8, 3.9, 2.4, ]   
}

## for simplicity in later code, this dictionary will be assigned a different name
infl = annual_infl_data_1990_to_2024

## turning all the percentages in to decimals
yearly_infl = []


## converting all precentages into decimals
perc_to_deci(infl['inflation'],yearly_infl)

converted_infl_data ={
    'years': years,
    'inflation': yearly_infl
}


## Lowkey this data should be framed horizontally, not vertically. 
df =pnds.DataFrame(data = converted_infl_data)
print(df)







