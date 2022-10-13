/*
Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
*/

function pickFromStream(stream) {
    let minVal = 1;
    let selection = stream[0];
    let randVal = 1;

    stream.forEach((s) => {
        randVal = Math.random();
        if (randVal < minVal){
            selection = s;
            minVal = randVal;
        }
    });

    return selection;
}