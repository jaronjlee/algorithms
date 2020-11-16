Array.prototype.bubbleSort = function(cb) {

    if (!cb) cb = (a,b) => {
        if (a < b) {
            return -1;
        } else if (a === b) {
            return 0;
        } else {
            return 1;
        }
    }

    let result = this.slice()
    let sorted = false;

    while (!sorted) {
        sorted = true;

        for (let i = 0; i < (result.length - 1); i++) {
            let el1 = result[i];
            let el2 = result[i+1]
            if (cb(el1, el2) === 1) {
                result[i] = el2;
                result[i+1] = el1;
                // [result[i], result[i+1]] = [result[i+1], result[i]];
                sorted = false;
            }
        }
    }
    return result;
};