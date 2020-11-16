function jumbleSort(str, alpha=null) {
    if (!alpha) alpha = 'abcdefghijklmnopqrstuvwxyz'.split('');
    // alpha = alpha || 'abcdefghijklmnopqrstuvwxyz'.split('');
    str = str.split('');

    let sorted = false;

    while (!sorted) {
        sorted = true;
        for (let i = 0; i < (str.length - 1); i++) {
            let el1 = str[i];
            let el2 = str[i+1];

            if (alpha.indexOf(el1) > alpha.indexOf(el2)) {
                str[i] = el2;
                str[i+1] = el1;
                sorted = false;
            }
        }
    }

    return str.join('');
}