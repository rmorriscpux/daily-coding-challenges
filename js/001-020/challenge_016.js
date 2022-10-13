/*
You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

    record(order_id): adds the order_id to the log
    get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

You should be as efficient with time and space as possible.
*/

class OrderLog {
    constructor(N) {
        if (!isNaN(N)) {
            throw "Log limit must be a number.";
        }
        this.maxLogSize = Math.floor(N);
        this.log = [];
    }

    record(orderId) {
        this.log.unshift(orderId);
        if (this.log.length > this.maxLogSize) {
            this.log.pop();
        }
        return;
    }

    getLast(i) {
        return this.log[this.maxLogSize-i];
    }
}