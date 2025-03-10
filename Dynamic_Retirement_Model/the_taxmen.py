'''
-----------------------------------------------------
Module Holds all the federal and provincial tax data.
-----------------------------------------------------
Author: Top Aspirer
ID: HIM
Email: tendolloyd@gmail.com
Created:  Sometime in Feb 2025
'''

from dataclasses import dataclass


# Tax deductions
SINGLE = 14000
MARRIED_FILING_JOINTLY  = 29200
HEAD_OF_HOUSE_HOLD = 21900

# Need to create a data class that'll hold tax brackets

@dataclass
class FederalTax:
    
    @dataclass
    class BracketRates:
        """
        Holds 2025 Canadian Federal tax rates 
        Contains the tax rate for each tax bracket.
        Works in tandem with Bracketranges dataclass
        """

        """Bracket 1: """
        BRACKET_1: float = 0.10
        """Bracket 2: """
        BRACKET_2: float = 0.12
        """Bracket 3: """
        BRACKET_3: float = 0.22
        """Bracket 4: """
        BRACKET_4: float = 0.24
        """Bracket 5: """
        BRACKET_5: float = 0.32

    @dataclass
    class BracketRanges:
        """
        Contains the minimums and maximum incomes in each tax bracket
        """
        MIN_BRACKET_1: int = 0
        MAX_BRACKET_1: float = 20000

        MIN_BRACKET_2: int = 20001
        MAX_BRACKET_2: int = 80000

        MIN_BRACKET_3: int = 80001
        MAX_BRACKET_3: int = 175000

        MAX_BRACKET_4: int = 175001
        MAX_BRACKET_4: int = 330000

        MIN_BRACKET_5: int = 330001
        MAX_BRACKET_5: int = 450000
  

@dataclass
class OntarioTax:
    @dataclass
    class BracketRates:
        """
        Holds 2025 Ontario tax data.
        """

        """Bracket 1: """
        BRACKET_1: float = 0.10
        """Bracket 2: """
        BRACKET_2: float = 0.12
        """Bracket 3: """
        BRACKET_3: float = 0.22
        """Bracket 4: """
        BRACKET_4: float = 0.24
        """Bracket 5: """
        BRACKET_5: float = 0.32

    @dataclass
    class BracketRanges:
        """
        Contains the minimums and maximum of each bracket
        """
        MIN_BRACKET_1: int = 0
        MAX_BRACKET_1: float = 20000

        MIN_BRACKET_2: int = 20001
        MAX_BRACKET_2: int = 80000

        MIN_BRACKET_3: int = 80001
        MAX_BRACKET_3: int = 175000

        MAX_BRACKET_4: int = 175001
        MAX_BRACKET_4: int = 330000

        MIN_BRACKET_5: int = 330001
        MAX_BRACKET_5: int = 450000






