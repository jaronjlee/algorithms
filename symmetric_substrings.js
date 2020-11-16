String.prototype.symmetricSubstrings = function () {
    const result = [];

    for (let i = 0; i < this.length; i++) {
        for (let j = i+1; j < this.length; j++) {
            const sub = this.slice(i,j+1);
            const reversed = sub.split('').reverse().join('');
            if (sub === reversed) {
                result.push(sub);
            }
        }
    }

    return result.sort();
};