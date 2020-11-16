function titleize(str) {
    const littleWords = ["a", "and", "of", "over", "the"];

    let words = str.split(' ');
    let result = words.map( (word, idx) => {
        if (idx != 0 && littleWords.includes(word)) {
            return word.toLowerCase();
        } else {
            return word.slice(0,1).toUpperCase() + word.slice(1);
        };
    })

    return result.join(' ');
}