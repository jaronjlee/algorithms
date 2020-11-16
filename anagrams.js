function anagrams(str1, str2) {
    const hash = {};

    str1.split('').forEach (char => {
        if (!hash[char]) hash[char] = 0;
        hash[char] += 1;
    })

    str2.split('').forEach (char => {
        if (!hash[char]) hash[char] = 0;
        hash[char] -= 1;
    })

    let keys = [];
    let values = [];

    for (key in hash) {
        keys.push(key);
        values.push(hash[key]);
    }

    for (let i = 0; i < values.length; i++) {
        if (values[i] !== 0) return false;
    }

    return true;
}