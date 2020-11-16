function binarySearch(sortedArray, target) {
    if (sortedArray.length === 0) return -1;
    const midIdx = Math.floor(sortedArray.length/2);
    if (sortedArray[midIdx] === target) return midIdx;

    const left = sortedArray.slice(0,midIdx);
    const right = sortedArray.slice(midIdx + 1); //exclude mid ele
    
    if (target < sortedArray[midIdx]) {
        const result = binarySearch(left, target);
        if (result === -1) {
            return -1;
        } else {
            return result;
        }
    } else {
        const result = binarySearch(right, target);
        if (result === -1) {
            return -1;
        } else {
            return result + midIdx + 1;
        }
    }
}
