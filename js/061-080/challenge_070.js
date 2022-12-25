/*
A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
*/

// The partial solution for single digit n reveals a pattern:
// Perfect number n is equal to (n * 10) + (10 - n)
// This breaks down for n with more than one digit.
// The quickest way to find the nth perfect number beyond this is to find integers with digits that sum up to 10 or less, up to the nth one,
// then multiply that integer by 10, and add the digit that will make all digits sum to 10, i.e. 10 - base_digit_sum.
// This is quicker than naively finding all numbers with digits that add up to 10 exactly.

function nthPerfectNumber(n) {
    if (typeof(n) != 'number') throw TypeError("n must be a number.");
    if (n < 1) throw RangeError("n must be positive.");

    let perfNumBase = 0;
    let perfNumDigits = 0;
    let k = 0;
    let baseDigitSum = 0;

    while (k < n) {
        perfNumBase++;
        baseDigitSum = 0;
        perfNumDigits = perfNumBase;
        while (perfNumDigits > 0){
            baseDigitSum += perfNumDigits % 10;
            perfNumDigits = Math.floor(perfNumDigits / 10);
        }
        if (baseDigitSum <= 10){
            k++;
        }
    }

    return perfNumBase * 10 + 10 - baseDigitSum;
}

console.log(nthPerfectNumber(1));
console.log(nthPerfectNumber(2));
console.log(nthPerfectNumber(12345));