

## This folder will primarilly manage the calculation and projection of inflation rates. 
## this will be a dictionary that contains the inflation rates of every month for the past 34 years.


import pandas as pnds
from model_functions import perc_to_deci


years = []
for year in range(1990,1999):
    years.append(year)


## Ended at 1998
## Alot more data to add
prev_infl_34_yrs ={
    'years': years,
    'jan': [5.5, 6.9, 1.6, 2.0, 1.3, 0.6, 1.6, 2.2, 1.1             ],
    'feb': [5.5, 6.2, 1.6, 2.4, 0.1, 1.9, 1.3, 2.3, 1.0             ],
    'mar': [5.3, 6.2, 1.6, 1.9, 0.2, 2.1, 1.5, 1.9, 1.0             ],
    'apr': [5.0, 6.2, 1.7, 1.8, 0.2, 2.5, 1.4, 1.7, 0.9             ],
    'may': [4.4, 6.3, 1.3, 1.9, -0.2, 2.9, 1.5, 1.5, 1.1            ],
    'jun': [4.4, 6.0, 1.1, 1.7, 0.0, 2.7, 1.3, 1.7, 1.0             ],
    'jul': [4.1, 6.0, 1.2, 1.8, 0.1, 2.6, 1.5, 1.7, 1.0             ],
    'aug': [4.1, 6.0, 1.1, 1.8, 0.1, 2.2, 1.3, 1.8, 0.9             ],
    'sep': [4.2, 5.5, 1.3, 1.8, 0.2, 2.2, 1.5, 1.7, 0.7             ],
    'oct': [4.7, 4.4, 1.6, 1.9, -0.2, 2.3, 1.8, 1.5, 1.1            ],
    'nov': [5.1, 4.1, 1.7, 1.9, -0.1, 2.1, 1.9, 0.9, 1.2            ],
    'dec': [5.0, 3.8, 2.2, 1.7, 0.2, 1.7, 2.2, 0.8, 1.0             ]
}

## for simplicity in later code, this dictionary will be assigned a different name
infl = prev_infl_34_yrs

## turning all the percentages in to decimals
jan_infl = []
feb_infl = []
mar_infl = []
apr_infl = []
may_infl = []
jun_infl = []
jul_infl = []
aug_infl = []
sep_infl = []
oct_infl = []
nov_infl = []
dec_infl = []

## converting all precentages into decimals
perc_to_deci(infl['jan'],jan_infl), perc_to_deci(infl['feb'],feb_infl), perc_to_deci(infl['mar'],mar_infl)
perc_to_deci(infl['apr'],apr_infl), perc_to_deci(infl['may'],may_infl), perc_to_deci(infl['jun'],jun_infl)
perc_to_deci(infl['jul'],jul_infl), perc_to_deci(infl['aug'],aug_infl), perc_to_deci(infl['sep'],sep_infl)
perc_to_deci(infl['oct'],oct_infl), perc_to_deci(infl['nov'],nov_infl), perc_to_deci(infl['dec'],dec_infl)

print(jul_infl)

