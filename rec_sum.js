function recSum(numArr) {
    if (numArr.length === 0) return 0;

    return numArr[0] + recSum(numArr.slice(1))
}