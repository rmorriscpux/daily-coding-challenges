/*
Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first,
the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
*/

Array.prototype.rgbSort = function() {
    let redPtr = 0;
    let bluePtr = this.length-1;
    if (redPtr >= bluePtr) {
        return;
    }

    while (this[redPtr] == 'R' && redPtr < this.length) {
        redPtr++;
    }
    while (this[bluePtr] == 'B' && bluePtr >= 0) {
        bluePtr--;
    }

    let swapPtr = redPtr;
    while (swapPtr <= bluePtr) {
        switch (this[swapPtr]) {
            case 'R':
                if (swapPtr > redPtr) {
                    let temp = this[redPtr];
                    this[redPtr] = this[swapPtr];
                    this[swapPtr] = temp;
                }
                redPtr++;
                break;
            case 'G':
                swapPtr++;
                break;
            case 'B':
                if (swapPtr < bluePtr) {
                    let temp = this[bluePtr];
                    this[bluePtr] = this[swapPtr];
                    this[swapPtr] = temp;
                }
                bluePtr--;
                break;
            default:
                throw "rgbSort(): All values in the array must be 'R', 'G', or 'B'.";
        }
        
        if (redPtr > swapPtr) {
            swapPtr = redPtr;
        }
    }
}

const testArray = ['G', 'B', 'R', 'R', 'B', 'R', 'G'];
testArray.rgbSort();
console.log(testArray);