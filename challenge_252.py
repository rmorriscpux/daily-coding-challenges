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
        elif denominator < 0:
            numerator = -numerator
            denominator = -denominator
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator} / {self.denominator}"

    def __repr__(self) -> str:
        return str(self)
    
    # Fraction Addition
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
    
    # Fraction Subtraction
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
    
    # Problem Method.
    def toEgyptianFraction(self) -> str:
        def rToEgyptianFraction(frac: Fraction, denominators: List[int]):
            # End Case
            if frac.numerator == 0:
                return denominators
            
            # Fraction normalized to numerator of 1 and denominator rounded up to the nearest whole number. Add this denominator to list.
            egypt_frac = Fraction(1, ceil(frac.denominator / frac.numerator))
            denominators.append(egypt_frac.denominator)
            # Get the remainder fraction and recur with it.
            remainder = frac - egypt_frac
            return rToEgyptianFraction(remainder, denominators)
        
        # Get denominator list.
        denominators = rToEgyptianFraction(Fraction(abs(self.numerator), self.denominator), [])
        # Case: self.numerator = 0
        if not denominators:
            return str(self)

        # Convert to formatted string.
        egypt_frac_str = "-" if self.numerator < 0 else ""
        if len(denominators) == 1:
            egypt_frac_str += f"1 / {denominators[0]}" 
        else:
            for d in denominators[:-1]:
                egypt_frac_str += f"1 / ({d} + "
            egypt_frac_str += f"(1 / {denominators[-1]}" + ")" * len(denominators)

        return egypt_frac_str
    
f1 = Fraction(4, 13)
print(f1.toEgyptianFraction())

f2 = Fraction(1, 13)
print(f2.toEgyptianFraction())

f3 = Fraction(-4, 13)
print(f3.toEgyptianFraction())

f4 = Fraction(2, 16)
print(f4.toEgyptianFraction())