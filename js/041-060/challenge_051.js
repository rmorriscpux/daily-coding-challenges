/*
Given a function that generates perfectly random numbers between 1 and k (inclusive),
where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.
*/

// Function that returns an integer between 1 and k with equal probability.
function randInt(k) {
    // Check that k is valid: Number that can be resolved to a positive integer.
    const assert = require("assert");
    assert(typeof k == "number");
    assert(k >= 1);
    // Require integer k.
    k = Math.floor(k);
    // To get range from 1 to k, first multiply the random output [0, 1) by k, get the integer portion with Math.floor(), then add 1.
    return Math.floor(Math.random() * k) + 1;
}

// Card Shuffle function. Single for loop means O(N) time. Deck array is passed by reference.
function shuffleCards(deck) {
    // Start at the bottom of the deck and work upwards, getting a random swap position. After a position is swapped, it is locked in place.
    for (let cardPosition = deck.length-1; cardPosition > 0; cardPosition--) {
        // randInt gets numbers from 1 to k. We want numbers from 0 to k-1. 
        let swapPosition = randInt(cardPosition + 1) - 1;
        if (swapPosition != cardPosition) {
            let temp = deck[swapPosition];
            deck[swapPosition] = deck[cardPosition];
            deck[cardPosition] = temp;
        }
    }
    return;
}

// Build poker deck and test.
const suits = "♠♣♥♦";
const ranks = "A23456789TJQK";

const pokerDeck = [];
for (let s = 0; s < suits.length; s++) {
    for (let r = 0; r < ranks.length; r++) {
        pokerDeck.push(ranks.charAt(r) + suits.charAt(s));
    }
}

console.log(pokerDeck);
shuffleCards(pokerDeck);
console.log(pokerDeck);