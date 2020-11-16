function stringIncludeKey(string, key) {
    if (key.length === 0) return true;

    let nextKey = key[0];
    let i = string.indexOf(nextKey);

    if (i < 0) return false;
    return stringIncludeKey(string.slice(i+1), key.slice(1))
}
