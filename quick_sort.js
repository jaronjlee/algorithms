Array.prototype.quickSort = function (cb) {
    if (this.length < 2) return this;

    if (!cb) cb = (a, b) => {
        if (a < b) {
            return -1;
        }
        return 1;
    };

    const pivot = this[0];
    let left = [];
    let right = [];

    for (let i = 1; i < this.length; i++) {
        if (cb(this[i], pivot) === -1) {
            left.push(this[i]);
        }
        else {
            right.push(this[i]);
        }
    }

    let sortedLeft = left.quickSort(cb);
    let sortedRight = right.quickSort(cb);

    return sortedLeft.concat([pivot]).concat(sortedRight);

}