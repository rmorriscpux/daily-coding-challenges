/*
The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
*/

// Set helper functions
Set.prototype.union = function(otherSet) {
    if (!otherSet instanceof Set){
        throw "Parameter must be a Set";
    }
    
    const unionSet = new Set(this.values());
    otherSet.forEach((v) => {
        unionSet.add(v);
    });

    return unionSet;
}

Set.prototype.compare = function(otherSet) {
    if (!otherSet instanceof Set){
        throw "Parameter must be a Set";
    }

    if (this.size != otherSet.size) {
        return false;
    }

    for (const value of this.values()) {
        if (!otherSet.has(value)){
            return false;
        }
    }

    return true;
}

// Building array of sets. Sets cannot contain sets as elements.
function createPowerSet(inputSet) {
    const powerSet = [new Set()];
    inputSet.forEach((value) => {
        powerSet.push(new Set([value]));
    });

    let u = new Set();
    let i = 1;
    while (i < powerSet.length) {
        for (let j = i+1; j < powerSet.length; j++) {
            u = powerSet[i].union(powerSet[j]);

            let inPowerSet = false;
            for (let k = 0; k < powerSet.length; k++) {
                if (u.compare(powerSet[k])){
                    inPowerSet = true;
                    break;
                }
            }

            if (!inPowerSet) {
                powerSet.push(u);
            }
        }
        i++;
    }

    return powerSet;
}

console.log(createPowerSet(new Set([1, 2, 3])));
console.log(createPowerSet(new Set([1, 2, 3, 4])));