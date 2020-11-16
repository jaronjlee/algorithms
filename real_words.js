String.prototype.realWordsInString = function(dictionary) {
    let result = []
    let substrings = []

    let letters = this.split('')

    for (let i = 0; i < letters.length; i++) {
        for (let j = i; j < letters.length; j++) {
            let substring = letters.slice(i,j+1).join('');
            if (dictionary.includes(substring) && !result.includes(substring)) {
                result.push(substring);
            }
        }
    }

    return result.sort();
}