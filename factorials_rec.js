function factorialsRec(num) {
    if (num === 1) return [1];

    const prev = factorialsRec(num-1);
    const newNum = (num - 1) * prev[prev.length-1];
    prev.push(newNum);
    return prev
}
