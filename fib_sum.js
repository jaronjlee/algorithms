function fibsSum(n) {
    if (n === 1) return 1;
    if (n === 2) return 2;

    return fibsSum(n-1) + fib(n);
}

// f(2)[1, 1] 
// f(3)[1, 1, 2] 
// f(4)[1, 1, 2, 3] 
// f(5)[1, 1, 2, 3, 5] 
// f(6)[1, 1, 2, 3, 5, 8] 

function fib(n) {
    if (n === 1) return 1;
    if (n === 2) return 1;
    
    return fib(n-1) + fib(n-2)
}
