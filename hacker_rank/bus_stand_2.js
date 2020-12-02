function kthPerson(k, p, q) {
    const newArr = []
    const memo = {}
    let busLow = Infinity
    for (let i = 0; i < q.length; i++) {
        if (memo.hasOwnProperty(q[i])) {
            newArr.push(memo[q[i]])
            continue
        }
        if (busLow <= q[i]) {
            newArr.push(memo[busLow])
            continue
        } 
        
        let counter = k;
        for (let j = 0; j < p.length; j++) {
            if (q[i] <= p[j]) counter -= 1
            if (counter === 0) {
                newArr.push(j + 1)
                memo[q[i]] = j + 1
                break;
            }
            if (j === p.length - 1) {
                busLow = Math.min(busLow, q[i]) 
                memo[q[i]] = 0
                newArr.push(0)                   
            }
        }
    }
    return newArr
}