'''
The ancient Egyptians used to express fractions as a sum of several terms where each numerator is one.
For example, 4 / 13 can be represented as 1 / (4 + 1 / (18 + (1 / 468))).

Create an algorithm to turn an ordinary fraction a / b, where a < b, into an Egyptian fraction.
'''

from math import ceil
from typing import List

class Fraction:
    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator} / {self.denominator}"

    def __repr__(self) -> str:
        return str(self)
    
    def __add__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Cannot add Fraction with non-Fraction.")
        # Find LCD
        lower_denom = min(self.denominator, other.denominator)
        upper_denom = max(self.denominator, other.denominator)
        lower_factor = 1
        while (lower_denom * lower_factor) % upper_denom != 0:
            lower_factor += 1
        sum_denom = lower_denom * lower_factor
        upper_factor = sum_denom // upper_denom
        # Do addition of numerators based on which factor applies to which.
        if self.denominator < other.denominator:
            return Fraction((self.numerator * lower_factor) + (other.numerator * upper_factor), sum_denom)
        else:
            return Fraction((self.numerator * upper_factor) + (other.numerator * lower_factor), sum_denom)
    
    def __sub__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Cannot subtract Fraction with non-Fraction.")
        # Find LCD
        lower_denom = min(self.denominator, other.denominator)
        upper_denom = max(self.denominator, other.denominator)
        lower_factor = 1
        while (lower_denom * lower_factor) % upper_denom != 0:
            lower_factor += 1
        diff_denom = lower_denom * lower_factor
        upper_factor = diff_denom // upper_denom
        # Do subtraction of numerators based on which factor applies to which.
        if self.denominator < other.denominator:
            return Fraction((self.numerator * lower_factor) - (other.numerator * upper_factor), diff_denom)
        else:
            return Fraction((self.numerator * upper_factor) - (other.numerator * lower_factor), diff_denom)
    
    def toDecimal(self) -> float:
        return self.numerator / self.denominator
    
    def toEgyptianFraction(self) -> str:
        def rToEgyptianFraction(frac: Fraction, denominators: List[int]):
            if frac.numerator == 1:
                denominators.append(frac.denominator)
                return denominators
            
            egypt_frac = Fraction(1, ceil(frac.denominator / frac.numerator))
            denominators.append(egypt_frac.denominator)

            new_frac = frac - egypt_frac
            return rToEgyptianFraction(new_frac, denominators)
        
        if self.numerator == 1:
            return str(self)
        
        denominators = rToEgyptianFraction(self, [])
        egypt_frac_str = ""

        for d in denominators[:-1]:
            egypt_frac_str += f"1 / ({d} + "
        egypt_frac_str += f"(1 / {denominators[-1]}" + ")" * len(denominators)

        return egypt_frac_str
    
f = Fraction(4, 13)

print(f.toEgyptianFraction())

f2 = Fraction(1, 13)
print(f2.toEgyptianFraction())