function deepDup(arr) {
    return arr.map((el) => {
        if (el instanceof Array) {
            return deepDup(el);
        } else {
            return el;
        }
    })
}