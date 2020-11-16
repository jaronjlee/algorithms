
Array.prototype.mergeSort = function (cb) {
    if (this.length <= 1) return this;

    if (!cb) cb = (left, right) => {
        if (left < right) {
            return -1;
        } else if (left > right) {
            return 1;
        } else return 0;
    }

    const mid = Math.floor(this.length / 2);
    const sortedLeft = this.slice(0,mid).mergeSort(cb);
    const sortedRight = this.slice(mid).mergeSort(cb);
    return merge(sortedLeft, sortedRight, cb);
};

function merge(left,right,cb) {
    let merged = [];

    while (left.length > 0 && right.length > 0) {
        if (cb(left[0], right[0]) === 1) {
            merged.push(right.shift());
        }
        else {
            merged.push(left.shift());
        }
    }

    merged = merged.concat(left, right);
    return merged;
}