

## Module focuses on the testing and application of tax algorithms





# Tax deductions
SINGLE = 14000
MARRIED_FILING_JOINTLY  = 29200
HEAD_OF_HOUSE_HOLD = 21900

# Need to create a data class that'll hold tax brackets

@dataclass
class FederalTax:
    
    @dataclass
    class BracketRates:
        """Holds 2025 Canadian Federal tax rates """

        """Bracket 1: On the portion of taxable $57,375 or less"""
        F1_0_to_57375_: float = 0.15

        """Bracket 2: On the portion taxable income $52,375 to $114,750"""
        F2_57375_to_114750: float = 0.205

        """Bracket 3: On the portion $114,750 to $117882"""
        F3_114750_to_177882: float = 0.26

        """Bracket 4: On the portion $ 117,882 to $ 253,414"""
        F4_177882_to_253414: float = 0.29

        """Bracket 5: On the portion that's $253,414 and above"""
        F5_253414: float = 0.33

    @dataclass
    class BracketRanges:
        # Created Variables of the different minimums and maximum's in each tax bracket
        min_bracket_1: int = 0
        max_bracket_1: float = 57375

        min_bracket_2: int = 57375
        max_bracket_2: int = 114750

        min_bracket_3: int = 114750
        max_bracket_3: int = 117882

        min_bracket_4: int = 117882
        max_bracket_4: int = 253414

        min_bracket_5: int = 253414
  


# testing salary brackets

FT_RATE = FederalTax.BracketRates
FT_BRACKET = FederalTax.BracketRanges
salary = 100000

if salary in range(FT_BRACKET.min_bracket_1, FT_BRACKET.max_bracket_1):
    b1 = FT_BRACKET.max_bracket_1 * FT_RATE.F1_0_to_57375_
    total_tax = b1
    print(f"Your taxes are: ${total_tax}")

elif salary in range(FT_BRACKET.min_bracket_2, FT_BRACKET.max_bracket_2):

    b1 = FT_RATE.F1_0_to_57375_ * FT_BRACKET.max_bracket_1
    b2 = (salary - FT_BRACKET.max_bracket_2) * FT_RATE.F2_57375_to_114750
    total_tax = b1 + b2
    print(f"Your taxes are: ${total_tax}")





@dataclass
class OntarioTaxRates:
    """Holds the 2025 Ontario Tax Rates"""

    """On the portion $52,886 or less"""
    OT1: float = 52886

    """On the portion $52,886 to $105,775"""
    OT2: float = 105775